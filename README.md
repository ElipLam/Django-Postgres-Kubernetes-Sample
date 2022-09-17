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


Reference:

https://docs.docker.com/samples/django/
https://dockertraining.readthedocs.io/en/latest/django/