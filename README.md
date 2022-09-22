- [Docker](#docker)
  - [Build our custom docker image](#build-our-custom-docker-image)
  - [Deploy with Docker Compose](#deploy-with-docker-compose)
- [Kubernetes](#kubernetes)
  - [Install kubectl](#install-kubectl)
  - [Install minikube](#install-minikube)
  - [Deploy Postgres](#deploy-postgres)
  - [Deploy Django](#deploy-django)
  - [More Commands](#more-commands)

# Docker
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
docker push eliplam/hello_django:only_postgres
# or
docker push eliplam/hello_django:0.0.1
```
Here is [my image](https://hub.docker.com/repository/docker/eliplam/hello_django) in Docker hub.

With that, we have our Dockerfile for the container image. You can now build an image based on your application requirements by running the following command:

```console
sudo docker build . --tag eliplam/hello_django:0.0.1
```

**run only django**:

```
sudo docker run -p 8080:8000 -v src:/hello-django --name hello_django_app hello_django:0.0.1 
```

`-p`: mapping port from 8080 to 8000

**delete container**:

```
sudo docker rm -f hello_django_app
```


**Execute container**:

```console
docker exec -ti <container name> /bin/bash
```

**Install sudo for Debian**: 

```console
apt update
apt install sudo -y
```
## Deploy with Docker Compose

At root folder, run:

```console
sudo docker-compose up
```

Then open new terminal, execute in to container postgres container:

```console
docker exec -it <postgres-container-name> /bin/bash 
```

After that run command bellow to create database and import data:

```
cd /usr/src
bash creat_scripts.sh
bash import_data.sh
```

**Advance**

Run command to use postgres with terminal:

```console
psql -U postgres
```

Click [here](https://www.geeksforgeeks.org/postgresql-psql-commands/) for more command.

# Kubernetes

We need to provide the deployment name and app image location (include the full repository url for images hosted outside Docker hub).


## Install kubectl

Install [here](https://kubernetes.io/docs/tasks/tools/)


## Install minikube

Install [here](https://kubernetes.io/vi/docs/tasks/tools/install-minikube/)

## Deploy Postgres 

Data in PostgreSQL needs to be persisted for long term storage. The default location for storage in PostgreSQL is `/var/lib/postgresql/data`. However, Kubernetes pods are designed to have ephemeral storage, which means once a pod dies all the data within the pod is lost.

To mitigate against this, Kubernetes has the concept of volumes. There are several volume options, but the recommended type for databases is the PersistentVolume subsystem.

As a result, Kubernetes provides two API resources which are the `PersistentVolume` and `PersistentVolumeClaim`for setting volumes.

`echo -n "<string>" | base64`

At root folder, run:

```console
cd kubernetes/
```

Apply the files following:

- postgres/volume.yaml
- postgres/volume_claim.yaml
- postgres/secrets.yaml
- postgres/deployments.yaml
- postgres/service.yaml


with syntax: `kubectl apply -f <filename.yaml>`

```kubectl exec -it <pod-postgres-name> -- bin/bash```

**Note**: pre-requirement: install vim.

Use psql with username postgres:

```console
psql -U postgres
```

**Fixed**: 
> psql: error: connection to server on socket "/var/run/postgresql/.s.PGSQL.5432" failed: No such file or directory.	Is the server running locally and accepting connections on that socket?

Run postgresql in postgres container:

```console
pg_createcluster 14 main
service postgresql restart
```


**Fixed**:
> psql: error: connection to server on socket "/var/run/postgresql/.s.PGSQL.5432" failed: FATAL:  Peer authentication failed for user "postgres"

In `/etc/postgresql/14/main/pg_hba.conf` at the last file, change method: `peer` to `trust`.

From: 
```
# Database administrative login by Unix domain socket
local   all             postgres                                peer

# TYPE  DATABASE        USER            ADDRESS                 METHOD

# "local" is for Unix domain socket connections only
local   all             all                                     peer
...
# Allow replication connections from localhost, by a user with the
# replication privilege.
local   replication     all                                     peer
...
```

To:

```
# Database administrative login by Unix domain socket
local   all             postgres                                trust

# TYPE  DATABASE        USER            ADDRESS                 METHOD

# "local" is for Unix domain socket connections only
local   all             all                                     trust
...
# Allow replication connections from localhost, by a user with the
# replication privilege.
local   replication     all                                     trust
```
Then run:

```console
service postgresql restart
```


**Fixed**: 
> PG::ConnectionBad (FATAL: pg_hba.conf rejects connection for host "172.17.0.1", user "XXX", database "XXX", SSL off ):

- add: host all all 0.0.0.0/0 trust 

```
...
# "local" is for Unix domain socket connections only
local   all             all                                     trust
host    all             all             0.0.0.0/0               trust
...                       
```

then restart postgresql:
```console
sudo service postgresql restart
```

Run this command to create database:
```
psql -U postgres -c "\set AUTOCOMMIT on"
# create dota2 database if not exists.
psql -U postgres -tc "SELECT 1 FROM pg_database WHERE datname = 'dota2'" | grep -q 1 | psql -U postgres -c "CREATE DATABASE dota2"
# psql -U postgres -c "CREATE DATABASE dota2;"

# connect to dota2 database and create tables.
psql -U postgres -d dota2 -c "
CREATE TABLE IF NOT EXISTS hero (
  hero_id INTEGER NOT NULL, 
  hero_name character varying,
  pro_Win INTEGER,
  pro_pick INTEGER
);
CREATE TABLE IF NOT EXISTS player (
  player_id REAL NOT NULL, 
  rank_tier REAL,
  win REAL,
  lose REAL,
  mmr_estimate REAL
);"

# connect to dota2 database and import sample data.
psql -U postgres -d dota2 -c "
INSERT INTO hero (hero_id,hero_name,pro_win,pro_pick) 
VALUES (1,'antimage',46,95),
(2,'axe',20,46),
(3,'bane',172,310),
(4,'bloodseeker',127,261),
(5,'crystal maiden',71,147);

INSERT INTO player (player_id,rank_tier,win,lose,mmr_estimate) 
VALUES (19813,65.0,3068,3024,3686.0),
(24937,55.0,1102,1084,3565.0),
(26952,80.0,3932,3792,5294.0),
(30208,65.0,3318,3204,4636.0),
(40380,75.0,4830,4551,4014.0),
(42072,80.0,2020,2083,4096.0),
(43407,75.0,5186,4834,4617.0);"
```

Note:

- -c = run command in database session, command is given in string
- -t = skip header and footer
- -q = silent mode for grep 
- || = logical OR, if grep fails to find match run the subsequent command

## Deploy Django

At root folder, run:

```console
cd kubernetes/
```

Apply the files following:

- django/deployments.yaml
- django/service.yaml

with syntax: `kubectl apply -f <filename.yaml>`

```kubectl exec -it <pod-postgres-name> -- bin/bash```

Run django servirce:

```console
minikube service django-service
```
Enjoy!!!

## More Commands

To list your deployments use the get deployments command:

```
kubectl get deployments
```


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

Reference:
https://docs.docker.com/samples/django/
https://dockertraining.readthedocs.io/en/latest/django/