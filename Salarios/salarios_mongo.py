"""Taller python"""
import json
import pymongo

URI = "mongodb://localhost:27017/"
CLIENTE = pymongo.MongoClient(URI)
BASEDATOS = CLIENTE["empleados"]
COLECCION = BASEDATOS["empleados"]
OPCION = ""


def ver_datos():
    """Funcion para visualizar todos los datos de la bd"""
    for value_x in COLECCION.find():
        print(value_x)


def construir_json(cedula_empleado, nombre_empleado, correo_empleado, cargo_empleado, valor_hora, horas_trabajadas):
    """Funcion para construir el json"""
    salario_empleado = int(valor_hora) * int(horas_trabajadas)
    result = '{ "cedula":"'+cedula_empleado+'", "nombre":"'+nombre_empleado+'", "correo":"'
    result = result+correo_empleado+'", "cargo":"'+cargo_empleado+'", "valorHora":'+valor_hora
    result = result+', "horasTrabajadas":'+horas_trabajadas+', "salario":'+str(salario_empleado)+'}'
    return result


while OPCION != "0":
    MENSAJE = "Ingresa 1 para agregar un empleado, 2 para actualizarlo, 3 para ver los datos de "
    MENSAJE = MENSAJE+"los empleados, 4 para eliminar un empleado o 0 para salir:"
    print(MENSAJE)
    OPCION = input()
    if OPCION == "1":
        print("Ingresa la cedula del empleado: ")
        CEDULA = input()
        print("Ingresa el nombre del empleado: ")
        NOMBRE = input()
        print("Ingresa el correo del empleado: ")
        CORREO = input()
        print("Ingresa el cargo del empleado: ")
        CARGO = input()
        print("Ingresa el valor de la hora del empleado: ")
        VALORHORA = input()
        print("Ingresa las horas trabajadas del empleado: ")
        HORASTRABAJADAS = input()

        JSONVARIABLE = construir_json(CEDULA, NOMBRE, CORREO, CARGO, VALORHORA, HORASTRABAJADAS)
        print(JSONVARIABLE)
        X = COLECCION.insert_one(json.loads(JSONVARIABLE))
        if X:
            print("Ingreso exitoso con id: ", X.inserted_id)
        else:
            print("Error al insertar el dato!")

    elif OPCION == "2":
        print("Ingresa la cedula del empleado: ")
        CC = input()
        for x in COLECCION.find({"cedula": CC}):
            print(x)
            myquery = x
        print("Ingresa el nuevo correo: ")
        CORREO = input()
        print("Ingresa el nuevo cargo: ")
        CARGO = input()
        print("Ingresa el nuevo valor de la hora: ")
        VALORHORA = input()
        print("Ingresa las horas trabajadas: ")
        HORASTRABAJADAS = input()

        NEWVALUESINPUT = {"$set": json.loads(construir_json(myquery['cedula'], myquery['nombre'], CORREO, CARGO, VALORHORA, HORASTRABAJADAS))}
        COUNTUPDATE = COLECCION.update_one(myquery, NEWVALUESINPUT)
        print('Los registros modificados en total fueron: '+str(COUNTUPDATE.modified_count))

    elif OPCION == "3":
        ver_datos()
    elif OPCION == "0":
        print("FINALIZADO!")
    else:
        print("Por favor ingresa un valor correcto")
