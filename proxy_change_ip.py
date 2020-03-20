#!/usr/bin/python3

from configparser import ConfigParser
import os

config = ConfigParser()
config.read('MIGdrupal.conf')

os.system("sudo sed -i 's/https:\/\/*.*.*.*/https:\/\/" + config['Proxy']['ip1'] + "\//g' /etc/apache2/sites-available/proxy.conf")
os.system("sudo sed -i '0,/https:\/\/*.*.*.*/! s/https:\/\/*.*.*.*/https:\/\/" + config['Proxy']['ip2'] + "\//' /etc/apache2/sites-available/proxy.conf")