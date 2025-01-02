# What is Docker?
- Software applications that are inside a container. Create an abstract layber of automation on the OS-level
# What is a container?
- Containers operate a lot like Virtual Machines, but in a slightly different way. VM's isolate the entire hosts operating system while containers are logical packages so they are stand alone packages/applications.
# Quick Getting Started:
- Docker instalation
    - https://docs.docker.com/docker-for-windows/install
- Docker Registry
    - Here is where you can find images you can build upon
    - https://hub.docker.com/
- Hands on example:
    - Confirm Docker is working 
        - ```Docker Version ```
    - Install test image
        - ```docker pull busybox```
    - The image will be installed on your local machines
        - ```docker run busybox echo "hello from busybox"```
    - To see all of your containers and images
        - ```docker ps -a```
    - To remove a container/image
        - ```docker rm {container ID}```
        - ``` docker rmi {image id}```


# Commands
List local images:
```docker images```<br>
Pull an image from Docker hub:
```docker pull <image_name>``` <br>
List all running containers:
```docker ps```<br>
Logs for the container:
```docker logs -f <container_name>```

### Docker Training:
- https://docker-curriculum.com/
- https://docs.docker.com/get-started/docker_cheatsheet.pdf