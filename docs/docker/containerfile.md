---
layout: default
title: Containerfile
parent: Docker
---

# {{ page.title }}

______________________________________________________________________

{: .note }

> Containerfiles sind Bauanleitungen für Container Images, welche die ausgeführte Software darstellen.

______________________________________________________________________

Die folgenden Anweisungen stehen in Dockerfiles zur Verfügung:

| Anweisung  | Funktion                                                                                                                                                                            |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| FROM       | Definiert das Base Image welches verwendet wird.                                                                                                                                    |
| ADD        | Kopiert Dateien in das Image.                                                                                                                                                       |
| ARG        | Temporäre ENV-Variable aus Build Context.                                                                                                                                           |
| CMD        | Führt ein Befehl im Container beim run aus, sofern NICHTS an Argumenten übergeben wurde. kann in "exec" oder "shell" Form angegeben werden (Shell form akzeptiert keine Parameter!) |
| ENTRYPOINT | Wie CMD, wird aber immer ausgeführt sobald der Container gestartet wird. kann in "exec" oder "shell" Form angegeben werden (Shell form akzeptiert keine Parameter!)                 |
| ENV        | Setzt eine Environment Variable. Kann im Dockerfile als auch im Container genutzt werden.                                                                                           |
| EXPOSE     | Deklariert Ports für den Containerzugriff                                                                                                                                           |
| USER       | Ab der Angabe USER werden alle folgenden Commands (CMD, ENTRYPOINT etc.) im Container als USER ausgeführt                                                                           |

## Beispiel

______________________________________________________________________

```Dockerfile
FROM ubuntu:latest

MAINTAINER Name "[mailto:maintainer@example.com]"

RUN apt-get update apt-get install -y python python-pip wget; apt clean
RUN pip install Flask
ADD hello.py /home/hello.py

WORKDIR /home
CMD ["echo","Welt"]
ENTRYPOINT ["echo", "Hallo"]
```
