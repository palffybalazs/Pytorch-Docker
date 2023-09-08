# Pytorch Docker
This repository provides a dockerized pythorch environment with cuda support for neural network training.



## Install

### Install docker
https://docs.docker.com/engine/install/ubuntu/

#### Run post-installation steps
https://docs.docker.com/engine/install/linux-postinstall/

You should be able to run `docker run hello-world` without using sudo. If sudo is still required, run `sudo newgrp docker` and restart your computer.

### Install Nvidia drivers
Install Nvidia Driver Version: 525.125.06 or higher.
### Install Nvidia container toolkit
https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#docker

## Compile container

`./compile.sh`

## Run _livox_ros_ container

Run the container: `./run.sh`
In case of an error like this:
`docker: Error response from daemon: Unknown runtime specified nvidia.`

Run the following commands

```
sudo apt install -y nvidia-docker2
sudo systemctl daemon-reload
sudo systemctl restart docker
```

In VSCode install Dev Container and Docker


The repository `/data` folder is not synced to github, but it is attached to the container at `/home/appuser/data`, the same goes with src.

## Test the docker
Navigate to src folder and run the provided python script.
`python test-gpu.py`
The result should look similar to this:
```
Is GPU available:  True
Number of GPU:  1
Device number:  0
Cuda device:  <torch.cuda.device object at 0x7f83317c9820>
Name of the GPU:  NVIDIA GeForce GTX 1080
```
Let's go!
