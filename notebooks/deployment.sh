kubectl port-forward $(kubectl get pod -l app=iefwk-ie-deployment -o jsonpath='{.items[0].metadata.name}') 8886:8886
