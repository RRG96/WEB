#!/usr/bin/bash

set -e
cd /var/www/nuevosmagumbos/
drush dl migrate_tools -y
drush en migrate_tools -y
drush dl migrate_upgrade -y
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
);" >> /var/www/nuevosmagumbos/sites/default/settings.php
echo -n "\$databases['migrate']['default'] = array (\n
'database' => '$1',\n
'username' => '$2',\n
'password' => '$3',\n
'prefix' => '',\n
'host' => '$4',\n
'port' => '$5',\n
'namespace' => 'Drupal\\Core\\Database\\Driver\pgsql',\n
'driver' => 'pgsql'\n
);" >> /var/www/nuevosmagumbos/sites/default/settings.php
drush migrate-upgrade --legacy-db-url=pgsql://$6:$7@$8/$9 --legacy-root=/var/www/magumbos --configure-only
drush migrate-status
drush migrate-import --all --feedback="60 seconds"
echo "NOTA: Es posible que se encuentren errores extra"