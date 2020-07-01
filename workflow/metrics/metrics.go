package metrics

import (
	"fmt"
	"k8s.io/client-go/util/workqueue"
	"time"

	"github.com/prometheus/client_golang/prometheus"

	"github.com/argoproj/argo/pkg/apis/workflow/v1alpha1"
)

const (
	argoNamespace            = "argo"
	workflowsSubsystem       = "workflows"
	DefaultMetricsServerPort = "9090"
	DefaultMetricsServerPath = "/metrics"
)

type ServerConfig struct {
	Enabled      bool
	Path         string
	Port         string
	TTL          time.Duration
	IgnoreErrors bool
}

func (s ServerConfig) SameServerAs(other ServerConfig) bool {
	return s.Port == other.Port && s.Path == other.Path && s.Enabled && other.Enabled
}

type metric struct {
	metric      prometheus.Metric
	lastUpdated time.Time
}

type Metrics struct {
	metricsConfig   ServerConfig
	telemetryConfig ServerConfig

	workflowsProcessed prometheus.Counter
	workflowsByPhase   map[v1alpha1.NodePhase]prometheus.Gauge
	operationDurations prometheus.Histogram
	errors             map[ErrorCause]prometheus.Counter
	customMetrics      map[string]metric
	workqueueMetrics   map[string]prometheus.Metric

	// Used to quickly check if a metric desc is already used by the system
	defaultMetricDescs map[string]bool
}

var _ prometheus.Collector = Metrics{}

func New(metricsConfig, telemetryConfig ServerConfig) Metrics {
	metrics := Metrics{
		metricsConfig:      metricsConfig,
		telemetryConfig:    telemetryConfig,
		workflowsProcessed: newCounter("workflows_processed_count", "Number of workflow updates processed", nil),
		workflowsByPhase:   getWorkflowPhaseGauges(),
		operationDurations: newHistogram("operation_duration_seconds", "Histogram of durations of operations", nil, []float64{0.1, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.5, 3.0}),
		errors:             getErrorCounters(),
		customMetrics:      make(map[string]metric),
		workqueueMetrics:   make(map[string]prometheus.Metric),
		defaultMetricDescs: make(map[string]bool),
	}

	for _, metric := range metrics.allMetrics() {
		metrics.defaultMetricDescs[metric.Desc().String()] = true
	}

	return metrics
}

func (m Metrics) allMetrics() []prometheus.Metric {
	allMetrics := []prometheus.Metric{
		m.workflowsProcessed,
		m.operationDurations,
	}
	for _, metric := range m.workflowsByPhase {
		allMetrics = append(allMetrics, metric)
	}
	for _, metric := range m.errors {
		allMetrics = append(allMetrics, metric)
	}
	for _, metric := range m.workqueueMetrics {
		allMetrics = append(allMetrics, metric)
	}
	for _, metric := range m.customMetrics {
		allMetrics = append(allMetrics, metric.metric)
	}

	return allMetrics
}

func (m Metrics) WorkflowAdded(phase v1alpha1.NodePhase) {
	if _, ok := m.workflowsByPhase[phase]; ok {
		m.workflowsByPhase[phase].Inc()
	}
}

func (m Metrics) WorkflowUpdated(fromPhase, toPhase v1alpha1.NodePhase) {
	m.WorkflowDeleted(fromPhase)
	m.WorkflowAdded(toPhase)
}

func (m Metrics) WorkflowDeleted(phase v1alpha1.NodePhase) {
	if _, ok := m.workflowsByPhase[phase]; ok {
		m.workflowsByPhase[phase].Dec()
	}
}

func (m Metrics) OperationCompleted(durationSeconds float64) {
	m.operationDurations.Observe(durationSeconds)
}

func (m Metrics) GetCustomMetric(key string) prometheus.Metric {
	// It's okay to return nil metrics in this function
	return m.customMetrics[key].metric
}

func (m Metrics) UpsertCustomMetric(key string, newMetric prometheus.Metric) error {
	if _, inUse := m.defaultMetricDescs[newMetric.Desc().String()]; inUse {
		return fmt.Errorf("metric '%s' is already in use by the system, please use a different name", newMetric.Desc())
	}
	m.customMetrics[key] = metric{metric: newMetric, lastUpdated: time.Now()}
	return nil
}

type ErrorCause string

const (
	ErrorCauseOperationPanic              ErrorCause = "OperationPanic"
	ErrorCauseCronWorkflowSubmissionError ErrorCause = "CronWorkflowSubmissionError"
)

func (m Metrics) OperationPanic() {
	m.errors[ErrorCauseOperationPanic].Inc()
}

func (m Metrics) CronWorkflowSubmissionError() {
	m.errors[ErrorCauseCronWorkflowSubmissionError].Inc()
}

var _ workqueue.MetricsProvider = Metrics{}



func (m Metrics) NewDepthMetric(name string) workqueue.GaugeMetric {
	key := fmt.Sprintf("%s-depth", name)
	if _, ok := m.workqueueMetrics[key]; !ok {
		m.workqueueMetrics[key] = newGauge("queue_depth_count", "Depth of the queue", map[string]string{"queue_name": name})
	}
	return m.workqueueMetrics[key].(prometheus.Gauge)
}

func (m Metrics) NewAddsMetric(name string) workqueue.CounterMetric {
	key := fmt.Sprintf("%s-adds", name)
	if _, ok := m.workqueueMetrics[key]; !ok {
		m.workqueueMetrics[key] = newCounter("queue_adds_count", "Adds to the queue", map[string]string{"queue_name": name})
	}
	return m.workqueueMetrics[key].(prometheus.Counter)
}

// These metrics are not relevant to be exposed
type noopMetric struct{}

func (noopMetric) Inc()            {}
func (noopMetric) Dec()            {}
func (noopMetric) Set(float64)     {}
func (noopMetric) Observe(float64) {}

func (m Metrics) NewLatencyMetric(name string) workqueue.HistogramMetric      { return noopMetric{} }
func (m Metrics) NewRetriesMetric(name string) workqueue.CounterMetric        { return noopMetric{} }
func (m Metrics) NewWorkDurationMetric(name string) workqueue.HistogramMetric { return noopMetric{} }
func (m Metrics) NewUnfinishedWorkSecondsMetric(name string) workqueue.SettableGaugeMetric {
	return noopMetric{}
}
func (m Metrics) NewLongestRunningProcessorSecondsMetric(name string) workqueue.SettableGaugeMetric {
	return noopMetric{}
}
