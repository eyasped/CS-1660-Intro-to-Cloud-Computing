**Steps you used to run your Docker images on Kubernetes Engine**
1. Search for working image and select the one you want
2. Pull the image using command like *docker pull jupyter/all-spark-notebook*
3. Create a dockerfile and build the docker * docker build -f Dockerfile -t $DOCKER_USER_ID/<image-name .*
4. tag the image using *docker image tag jupyter/all-spark-notebook eyasped/jupyter:new*
5. Then push the docker container docker *push $DOCKER_USER_ID/<image-name>*
6. using the same step pull, tag, build and push the image for the other applications as well
6. Start Minicube by exuting minikube start
7. Create a yaml deloyment file 
9. create a pod and deployment in kubernetes using commands like *kubectl create -f jupyter-notebook-deployment.yaml*
  *kubectl apply -f jupyter-notebook-deployment.yaml*
10. Then run kubectl get nodes to see kubernetes clusters
 
 
**to Start up the CLI app go to the main.py and open it**
then follow the following instruction
1. Appache Hadoop
2. Appache Spark
3. Jupyter Notebook
4. SonarQube and SonarScanner
Enter q to quit.

The options are not linked to any of the links at the moment. 
