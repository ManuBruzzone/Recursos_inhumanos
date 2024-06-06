from archivos import *

def calcular_salario_promedio(lista_empleados: list[dict]):
    salario_total = 0
    cantidad_empleados = len(lista_empleados)
    for empleado in lista_empleados:
        salario_total += empleado['salario']

    salario_promedio = salario_total / cantidad_empleados

    print(f'El sueldo promedio de los {cantidad_empleados} empleados actuales es de ${salario_promedio}.')

    
def buscar_empleado(lista_empleados: list[dict], dni:int):
        for empleado in lista_empleados:
            if dni == empleado['DNI']:
                mostrar_un_empleado(empleado)


def ordenar_lista_empleados(lista_empleados: list[dict]):
    bandera_seguir = True
    while bandera_seguir == True:
        system('cls')

        opcion = input('Ordene la lista a su gusto!\nOrdenar por:\n1. nombre\n2. apellido\n3. salario\n4. salir\nAqui su respuesta: ')
        match opcion:
            case '1':
                system('cls')
                variable = 'nombre'

            case '2':
                system('cls')
                variable = 'apellido'

            case '3':
                system('cls')
                variable = 'salario'

            case '4':
                bandera_seguir = False
                break

        opcion = input('Ordene la lista a su gusto!\n1. Ordenar de manera ascendente\n2. Ordenar de manera descendente\n3. atras\nAqui su respuesta: ')       
        system('cls')
        match opcion:
            case '1':
                system('cls')
                ordenamiento = 'ascendente'

            case '2':
                system('cls')
                ordenamiento = 'descendente'

            case '3':
                break
    
        mecanismo_ordenar_lista(lista_empleados, variable, ordenamiento)
        
def mecanismo_ordenar_lista(lista_empleados: list[dict], variable, ordenamiento):
    
    if ordenamiento == 'ascendente':
        lista_empleados.sort(key=lambda x: x[variable])

    else:
        lista_empleados.sort(key=lambda x: x[variable], reverse=True)


def reporte_sueldo(lista: list[dict], path):
    sueldo = int(input('Ingrese un sueldo: '))
    lista_empleados_mayor_sueldo = []
    for empleado in lista:
        if sueldo < empleado['salario']:
            lista_empleados_mayor_sueldo.append(empleado)

    generar_reporte(lista_empleados_mayor_sueldo, path)      