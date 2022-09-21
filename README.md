## Build our custom docker image

**Build docker file**

Syntax: 
```
sudo docker build . -f Dockerfile --pull --tag username/my-image:0.0.1
```

Example: 

```console
sudo docker build . -f Dockerfile --tag eliplam/hello_django:0.0.1
```

**Push image to docker hub**

You can push this repository to the registry designated by its name or tag.

Syntax:

```
docker push <hub-user>/<repo-name>:<tag>
```

Example:

```console
docker push eliplam/hello_django:0.0.1
```
Here is [my image](https://hub.docker.com/repository/docker/eliplam/hello_django) in Docker hub.

With that, we have our Dockerfile for the container image. You can now build an image based on your application requirements by running the following command:

```console
sudo docker build . --tag eliplam/hello_django:0.0.1
```

run:

```
sudo docker run -p 8080:8000 -v src:/hello-django --name hello_django_app hello_django:0.0.1 
```

-p: map port 8080 vao port 8000

delete container:

```
sudo docker rm -f hello_django_app
```


Execute container:

```console
docker exec -ti <container name> /bin/bash
```

Install sudo for Debian: 

```console
apt update
apt install sudo -y
```

psql -U postgres


-c = run command in database session, command is given in string
-t = skip header and footer
-q = silent mode for grep 
|| = logical OR, if grep fails to find match run the subsequent command


vao container postgres, sau do toi /usr/src/ chay script de khoi tao database.


We need to provide the deployment name and app image location (include the full repository url for images hosted outside Docker hub).

```console
kubectl create deployment <project-name> --image=gcr.io/google-samples/kubernetes-bootcamp:v1
```

```console
kubectl create deployment kubernetes-bootcamp --image=gcr.io/google-samples/kubernetes-bootcamp:v1
```

To list your deployments use the get deployments command:

```
kubectl get deployments
```

echo -e "\n\n\n\e[92mStarting Proxy. After starting it will not output a response. Please click the first Terminal Tab\n"; 
kubectl proxy


On Kubernetes, configuration variables can be injected using ConfigMaps and Secrets.
**Secrets** also store data in **base64**, while **ConfigMaps** store data in **plain text**.


kubernetes get deployments

```
kubectl get deployments
```

kubernetes get services

```
kubectl get services
```

kubernetes delete deployment

```
kubectl delete deployments <name-deployment>
```

kubernetes delete service 

```
kubectl delete service <name-serice>
```


# Deploy Postgres 

Data in PostgreSQL needs to be persisted for long term storage. The default location for storage in PostgreSQL is `/var/lib/postgresql/data`. However, Kubernetes pods are designed to have ephemeral storage, which means once a pod dies all the data within the pod is lost.

To mitigate against this, Kubernetes has the concept of volumes. There are several volume options, but the recommended type for databases is the PersistentVolume subsystem.

As a result, Kubernetes provides two API resources which are the `PersistentVolume` and `PersistentVolumeClaim`for setting volumes.

echo -n "<string>" | base64

Apply the files following:
    postgres/volume.yaml
    postgres/volume_claim.yaml
    postgres/secrets.ymal
    postgres/deployments.yaml
    postgres/service.yaml

Syntax: kubectl apply -f <filename.yaml>

kubectl exec -it <pod-name> bin/bash

in postgres container:
sudo pg_createcluster 14 main
/etc/postgresql/14/main
sudo service postgresql restart
Reference:

https://docs.docker.com/samples/django/
https://dockertraining.readthedocs.io/en/latest/django/