from os import system
from Package_Input.Input import *
from archivos import *

# Create
def crear_id(path, lista):
    try:
       with open(path, 'r+') as archivo:
            contenido = archivo.read()
            numero_id = int(contenido)
            archivo.seek(0)  
            archivo.write(str(numero_id + 1))

    except:
        print('Se genero el archivo id.')
        numero_id = len(lista) + 1
        with open(path, 'w') as archivo:
            archivo.write(str(len(lista) + 1))

    return numero_id

def crear_empleado(id, nombre: str, apellido: str, dni: int, puesto: str, salario: int):
    diccionario_empleado = {
        'id': id,
        'DNI' : dni,
        'nombre' : nombre,
        'apellido' : apellido,
        'puesto' : puesto,
        'salario': salario
    }

    return diccionario_empleado

def ingresar_empleado_lista(lista_empleados: list,id: int): #retorne si pudo o no
    dni = get_int('Ingrese su DNI: ','Re-Ingrese su DNI: ', 5000000, 99999999, 3)
    nombre = get_string('Ingrese su nombre: ','Re-Ingrese su nombre: ',1, 20, 3)
    apellido = get_string('Ingrese su apellido: ','Re-Ingrese su apellido: ',1, 20, 3)
    puesto = get_string_puesto('Ingrese su puesto:\n“Gerente”\n“Supervisor"\n“Analista”\n“Encargado”\n“Asistente”\nAqui su respuesta: ','Re-Ingrese su puesto: ',3, 20, 3)
    salario = get_int('Ingrese su sueldo: ','Re-Ingrese su sueldo: ', 234315, 99999999, 3)

    diccionario_empleado = crear_empleado(id, nombre, apellido, dni, puesto, salario)

    lista_empleados.append(diccionario_empleado)


# Read
def mostrar_un_empleado(un_empleado: dict):
    print(f'| {un_empleado['nombre']:>12} | {un_empleado['apellido']:>12} | {un_empleado['puesto']:>12} | ${un_empleado['salario']:>12} |')

def mostrar_todos_los_empleados(lista_empleados: list[dict]):
    for empleado in lista_empleados:
        mostrar_un_empleado(empleado)

# Update
def modificar_empleado(lista_empleados: list[dict], id: int): #retorne si pudo o no
    for empleado in lista_empleados:
        if id == empleado['id']:
            bandera_seguir = True
            while bandera_seguir == True:
                opcion = input('Elija la opcion a modificar\n1. nombre\n2. apellido\n3. dni\n4. puesto\n5. salario\n6. cancelar\nAqui su respuesta: ')
                match opcion:
                    case '1':
                        nuevo_nombre = input('Ingrese el nuevo nombre: ')
                        empleado['nombre'] = nuevo_nombre
                    case '2':
                        nuevo_apellido = input('Ingrese el nuevo apellido: ')
                        empleado['apellido'] = nuevo_apellido
                    case '3':
                        nuevo_dni = int(input('Ingrese el nuevo dni: '))
                        empleado['DNI'] = nuevo_dni
                    case '4':
                        nuevo_puesto = input('Ingrese el nuevo puesto: ')
                        empleado['puesto'] = nuevo_puesto
                    case '5':
                        nuevo_salario = int(input('Ingrese el nuevo salario: '))
                        empleado['salario'] = nuevo_salario
                    case '6':
                        bandera_seguir = False
                        print('Operacion cancelada!')
                        break
                
                continuar = input(f'Desea seguir modificando la informacion del empleado con id {empleado['id']}? (si/no)\nSu respuesta: ')
                if continuar == 'no':
                    break

#Delete
def eliminar_empleado(lista_empleados: list[dict], id: int, path):
    eliminado = None
    for empleado in lista_empleados:
        if id == empleado['id']:
            eliminado = empleado
            diccionario = leer_archivo_json(path)
            diccionario.append(eliminado)
            cargar_baja(path, diccionario)
            break

    if eliminado != None:
        lista_empleados.remove(eliminado)