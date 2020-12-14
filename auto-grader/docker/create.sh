#!/bin/bash
sudo docker pull selenium/hub
sudo docker pull selenium/node-chrome

sudo docker run -p -d --name hub selenium/hub
sudo docker run -d --link selenium-hub:hub selenium/node-chrome

python3 sampletest.py
docker logs hub

sudo docker stop node
sudo docker rm node
sudo docker image rm  grade:v1


