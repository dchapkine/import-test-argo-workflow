package cron

import (
	"encoding/json"
	"fmt"
	"strings"

	"github.com/argoproj/pkg/humanize"
	"github.com/spf13/cobra"
	"sigs.k8s.io/yaml"

	"github.com/argoproj/argo/cmd/argo/commands/client"
	cmdcommon "github.com/argoproj/argo/cmd/argo/commands/common"
	"github.com/argoproj/argo/pkg/apiclient/cronworkflow"
	wfv1 "github.com/argoproj/argo/pkg/apis/workflow/v1alpha1"
)

func NewGetCommand() *cobra.Command {
	var (
		output string
	)

	var command = &cobra.Command{
		Use:   "get CRON_WORKFLOW...",
		Short: "display details about a cron workflow",
		RunE: func(cmd *cobra.Command, args []string) error {
			if len(args) == 0 {
				cmd.HelpFunc()(cmd, args)
				return cmdcommon.MissingArgumentsError
			}

			ctx, apiClient := cmdcommon.CreateNewAPIClient()
			serviceClient := apiClient.NewCronWorkflowServiceClient()
			namespace := client.Namespace()

			for _, arg := range args {
				cronWf, err := serviceClient.GetCronWorkflow(ctx, &cronworkflow.GetCronWorkflowRequest{
					Name:      arg,
					Namespace: namespace,
				})
				if err != nil {
					return err
				}
				err = printCronWorkflow(cronWf, output)
				if err != nil {
					return err
				}
			}
			return nil
		},
	}

	command.Flags().StringVarP(&output, "output", "o", "", "Output format. One of: json|yaml|wide")
	return command
}

func printCronWorkflow(wf *wfv1.CronWorkflow, outFmt string) error {
	switch outFmt {
	case "name":
		fmt.Println(wf.ObjectMeta.Name)
	case "json":
		outBytes, _ := json.MarshalIndent(wf, "", "    ")
		fmt.Println(string(outBytes))
	case "yaml":
		outBytes, _ := yaml.Marshal(wf)
		fmt.Print(string(outBytes))
	case "wide", "":
		fmt.Print(getCronWorkflowGet(wf))
	default:
		return fmt.Errorf("Unknown output format: %s", outFmt)
	}
	return nil
}

func getCronWorkflowGet(wf *wfv1.CronWorkflow) string {
	const fmtStr = "%-30s %v\n"

	out := ""
	out += fmt.Sprintf(fmtStr, "Name:", wf.ObjectMeta.Name)
	out += fmt.Sprintf(fmtStr, "Namespace:", wf.ObjectMeta.Namespace)
	out += fmt.Sprintf(fmtStr, "Created:", humanize.Timestamp(wf.ObjectMeta.CreationTimestamp.Time))
	out += fmt.Sprintf(fmtStr, "Schedule:", wf.Spec.Schedule)
	out += fmt.Sprintf(fmtStr, "Suspended:", wf.Spec.Suspend)
	if wf.Spec.Timezone != "" {
		out += fmt.Sprintf(fmtStr, "Timezone:", wf.Spec.Timezone)
	}
	if wf.Spec.StartingDeadlineSeconds != nil {
		out += fmt.Sprintf(fmtStr, "StartingDeadlineSeconds:", *wf.Spec.StartingDeadlineSeconds)
	}
	if wf.Spec.ConcurrencyPolicy != "" {
		out += fmt.Sprintf(fmtStr, "ConcurrencyPolicy:", wf.Spec.ConcurrencyPolicy)
	}
	if wf.Status.LastScheduledTime != nil {
		out += fmt.Sprintf(fmtStr, "LastScheduledTime:", humanize.Timestamp(wf.Status.LastScheduledTime.Time))
	}

	next, err := wf.GetNextRuntime()
	if err == nil {
		out += fmt.Sprintf(fmtStr, "NextScheduledTime:", humanize.Timestamp(next))
	}

	if len(wf.Status.Active) > 0 {
		var activeWfNames []string
		for _, activeWf := range wf.Status.Active {
			activeWfNames = append(activeWfNames, activeWf.Name)
		}
		out += fmt.Sprintf(fmtStr, "Active Workflows:", strings.Join(activeWfNames, ", "))
	}
	if len(wf.Status.Conditions) > 0 {
		out += wf.Status.Conditions.DisplayString(fmtStr, map[wfv1.ConditionType]string{wfv1.ConditionTypeSubmissionError: "✖"})
	}
	if len(wf.Spec.WorkflowSpec.Arguments.Parameters) > 0 {
		out += fmt.Sprintf(fmtStr, "Workflow Parameters:", "")
		for _, param := range wf.Spec.WorkflowSpec.Arguments.Parameters {
			if param.Value == nil {
				continue
			}
			out += fmt.Sprintf(fmtStr, "  "+param.Name+":", *param.Value)
		}
	}
	return out
}
