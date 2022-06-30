#Starting the image creation and deployments

docker build -f app_images/Dockerfile -t flask-app .
docker build -f app_images/Dockerfile-consumer -t consumer-app .

kubectl create -f deployment/deployment.yml
kubectl create -f deployment/service.yml

kubectl create -f deployment/consumer-service.yml
kubectl create -f deployment/consumer-deployment.yml

echo "Deployments finished successfully"
