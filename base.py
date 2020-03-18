import argparse
import os

def parse():

    parser = argparse.ArgumentParser(   prog = 'MIGdrupal',
                                        description = 'Programa que permite la migración de drupal 7 a drupal 8')

    parser.add_argument('-pd', '--postgres-direcccion', action='store', default='localhost', type=str, help='Dirección ip de la base de datos postgres', metavar= 'postgres-dir', dest='pd')
    parser.add_argument('-pu', '--postgres-user', action='store', default='Drupal', type=str, help='Usuario de la base de datos postgres', metavar= 'postgres-usr', dest='pu')
    parser.add_argument('-pp', '--postgres-password', action='store', default='Drupal', type=str, help='Contraseña de la base de datos postgres', metavar= 'postgres-psswd', dest='pp')
    parser.add_argument('-pn', '--postgres-name', action='store', default='DrupalDB', type=str, help='Nombre de la base de datos de postgres', metavar= 'potgres-nm', dest='pn')
    parser.add_argument('-su', '--ssh-user', action='store', required = True, type=str, help='Usuario de conexión a la máquina remota', metavar= 'SSH-USR', dest='su')
    return parser.parse_args()

def validacion():
    do
    {
        opcion = input('Desea Continuar?\nSi (S), No (N): ')
    }while(opcion == "S" or opcion == "N" or opcion == "s" or opcion == "n")
    if opcion == "S" or opcion == "s":
        True
    else:
        False

def instalar_dependencias(prs.su, prs.pd, prs.pu, prs.pp, prs.pn):
    print("Se descargaran dependencias necesarias para la migración")
    if validacion():
        os.system("chmod 777 ../*")
        os.system("sudo dependencias.sh" + prs.su + " " + prs.pd + " " + prs.pu + " " + prs.pp + " " + prs.pn)
    else:
        print("No se descargaron dependencias\nPueden ser necesarias para los procesos siguientes")

def instalar_drupal(prs.pd, prs.pu, prs.pp, prs.pn):
    print("Se instalará drush y drupal" + prs.pd + " " + prs.pu + " " + prs.pp + " " + prs.pn)
    if validacion():
        os.system("sudo drush.sh")
    else:
        print("No se instaló Drush ni Drupal\nPuede provocar problemas en el proceso futuro")
     
def configurar():
    print("Se configurará Apache y PHP")
    if validacion():
        os.system("sudo configuracion.sh")
    else:
        print("No se configuraron los servicios\nBrechas de seguridad inminentes")
        
def migracion():
    print("Se comienza la migración de drupal 7 a drupal 8")
    if validacion:
        os.system("sudo migracion.sh")   
    else:
        print("No se realizó la migración")

if __name__ == '__main__':
    prs = parse()
    print("La base de datos para drupal se creará con los siguientes parámetros default " + prs.pd + " " + prs.pu + " " + prs.pp + " " + prs.pn)
    if validacion():
        instalar_dependencias()
        configurar()
        instalar_drupal()
        migracion()
    else:
        print("Ingrese los valores al llamar al programa\nbase.py -pd algo -pu algo -pp algo -pn algo")
        
