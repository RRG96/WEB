#!/usr/bin/python3

import argparse
import os

def parse():
    parser = argparse.ArgumentParser(   prog = 'MIGdrupal', description = 'Programa que permite la migración de drupal (Versión 7.x a 8.x)')
    parser.add_argument('-i', '--postgres-direcccion', action='store', required = True, type = str, help = 'Dirección ip de la base de datos postgres', metavar= 'postgres-ip', dest='ip')
    parser.add_argument('-u', '--postgres-user', action='store', required = True, type = str, help = 'Usuario de la base de datos postgres', metavar= 'postgres-user', dest='user')
    parser.add_argument('-p', '--postgres-password', action='store', required = True, type = str, help = 'Contraseña de la base de datos postgres', metavar= 'postgres-password', dest='password')
    parser.add_argument('-d', '--postgres-database', action='store', required = True, type = str, help = 'Nombre de la base de datos de postgres', metavar= 'potgres-database', dest='database')
    return parser.parse_args()

def validacion():
    print("La base de datos para drupal se creará con los siguientes argumentos:\nUsuario: {0}\nContraseña: {1}\nDatabase: {2}\nIP: {3}".format(args.user, args.password, args.database, args.ip))
    opcion = input('¿Iniciar migración?\n(Si) -> S\n(No) -> Cualquier tecla\nIngresa una opción: ')
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
    args = parse()
    print("Bienvenido a la herramienta de migración de drupal (Versión 7.x a 8.x)")
    if (validacion()):
        if instalar_componente("dependencias"):
            if instalar_componente("drush"):
                print("Migración completa")