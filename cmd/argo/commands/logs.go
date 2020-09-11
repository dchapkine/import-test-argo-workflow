package commands

import (
	"context"
	"fmt"
	"io"
	"time"

	"github.com/spf13/cobra"
	corev1 "k8s.io/api/core/v1"
	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	"k8s.io/utils/pointer"

	"github.com/argoproj/argo/cmd/argo/commands/client"
	cmdcommon "github.com/argoproj/argo/cmd/argo/commands/common"
	workflowpkg "github.com/argoproj/argo/pkg/apiclient/workflow"
)

func NewLogsCommand() *cobra.Command {
	var (
		since     time.Duration
		sinceTime string
		tailLines int64
	)
	logOptions := &corev1.PodLogOptions{}
	var command = &cobra.Command{
		Use:   "logs WORKFLOW [POD]",
		Short: "view logs of a pod or workflow",
		Example: `# Print the logs of a workflow:

  argo logs my-wf

# Follow the logs of a workflows:

  argo logs my-wf --follow

# Print the logs of single container in a pod

  argo logs my-wf my-pod -c my-container

# Print the logs of a workflow's pods:

  argo logs my-wf my-pod

# Print the logs of a pods:

  argo logs --since=1h my-pod

# Print the logs of the latest workflow:
  argo logs @latest
`,
		RunE: func(cmd *cobra.Command, args []string) error {

			// parse all the args
			workflow := ""
			podName := ""

			switch len(args) {
			case 1:
				workflow = args[0]
			case 2:
				workflow = args[0]
				podName = args[1]
			default:
				cmd.HelpFunc()(cmd, args)
				return cmdcommon.MissingArgumentsError
			}

			if since > 0 && sinceTime != "" {
				return fmt.Errorf("--since-time and --since cannot be used together")
			}

			if since > 0 {
				logOptions.SinceSeconds = pointer.Int64Ptr(int64(since.Seconds()))
			}

			if sinceTime != "" {
				parsedTime, err := time.Parse(time.RFC3339, sinceTime)
				if err != nil {
					return err
				}
				sinceTime := metav1.NewTime(parsedTime)
				logOptions.SinceTime = &sinceTime
			}

			if tailLines >= 0 {
				logOptions.TailLines = pointer.Int64Ptr(tailLines)
			}

			// set-up
			ctx, apiClient := cmdcommon.CreateNewAPIClient()
			serviceClient := apiClient.NewWorkflowServiceClient()
			namespace := client.Namespace()

			return logWorkflow(ctx, serviceClient, namespace, workflow, podName, logOptions)
		},
	}
	command.Flags().StringVarP(&logOptions.Container, "container", "c", "main", "Print the logs of this container")
	command.Flags().BoolVarP(&logOptions.Follow, "follow", "f", false, "Specify if the logs should be streamed.")
	command.Flags().BoolVarP(&logOptions.Previous, "previous", "p", false, "Specify if the previously terminated container logs should be returned.")
	command.Flags().DurationVar(&since, "since", 0, "Only return logs newer than a relative duration like 5s, 2m, or 3h. Defaults to all logs. Only one of since-time / since may be used.")
	command.Flags().StringVar(&sinceTime, "since-time", "", "Only return logs after a specific date (RFC3339). Defaults to all logs. Only one of since-time / since may be used.")
	command.Flags().Int64Var(&tailLines, "tail", -1, "If set, the number of lines from the end of the logs to show. If not specified, logs are shown from the creation of the container or sinceSeconds or sinceTime")
	command.Flags().BoolVar(&logOptions.Timestamps, "timestamps", false, "Include timestamps on each line in the log output")
	command.Flags().BoolVar(&cmdcommon.NoColor, "no-color", false, "Disable colorized output")
	return command
}

func logWorkflow(ctx context.Context, serviceClient workflowpkg.WorkflowServiceClient, namespace, workflow, podName string, logOptions *corev1.PodLogOptions) error {
	// logs
	stream, err := serviceClient.PodLogs(ctx, &workflowpkg.WorkflowLogRequest{
		Name:       workflow,
		Namespace:  namespace,
		PodName:    podName,
		LogOptions: logOptions,
	})
	if err != nil {
		return err
	}

	// loop on log lines
	for {
		event, err := stream.Recv()
		if err == io.EOF {
			return nil
		}
		if err != nil {
			return err
		}
		fmt.Println(cmdcommon.ANSIFormat(fmt.Sprintf("%s: %s", event.PodName, event.Content), cmdcommon.ANSIColorCode(event.PodName)))
	}
}
