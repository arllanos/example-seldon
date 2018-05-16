gcloud container clusters get-credentials  kubeflow-seldon-ml --zone=us-central1-a

kubectl config set-context $(kubectl config current-context) --namespace=kubeflow-seldon
