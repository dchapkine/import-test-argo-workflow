package metrics

import (
	"context"
	"fmt"
	"io"
	"net/http"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestDisableMetricsServer(t *testing.T) {
	config := ServerConfig{
		Enabled: false,
		Path:    DefaultMetricsServerPath,
		Port:    DefaultMetricsServerPort,
	}
	m := New(config, config)

	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()

	m.RunServer(ctx, false)
	_, err := http.Get(fmt.Sprintf("http://localhost:%d%s", DefaultMetricsServerPort, DefaultMetricsServerPath))
	assert.Contains(t, err.Error(), "connection refused") // expect that the metrics server not to start
}

func TestMetricsServer(t *testing.T) {
	config := ServerConfig{
		Enabled: true,
		Path:    DefaultMetricsServerPath,
		Port:    DefaultMetricsServerPort,
	}
	m := New(config, config)

	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()

	m.RunServer(ctx, false)
	resp, err := http.Get(fmt.Sprintf("http://localhost:%d%s", DefaultMetricsServerPort, DefaultMetricsServerPath))
	assert.NoError(t, err)
	assert.Equal(t, http.StatusOK, resp.StatusCode)

	defer resp.Body.Close()

	bodyBytes, err := io.ReadAll(resp.Body)
	assert.NoError(t, err)

	bodyString := string(bodyBytes)
	assert.NotEmpty(t, bodyString)
}

func TestDummyMetricsServer(t *testing.T) {
	config := ServerConfig{
		Enabled: true,
		Path:    DefaultMetricsServerPath,
		Port:    DefaultMetricsServerPort,
	}
	m := New(config, config)

	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()

	m.RunServer(ctx, true)
	resp, err := http.Get(fmt.Sprintf("http://localhost:%d%s", DefaultMetricsServerPort, DefaultMetricsServerPath))
	assert.NoError(t, err)
	assert.Equal(t, http.StatusOK, resp.StatusCode)

	defer resp.Body.Close()

	bodyBytes, err := io.ReadAll(resp.Body)
	assert.NoError(t, err)

	bodyString := string(bodyBytes)

	assert.Empty(t, bodyString) // expect the dummy metrics server to provide no metrics responses
}
