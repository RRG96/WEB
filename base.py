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

if __name__ == '__main__':
    os.system("clear")
    print("Bienvenido a la herramienta de migración de drupal (Versión 7.x a 8.x)")
    if (validacion()):
        if instalar_componente("dependencias"):
            if instalar_componente("drush"):
                if instalar_componente("drupal"):
                    if instalar_componente("sitios"):
                        print("Migración completa")