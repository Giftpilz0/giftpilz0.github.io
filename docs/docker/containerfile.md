---
layout: default
title: Containerfile
parent: Docker
---

# {{ page.title }}

______________________________________________________________________

{: .note }

> Container files are building instructions for container images that represent the running software.

______________________________________________________________________

The following directives are available in Dockerfiles:

| instruction | function                                                                                                                                                          |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| FROM        | Defines the base image that is used.                                                                                                                              |
| ADD         | Copies files into the image.                                                                                                                                      |
| ARG         | Temporary ENV variable from Build Context.                                                                                                                        |
| CMD         | Executes a command in the container at run if NOTHING is passed as arguments. can be specified in "exec" or "shell" form (Shell form does not accept parameters!) |
| ENTRY POINT | Like CMD, but always executed when the container is started. can be specified in "exec" or "shell" form (Shell form does not accept parameters!)                  |
| EPS         | Sets an environment variable. Can be used in the Dockerfile as well as in the container.                                                                          |
| EXPOSE      | Declares ports for container access                                                                                                                               |
| USER        | From the specification USER all following commands (CMD, ENTRYPOINT etc.) are executed in the container as USER                                                   |

## Example

______________________________________________________________________

```Dockerfile
FROM ubuntu:latest

MAINTAINER name "[mailto:maintainer@example.com]"

RUN apt-get update apt-get install -y python python-pip wget; apt clean
RUN pip install Flask
ADD hello.py /home/hello.py

WORKDIR /home
CMD ["echo","world"]
ENTRYPOINT ["echo", "hello"]
```
