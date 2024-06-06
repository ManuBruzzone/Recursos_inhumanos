from empleados import *
from funciones import *


def mostrar_menu():
    opcion = input('---MENU---\n1. Ingresar empleado\n2. Modificar empleado\n3. Eliminar empleado\n4. Mostrar todos\n5. Calcular salario promedio\n6. Buscar empleado por DNI\n7. Ordenar empleados\n8. Generar reporte en base al sueldo.\n9. Generar reporte en base al apellido\n10. Salir\nElija una opcion: ')
    return opcion

path_empleados = './Empleados.csv'
path_bajas = './Bajas.json'
path_nro_reportes = './nro_reportes.txt'
path_nro_id = './nro_id.txt'
lista_empleados = cargar_lista(path_empleados)


system('cls')
#bandera_ingreso = False
while True:
    opcion = mostrar_menu()
    match opcion:
        case '1':
            system('cls')

            id = crear_id(path_nro_id, lista_empleados)
            ingresar_empleado_lista(lista_empleados, id)

            #bandera_ingreso = True
        case '2':
            #if bandera_ingreso == True:
                system('cls')

                id = int(input('Ingrese el ID del empleado: '))
                modificar_empleado(lista_empleados, id)

        case '3':
            #if bandera_ingreso == True:
                system('cls')

                id = int(input('Ingrese el dni del empleado: '))
                empleado_eliminado = eliminar_empleado(lista_empleados, id, path_bajas)
            

        case '4':
            #if bandera_ingreso == True:
                system('cls')

                print(f'{'*'*62}\n| {'Nombre':>12} | {'Apellido':>12} | {'Puesto':>12} |  {'Salario':>12} |\n{'-'*62}')
                mostrar_todos_los_empleados(lista_empleados)
                print(f'{'*'*62}')

        case '5':
            #if bandera_ingreso == True:
                system('cls')

                calcular_salario_promedio(lista_empleados)
                
        case '6':
            #if bandera_ingreso == True:
                system('cls')

                dni = int(input('Ingrese el DNI del empledo: '))

                print(f'{'*'*61}\n| {'Nombre':>12} | {'Apellido':>12} | {'Puesto':>12} | {'Salario':>12} |\n{'-'*61}')
                buscar_empleado(lista_empleados, dni)
                print(f'{'*'*61}')

        case '7':
            #if bandera_ingreso == True:
                system('cls')
                
                ordenar_lista_empleados(lista_empleados)
                
        case '8':
            #if bandera_ingreso == True:
                system('cls')
                

                reporte_sueldo(lista_empleados, path_nro_reportes)
    

        case '9':
            #if bandera_ingreso == True:
            pass
        

        case '10':
            actualizar_lista(path_empleados,lista_empleados)
            
            break

    system('pause')
    system('cls')