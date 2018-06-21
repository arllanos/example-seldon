{
  global: {},
  components: {
    // Component-level parameters, defined initially from 'ks prototype use ...'
    // Each object below should correspond to a component in the components/ directory
    "kubeflow-core": {
      cloud: "null",
      disks: "nfs-1",
      jupyterHubAuthenticator: "null",
      jupyterHubImage: "gcr.io/kubeflow/jupyterhub-k8s:v20180531-3bb991b1",
      jupyterHubServiceType: "ClusterIP",
      jupyterNotebookPVCMount: "null",
      jupyterNotebookRegistry: "gcr.io",
      jupyterNotebookRepoName: "kubeflow-images-public",
      name: "kubeflow-core",
      namespace: "kubeflow-seldon",
      reportUsage: true,
      tfAmbassadorImage: "quay.io/datawire/ambassador:0.30.1",
      tfAmbassadorServiceType: "ClusterIP",
      tfDefaultImage: "null",
      tfJobImage: "gcr.io/kubeflow-images-public/tf_operator:v20180522-77375baf",
      tfJobUiServiceType: "ClusterIP",
      tfJobVersion: "v1alpha1",
      tfStatsdImage: "quay.io/datawire/statsd:0.30.1",
      usageId: "D6EDEEE2-7CCF-4DF9-887C-0160E64AFA1B"
    },
    seldon: {
      apifeImage: "seldonio/apife:0.1.6",
      apifeServiceType: "NodePort",
      engineImage: "seldonio/engine:0.1.6",
      name: "seldon",
      namespace: "kubeflow-seldon",
      operatorImage: "seldonio/cluster-manager:0.1.6",
      operatorJavaOpts: "null",
      operatorSpringOpts: "null",
      withApife: "false",
      withRbac: "true"
    },
    argo: {
      imageTag: "latest",
      name: "argo",
      namespace: "kubeflow-seldon"
    }
  }
}