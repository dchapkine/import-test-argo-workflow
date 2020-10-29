package http

import (
	workflowpkg "github.com/argoproj/argo/pkg/apiclient/workflow"
)

type podLogsClient struct{ serverSentEventsClient }

func (f *podLogsClient) Recv() (*workflowpkg.LogEntry, error) {
	v := &workflowpkg.LogEntry{}
	return v, f.RecvEvent(v)
}
