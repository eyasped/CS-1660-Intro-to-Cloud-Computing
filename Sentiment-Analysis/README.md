# **Steps to get the application to work on Google Kubernetes Engine.**
1. Run microservice based application on your machine
  1. install NodeJS and NPM in your computer 
  2. navigate to sa-frontend and excute **npm install**
  3. excute **npm start**
  4. excute the followin command to generte a build **npm run build**
  5. Install and start the Nginx WebServer
  6. Move the build file to ..nginx/html/
  7. Navigate to sa-webapp directory and run **mvn install**
  8. run **java -jar sentiment-analysis-web-0.0.1-SNAPSHOT.jar**
  9. Then excute **java -jar sentiment-analysis-web-0.0.1-SNAPSHOT.jar --sa.logic.api.url=http://localhost:5000**
  10. Navigate to sa-logic/sa and run **python -m pip install -r requirements.txt python -m textblob.download_corpora**
  11. start app using **python sentiment_analysis.py**
2. Build container images for each service
  1. Create a Docker file for each services 
  2. login to docker and navigate to frontend folder then run **docker build -f Dockerfile -t $DOCKER_USER_ID/sentiment-analysis-frontend .**
  3. then push the docker container **docker push $DOCKER_USER_ID/sentiment-analysis-frontend**
  4. then pull and run the image by using **docker pull $DOCKER_USER_ID/sentiment-analysis-frontend** and **docker run -d -p 80:80 $DOCKER_USER_ID/sentiment-analysis-frontend**
  5. Do the sane step for each 3 services
  6. at these step we should be able to run the application in our local machine

3. Now let us start using Kubernetes 
  1. install minikube then start Minicube by exuting **minikube start** 
  2. then run **kubectl get nodes** to see kubernetes clusters
  3. Create the SA Frontend pod by usig a command **kubectl create -f sa-frontend-pod.yaml**
  4. add labes to organize the kubernates resources.
  5. run **kubectl apply -f sa-frontend-pod.yaml** and **kubectl create -f service-sa-frontend-lb.yaml**
  6. do the kubernetes deployment for each service by running **kubectl apply -f sa-frontend-deployment.yaml**
  7. after doing so, we migrated the whole microservice application to a Kubernetes Cluster


