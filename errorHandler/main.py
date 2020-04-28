#!/usr/bin/python3

from configparser import ConfigParser
import os

def verificarInstalaciones(dependencia):
    with open ("dependencias_instaladas.txt", "r") as instaladas:
        return True if dependencia in instaladas else False

def instalarComponente():
    with open ("dependencias.txt", "r") as dependencias:
        for dependencia in dependencias:
            if not verificarInstalaciones(dependencia):
                if os.system('sudo apt-get install -y ' + dependencia.replace('\n','')) == 0:
                    print(dependencia.replace('\n','') + ' instalado correctamente')
                    with open ("dependencias_instaladas.txt", "a") as instaladas:
                        instaladas.append(dependencia.replace('\n',''))
                else:
                    print('Error en la instalación de ' + dependencia.replace('\n',''))
            else:
                print(dependencia.replace('\n','') + ' ya se encuentra instalado')
instalarComponente()