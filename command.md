# MINIKUBE #
minikube --namespace=jenkins service jenkins

# KUBERNETES #
kubectl create clusterrolebinding jenkins --clusterrole cluster-admin --serviceaccount=jenkins:default