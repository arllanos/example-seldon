kubectl port-forward $(kubectl get pod  -l app=iefwk-configuration -o jsonpath='{.items[0].metadata.name}') 8889:8889
