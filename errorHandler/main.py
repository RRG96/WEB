#!/usr/bin/python3

from configparser import ConfigParser
import os

#Esta función verifica si existe el elemento en iteración del archivo dependencias.txt en el archivo dependencias_instaladas.txt
def verificarInstalaciones(dependencia):
    with open ("errorHandler/dependencias_instaladas.txt", "r") as instaladas:
        return True if dependencia in instaladas else False

#Esta función se encarga de verificar si ya se han instalado las dependencias especificadas en el archivo dependencias.txt
def instalarComponente(password):
    with open ("errorHandler/dependencias.txt", "r") as dependencias:
        for dependencia in dependencias:
            dependencia_stdout = dependencia.replace('\n','')
            #Si el elemento en iteración no existe en el archivo dependencias_instaladas.txt se instala
            #De lo contrario, notifica que ya se encuentra instalado
            if not verificarInstalaciones(dependencia):
                #Si no se presenta algún error en la instalación, el elemento se agrega al archivo dependencias_instaladas.txt
                #De lo contrario se notifica que hubo un error en la instalación
                if os.system('set -e | echo ' + password + ' | sudo  -S apt-get install -y ' + dependencia_stdout) == 0:
                    print(dependencia_stdout + ' instalado correctamente')
                    with open ("errorHandler/dependencias_instaladas.txt", "a") as instaladas:
                        instaladas.write(dependencia_stdout + '\n')
                else:
                    print('Error en la instalación de ' + dependencia_stdout)
            else:
                print(dependencia_stdout + ' ya se encuentra instalado')