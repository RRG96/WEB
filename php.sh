#!/usr/bin/bash

set -e
if [[ $(cat /etc/php/7.3/cli/php.ini | grep ".*php_expose.*") ]]; then sed -i "s/.*expose_php.*/expose_php = Off/" /etc/php/7.3/cli/php.ini; else echo "php_expose = Off" >> /etc/php/7.3/cli/php.ini; fi
if [[ $(cat /etc/php/7.3/cli/php.ini | grep ".*display_errors.*") ]]; then sed -i "s/.*display_errors.*/display_errors = Off/" /etc/php/7.3/cli/php.ini; else echo "display_errors = off" >> /etc/php/7.3/cli/php.ini; fi
if [[ $(cat /etc/php/7.3/cli/php.ini | grep ".*disable_functions.*") ]]; then sed -i "s/.*disable_functions.*/.*disable_functions = system, exec, php_uname/" /etc/php/7.3/cli/php.ini; else echo "disable_functions = system, exec, php_uname" >> /etc/php/7.3/cli/php.ini; fi
if [[ $(cat /etc/php/7.3/cli/php.ini | grep ".*file_uploads.*") ]]; then sed -i "s/.*file_uploads.*/file_uploads = Off/" /etc/php/7.3/cli/php.ini; else echo "files_uploads = Off" >> /etc/php/7.3/cli/php.ini; fi
if [[ $(cat /etc/php/7.3/cli/php.ini | grep ".*php_expose.*") ]]; then sed -i "s/.*expose_php.*/expose_php Off/" /etc/php/7.3/cli/php.ini; else echo "php_expose Off" >> /etc/php/7.3/cli/php.ini; fi
#if [[ $(cat /etc/php/7.3/cli/php.ini | grep ".*open_basedir.*") ]]; then sed -i "s/.*open_basedir.*/open_basedir = $2/" /etc/php/7.3/cli/php.ini; else echo "open_basedir = $2" >> /etc/php/7.3/cli/php.ini; fi
#if [[ $(cat /etc/php/7.3/cli/php.ini | grep ".*session\.name.*") ]]; then sed -i "s/.*session\.name.*/session\.name = $3/" /etc/php/7.3/cli/php.ini; else echo "session.name = $3" >> /etc/php/7.3/cli/php.ini; fi
#if [[ $(cat /etc/php/7.3/cli/php.ini | grep ".*$1.*") ]]; then sed -i "s/.*$1.*/$1/" /etc/php/7.3/cli/php.ini; else echo "$1" >> /etc/php/7.3/cli/php.ini; fi
echo "PHP configurado satisfactoriamente"