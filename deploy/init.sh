#!/bin/bash
echo "====================Start====================="
sudo apt-get update -y
sudo apt install docker.io  -y
sudo apt install docker-compose  -y
sudo mkdir /app && cd /app
sudo git clone https://github.com/yaroschak/project.git && cd project
sudo docker-compose up -d
echo "====================End====================="