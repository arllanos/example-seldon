{
  global: {},
  components: {
    // Component-level parameters, defined initially from 'ks prototype use ...'
    // Each object below should correspond to a component in the components/ directory
    "kubeflow-core": {
      AmbassadorImage: "quay.io/datawire/ambassador:0.30.1",
      AmbassadorServiceType: "ClusterIP",
      StatsdImage: "quay.io/datawire/statsd:0.30.1",
      centralUiImage: "gcr.io/kubeflow-images-public/centraldashboard:v20180618-v0.2.0-rc.0-5-g715aafc8-e3b0c4",
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
      tfDefaultImage: "null",
      tfJobImage: "gcr.io/kubeflow-images-public/tf_operator:v20180615-b2ac020",
      tfJobUiServiceType: "ClusterIP",
      tfJobVersion: "v1alpha2",
      usageId: "A9FBC2DC-5B64-43BA-ACE2-E0439BFD5731"
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