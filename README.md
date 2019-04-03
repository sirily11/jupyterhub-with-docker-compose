# jupyterhub-with-docker-compose
## Build the container
This is how you could set up jupyterhub with docker composer 

To build this docker container, simply run
```
docker-compose build
```

To run this docker container, simply run

```
docker-compose up
```

To run this container in background, run

```
docker-compose up -d

```
## Login the jupyterhub
Access http://0.0.0.0:5000, then use user name sirily11, and password 1234

## Change username and password
Go to build folder and change dockerfile
Change the following lines
```dockerfile
RUN useradd -ms /bin/bash  <Your username>
RUN echo <Your username>:<Your password> | chpasswd
```
Then re build the docker.
