package validation

import (
	"fmt"
	"strings"
	"testing"
)

func TestValidateExamples(t *testing.T) {
	failures, err := ValidateArgoYamlRecursively(".", []string{"testvolume.yaml", "global-parameters-from-configmap.yaml", "arguments-parameters-from-configmap.yaml"})
	if err != nil {
		t.Errorf("There was an error: %s", err)
	}
	if len(failures) > 0 {
		fails := []string{}
		for path, fail := range failures {
			fails = append(fails, fmt.Sprintf("Validation failed - %s: %s", path, strings.Join(fail, "\n")))
		}
		t.Errorf("There were validation failures:\n%s", strings.Join(fails, "\n"))
	}
}
