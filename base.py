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
    if os.system("sudo chmod +x apache.py && ./apache.py") == 0:
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
                if configurar_apache():
                    if configurar_php():
                        if migracion():
                            print("Migración completa")