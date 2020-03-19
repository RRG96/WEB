#!/usr/bin/bash

set -e
drush en migrate_tools -y
drush en migrate_upgrade -y
echo -n "\$databases['upgrade']['default'] = array (\n
'database' => '$1',\n
'username' => '$2',\n
'password' => '$3',\n
'prefix' => '',\n
'host' => '$4',\n
'port' => '$5',\n
'namespace' => 'Drupal\\Core\\Database\\Driver\pgsql',\n
'driver' => 'pgsql'\n
);" >> settings.php
echo -n "\$databases['migrate']['default'] = array (\n
'database' => '$1',\n
'username' => '$2',\n
'password' => '$3',\n
'prefix' => '',\n
'host' => '$4',\n
'port' => '$5',\n
'namespace' => 'Drupal\\Core\\Database\\Driver\pgsql',\n
'driver' => 'pgsql'\n
);" >> settings.php
drush migrate-upgrade --legacy-db-url=pgsql://$2@$4/$1 --legacy-$2=/Direccion de instalacion --configure-only
drush migrate-status
drush migrate-import --all --feedback="60 seconds"
echo "Es posible que se encuentren errores extra"