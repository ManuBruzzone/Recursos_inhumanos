import re
import json
from empleados import *
import datetime

def cargar_lista(path):
    lista = []

    with open(path, 'r') as archivo:
        archivo.readline()

        for line in archivo:
            lectura = re.split(',|\n', line)
            empleado = {}
            empleado['id'] = lectura[0]
            empleado['id'] = int(empleado['id'])
            empleado['nombre'] = lectura[1]
            empleado['apellido'] = lectura[2]
            empleado['DNI'] = lectura[3]
            empleado['DNI'] = int(empleado['DNI'])
            empleado['puesto'] = lectura[4]
            empleado['salario'] = lectura[5]
            empleado['salario'] = int(empleado['salario'])
            lista.append(empleado)

    return lista


def actualizar_lista(path,  lista):
    with open(path, 'w') as archivo:
        cabecera = 'id,nombre,apellido,DNI,puesto,salario'  
        archivo.write(f'{cabecera}\n')
        for empleado in lista:
            escribir = ','.join([str(empleado['id']), empleado['nombre'], empleado['apellido'], str(empleado['DNI']), empleado['puesto'], str(empleado['salario'])])
            archivo.write(f'{escribir}\n')


def cargar_baja(path, diccionario):
    with open(path, 'w') as archivo:
            json.dump(diccionario, archivo, indent = 4)

def leer_archivo_json(path):
    diccionario = []
    try:
        with open(path, 'r') as archivo:
            diccionario = json.load(archivo)
    except:
        print('fallo bro :v')
    
    return diccionario

def generar_reporte(lista, path):
    nro_reporte = generar_nro_reporte(path)
    fecha_solicitud = datetime.datetime.now().strftime("%Y-%m-%d")
    cantidad_empleados = len(lista)

    with open(f'./reporte_{nro_reporte}.txt', 'w') as archivo:
        archivo.write(f'Reporte Nro: {nro_reporte}\n')
        archivo.write(f'Fecha: {fecha_solicitud}\n')
        archivo.write(f'Cantidad coincidencias: {cantidad_empleados}\n')
        archivo.write(f'{"ID":<5}{"Apellido y Nombre":<30}{"Sueldo":<12}{"Puesto":<12}\n')
        for empleado in lista:
            archivo.write(f"{empleado['id']:<5}{empleado['apellido']}, {empleado['nombre']:<30}{empleado['salario']:<12}{empleado['puesto']:<12}\n")


def generar_nro_reporte(path):
    try:
       with open(path, 'r+') as archivo:
            contenido = archivo.read()
            numero_reporte = int(contenido)
            archivo.seek(0)  
            archivo.write(str(numero_reporte + 1))

    except:
        print('Se generará el primer reporte.')
        numero_reporte = 1
        with open(path, 'w') as archivo:
            archivo.write('1')

    return numero_reporte