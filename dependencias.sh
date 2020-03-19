#!/usr/bin/bash

set -e
sudo apt-get install -y php7.3
sudo apt-get install -y curl
sudo apt-get install apache2
sudo apt-get install postgresql-client -y
sudo apt-get install git -y
sudo apt-get install sshpass -y
sudo apt-get install -y build-essential
echo "Dependencias instaladas correctamente"