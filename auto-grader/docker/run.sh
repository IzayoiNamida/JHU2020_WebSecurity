#!/bin/bash
sudo docker run -d -P --name selenium-hub selenium/hub
sudo docker run -d --link selenium-hub:hub selenium/node-chrome

python3 test.py
docker logs hub



