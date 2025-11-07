---
title: Cheat Sheet
---

______________________________________________________________________

## Clean up Docker

______________________________________________________________________

Delete all containers

`docker rm -f $(sudo docker ps -a -q)`

Delete all volumes

`docker volume rm $(sudo docker volume ls -q)`

Delete all networks

`docker network rm $(sudo docker network ls -q)`

Delete all unused images

`docker system prune -a`

## Working with Docker

______________________________________________________________________

Start and attach bash in running container

`docker exec -u user -it container-name /bin/bash/`

Info about Docker and the config

`docker info`

Which containers are currently running

`docker ps`

Start container

`docker run imagename`

Forwards port "internal" of the container to port "external" of the host

`docker run -p port-internal:port-external`

Link the new container with the container "container_name"

`docker run --link container_name:network_alias`

View Docker stdout/stderr from detached container

`docker logs -f container-name`

Enter running, detached container

`docker container attach`

To learn more about a session

`docker inspect`

Restart/stop existing container

`docker start|stop`

Fetches an image from the online registry

`docker pull`

Pauses the container

`docker pause`

Resumes the container after pause

`docker unpause`

Compares the container with that of the last image

`docker diff`

Updates the image from the container

`docker commit`
