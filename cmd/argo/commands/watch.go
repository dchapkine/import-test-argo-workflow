package commands

import (
	"context"
	"fmt"
	"io"
	"os"

	"github.com/argoproj/pkg/errors"
	log "github.com/sirupsen/logrus"
	"github.com/spf13/cobra"
	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	"k8s.io/apimachinery/pkg/fields"

	"github.com/argoproj/argo/cmd/argo/commands/client"
	workflowpkg "github.com/argoproj/argo/pkg/apiclient/workflow"

	wfv1 "github.com/argoproj/argo/pkg/apis/workflow/v1alpha1"
	"github.com/argoproj/argo/workflow/packer"
)

func NewWatchCommand() *cobra.Command {
	var (
		getArgs getFlags
	)

	var command = &cobra.Command{
		Use:   "watch WORKFLOW",
		Short: "watch a workflow until it completes",
		Run: func(cmd *cobra.Command, args []string) {
			if (len(args) != 1 && !getArgs.latest) || (len(args) > 0 && getArgs.latest) {
				cmd.HelpFunc()(cmd, args)
				os.Exit(1)
			}
			wfName := ""
			if len(args) > 0 {
				wfName = args[0]
			}
			watchWorkflow(wfName, getArgs)

		},
	}
	command.Flags().StringVar(&getArgs.status, "status", "", "Filter by status (Pending, Running, Succeeded, Skipped, Failed, Error)")
	command.Flags().StringVar(&getArgs.nodeFieldSelectorString, "node-field-selector", "", "selector of node to display, eg: --node-field-selector phase=abc")
	command.Flags().BoolVar(&getArgs.latest, "latest", false, "Watch last submitted workflow")
	return command
}

func watchWorkflow(wfName string, getArgs getFlags) {

	ctx, apiClient := client.NewAPIClient()
	serviceClient := apiClient.NewWorkflowServiceClient()
	namespace := client.Namespace()
	ctx, cancel := context.WithCancel(ctx)
	defer cancel()

	if getArgs.latest {
		var workflows wfv1.Workflows
		wfList, err := serviceClient.ListWorkflows(ctx, &workflowpkg.WorkflowListRequest{Namespace: namespace})
		errors.CheckError(err)
		workflows = append(workflows, wfList.Items...)
		if len(workflows) == 0 {
			fmt.Println("No workflows. Exiting")
			os.Exit(1)
		}
		min := workflows[0]
		for _, wf := range workflows {
			if wf.ObjectMeta.CreationTimestamp.Before(&min.ObjectMeta.CreationTimestamp) {
				min = wf
			}
		}
		wfName = min.ObjectMeta.Name
	} else {
		// ensure that the desired workflow exists
		_, err := serviceClient.GetWorkflow(ctx, &workflowpkg.WorkflowGetRequest{
			Name:      wfName,
			Namespace: namespace,
		})
		errors.CheckError(err)
	}

	req := &workflowpkg.WatchWorkflowsRequest{
		Namespace: namespace,
		ListOptions: &metav1.ListOptions{
			FieldSelector: fields.ParseSelectorOrDie(fmt.Sprintf("metadata.name=%s", wfName)).String(),
		},
	}
	stream, err := serviceClient.WatchWorkflows(ctx, req)
	errors.CheckError(err)
	for {
		event, err := stream.Recv()
		if err == io.EOF {
			log.Debug("Re-establishing workflow watch")
			stream, err = serviceClient.WatchWorkflows(ctx, req)
			errors.CheckError(err)
			continue
		}
		errors.CheckError(err)
		wf := event.Object
		if wf == nil {
			break
		}
		printWorkflowStatus(wf, getArgs)
		if !wf.Status.FinishedAt.IsZero() {
			return
		}
	}
}

func printWorkflowStatus(wf *wfv1.Workflow, getArgs getFlags) {
	err := packer.DecompressWorkflow(wf)
	errors.CheckError(err)
	print("\033[H\033[2J")
	print("\033[0;0H")
	fmt.Print(printWorkflowHelper(wf, getArgs))
}
