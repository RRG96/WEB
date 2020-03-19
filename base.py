#!/usr/bin/python3

from configparser import ConfigParser
import os

config = ConfigParser()
config.read('MIGdrupal.conf')

def validacion():
    print("\nSe han configurado los siguientes valores para la migración:\n")
    with open ("MIGdrupal.conf", "r") as file:
        print(file.read())
    opcion = input("\n¿Iniciar migración?\n(Si) -> S\n(No) -> Cualquier tecla\n\nIngresa una opción: ")
    if (opcion.upper() == 'S'):
        return True
    else:
        print("Migración cancelada")

def instalar_componente(componente):
    print("Instalando " + componente + "...")
    if os.system("sudo chmod +x " + componente + ".sh && sudo ./" + componente + ".sh") == 0:
        return True
    else:
        print("Error en la instalación de " + componente)
        exit()

def configurar_apache():
    cadena = (config['Apache']['sitio']).split('.')
    cert = (config['SSH']['certPath']).split('/')
    key = (config['SSH']['keyPath']).split('/')
    if os.system("sudo chmod 777 /var/www/ && cd /var/www/ && drush dl drupal-8 && sudo mv drupal-8.8.4 " + cadena[0] + " && sudo chmod 755 /var/www/ && sudo cp \
     /etc/apache2/sites-available/default-ssl.conf /etc/apache2/sites-available/" + cadena[0]  + ".conf") == 0:
        os.system("sudo sshpass -p " + config['SSH']['password'] + " scp " + config['SSH']['user'] + "@" + config['SSH']['ip'] + ":" + config['SSH']['certPath'] + " /etc/ssl/certs/" + cert[len(cert)-1])
        #os.system("sudo chmod 777 /etc/ssl/private/")
        os.system("sudo sshpass -p " + config['SSH']['password'] + " ssh -t " + config['SSH']['user'] + "@" + config['SSH']['ip'] + " \"echo " + config['SSH']['password'] + " | sudo -S chmod 777 " + config['SSH']['keyPath'] + "\"")
        os.system("sudo sshpass -p " + config['SSH']['password'] + " scp " + config['SSH']['user'] + "@" + config['SSH']['ip'] + ":" + config['SSH']['keyPath'] + " /etc/ssl/private/" + key[len(key)-1])
        #os.system("sudo chmod 710 /etc/ssl/private/")
        os.system("sudo sshpass -p " + config['SSH']['password'] + " ssh -t " + config['SSH']['user'] + "@" + config['SSH']['ip'] + " \"echo " + config['SSH']['password'] + " | sudo -S chmod 710 " + config['SSH']['keyPath'] + "\"")
        os.system("sudo sed -i 's/DocumentRoot \/var\/www\/html/DocumentRoot \/var\/www\/" + cadena[0] + "\//g' /etc/apache2/sites-available/" + cadena[0]  + ".conf")
        os.system("sudo sed -i 's/\/etc\/ssl\/certs\/ssl-cert-snakeoil.pem/\/etc\/ssl\/certs\/" + cert[len(cert)-1] + "/g' /etc/apache2/sites-available/" + cadena[0]  + ".conf")
        os.system("sudo sed -i 's/SSLCertificateKeyFile \/etc\/ssl\/private\/ssl-cert-snakeoil.key/SSLCertificateKeyFile \/etc\/ssl\/certs\/" + key[len(key)-1] + "/g' /etc/apache2/sites-available/" + cadena[0]  + ".conf")
        os.system("sudo sed -i '5 a ServerName " + config['Apache']['sitio'] + "' /etc/apache2/sites-available/" + cadena[0]  + ".conf")
        os.system("sudo sed -i '5 a ServerAlias www." + config['Apache']['sitio'] + "' /etc/apache2/sites-available/" + cadena[0]  + ".conf")
        os.system("sudo sed -i '1 a " + config['Apache']['ip'] + " " + config['Apache']['sitio'] + "' /etc/hosts")
        os.system("sudo a2ensite " + cadena[0]  + ".conf")
        os.system("sudo systemctl restart apache2")
        print("Drupal instalado y configurado correctamente")
        return True
    else:
        print("Error en la configuración de apache")
        exit()
        
def configurar_php():
    if os.system("sudo chmod +x php.sh && sudo ./php.sh " + config['PHP']['dir'] + " " + config['PHP']['allow'] + " " + config['PHP']['session']) == 0:
        return True
    else:
        print("Error en la configuración de PHP")
        exit()

def migracion():
    if os.system("sudo chmod +x migracion.sh && sudo ./migracion.sh " + config['PostgreSQL']['database'] + " " + config['PostgrSQL']['user'] + " " + config['PostgreSQL']['password'] + " " + config['PostgreSQL']['host'] + " " + config['PostgreSQL']['port']) == 0:
        return True
    else:
        print("La migración no se logró")
        os.system('drush migrate-rollback --all --feedback="60 seconds"')
        exit()
        

if __name__ == '__main__':
    os.system("clear")
    print("Bienvenido a la herramienta de migración de drupal (Versión 7.x a 8.x)")
    if (validacion()):
        if instalar_componente("dependencias"):
            if instalar_componente("drush"):
<<<<<<< HEAD
                if configurar_apache():
                    print("Migración completa")
=======
                if instalar_componente("drupal"):
                    if configurar_apache():
                        if configurar_php():
                            if migracion():
                                print("Migración completa")
>>>>>>> 08a44d07140282f6f6f4e9a66ad198ddebff37d2
