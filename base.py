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
    parser.add_argument('-sp', '--ssh-password', action='store', required = True, type=str, help='Contraseña de conexión a la máquina remota', metavar= 'SSH-PSSWD', dest='sp')

    return parser.parse_args()

if __name__ == '__main__':
    prs = parse()
    print("La base de datos para drupal se creara con los siguientes parametros default " + prs.pd + " " + prs.pu + " " + prs.pp + " " + prs.pn)
    print("Desea continuar?")
    do
    {
        opcion = readline()
    }while(opcion == "S" or opcion == "N")
    if opcion == "S":
        print("Se descargaran dependencias necesarias para la migración")
        os.system("chmod 777 ../*")
        os.system("sudo dependencias.sh" + prs.su + " " + prs.sp + " " + prs.pd + " " + prs.pu + " " + prs.pp + " " + prs.pn)
        print("Se instalará drush y drupal" + prs.pd + " " + prs.pu + " " + prs.pp + " " + prs.pn)
        os.system("sudo drush.sh")
        print("Se comienza la migración")
        os.system("sudo migracion.sh")
    else:
        print("Ingrese los valores al llamar al programa\nbase.py -pd algo -pu algo -pp algo -pn algo")