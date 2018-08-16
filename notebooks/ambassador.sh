kubectl port-forward $(kubectl get pod -n kubeflow-seldon -l service=ambassador -o jsonpath='{.items[0].metadata.name}') 8002:80
