#!/usr/bin/python3

from configparser import ConfigParser
import os

def verificarInstalaciones(dependencia):
    with open ("errorHandler/dependencias_instaladas.txt", "r") as instaladas:
        return True if dependencia in instaladas else False

def instalarComponente(password):
    with open ("errorHandler/dependencias.txt", "r") as dependencias:
        for dependencia in dependencias:
            dependencia_stdout = dependencia.replace('\n','')
            if not verificarInstalaciones(dependencia):
                if os.system('set -e | echo ' + password + ' | sudo  -S apt-get install -y ' + dependencia_stdout) == 0:
                    print(dependencia_stdout + ' instalado correctamente')
                    with open ("errorHandler/dependencias_instaladas.txt", "a") as instaladas:
                        instaladas.write(dependencia_stdout + '\n')
                else:
                    print('Error en la instalación de ' + dependencia_stdout)
            else:
                print(dependencia_stdout + ' ya se encuentra instalado')