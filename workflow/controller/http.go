package controller

import (
	"bytes"
	"crypto/tls"
	"encoding/json"
	"fmt"
	"net/http"

	wfv1 "github.com/argoproj/argo/pkg/apis/workflow/v1alpha1"
)

func makeHTTPRequest(in *wfv1.HTTPArtifact) error {
	data, err := json.Marshal(in.Body)
	if err != nil {
		return err
	}
	req, err := http.NewRequest(in.Method, in.URL, bytes.NewBuffer(data))
	if err != nil {
		return err
	}
	for _, h := range in.Headers {
		req.Header.Add(h.Name, h.Value)
	}
	resp, err := (&http.Client{
		Transport: &http.Transport{TLSClientConfig: &tls.Config{InsecureSkipVerify: in.InsecureSkipVerify}},
		CheckRedirect: func(req *http.Request, via []*http.Request) error {
			return http.ErrUseLastResponse
		},
	}).Do(req)
	if err != nil {
		return err
	}
	if resp.StatusCode != 200 {
		return fmt.Errorf("HTTP request failed: %v", resp.Status)
	}
	return nil
}
