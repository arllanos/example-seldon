local params = std.extVar("__ksonnet/params");
local globals = import "globals.libsonnet";
local envParams = params + {
  components+: {
    "kubeflow-core"+: {
      cloud: "gke"
    }
  }
};

{
  components: {
    [x]: envParams.components[x] + globals for x in std.objectFields(envParams.components)
  }
}