PROJECT=banded-momentum-201921
ZONE=us-east1-d
CLUSTER=kubeflow-seldon-ml
gcloud beta container --project ${PROJECT} clusters create ${CLUSTER}  --zone=${ZONE} --cluster-version "1.9.6-gke.1" --image-type "COS" --disk-size "100" --num-nodes "3" 
gcloud compute disks create --project=${PROJECT} --zone=${ZONE} nfs-1 --description="PD to back NFS storage on GKE." --size=200GB
