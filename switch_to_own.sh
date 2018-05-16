gcloud container clusters get-credentials  kubeflow-seldon-ml --zone=us-east1-d	

kubectl config set-context $(kubectl config current-context) --namespace=kubeflow-seldon
