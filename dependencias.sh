#!bin/bash
apt install -y php7.3
apt install -y curl
apt install apache2
apt install -y postgresql-client-11
curl -sS https://getcomposer.org/installer | php --install-dir=/usr/local/bin/composer
ssh $1@$3 apt install -y postgresql-11 postgresql-client-11
