---
layout: default
title: Cheat Sheet
parent: Docker
---

# {{ page.title }}

______________________________________________________________________

## Docker Aufräumen

______________________________________________________________________

Alle Container löschen

`docker rm -f $(sudo docker ps -a -q)`

Alle Volumen löschen

`docker volume rm $(sudo docker volume ls -q)`

Alle Netzwerke löschen

`docker network rm $(sudo docker network ls -q)`

Alle ungenutzten Images löschen

`docker system prune -a`

## Arbeiten mit Docker

______________________________________________________________________

Bash in laufendem Container starten und anhängen

`docker exec -u user -it container-name /bin/bash/`

Infos über Docker und die Konfig / Module

`docker info`

Welche Container laufen gerade

`docker ps`

Container starten

`docker run Image-Name`

Leitet Port "intern" des Containers auf den Port "extern" des Hosts

`docker run -p port-intern:port-extern`

Linked den neuen Container mit dem Container "container_name" - Intern ist dieser über den Hostname "network_alias" erreichbar

`docker run --link container_name:network_alias`

Docker stdout/stderr von detached container ansehen

`docker logs -f container-name`

Laufenden, detached Container betreten

`docker container attach`

Um mehr über eine Sitzung zu erfahren

`docker inspect`

Vorhandenen Container erneut starten/stoppen

`docker start|stop`

holt ein image aus der online registry

`docker pull`

Pausiert den Container

`docker pause`

setzt den Container nach pause fort

`docker unpause`

vergleicht den Container mit der des letzten Images

`docker diff`

Updated das Image aus dem Container

`docker commit`
