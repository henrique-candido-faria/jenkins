# MINIKUBE #
minikube start
minikube status
minikube ip
minikube delete
minikube --namespace=jenkins service jenkins

# KUBERNETES #
kubectl create -f
kubectl create namespace jenkins
kubectl create -f jenkins/ -n jenkins
kubectl create clusterrolebinding jenkins --clusterrole cluster-admin --serviceaccount=jenkins:default

# JENKINS #
cat /var/jenkins_home/secrets/initialAdminPassword