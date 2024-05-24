from data_empleados import *
from random import randint, choice


def cargar_empleados_random(lista: list, cantidad: int):
    EDAD_MIN = 18
    EDAD_MAX = 65
    SUELDO_MIN = 20000
    SUELDO_MAX = 50000
    next_legajo = randint(20000, 30000 - cantidad)
    
    for _ in range(cantidad):
        
        legajo = next_legajo
        next_legajo += 1

        genero = choice(["f", "m"])

        match genero:
            case "f":
                nombre = choice(nombres_f)
            case "m":
                nombre = choice(nombres_m)

        apellido = choice(apellidos)

        edad = randint(EDAD_MIN, EDAD_MAX)

        calle = f"calle {randint(10, 90)} nro {randint(100, 999)}"

        localidad = choice(localidades)

        provincia = choice(provincias)

        email = f"{nombre}{apellido}{choice(dominios)}"

        sector = choice(sectores)

        sueldo = float(randint(SUELDO_MIN, SUELDO_MAX))

        lista.append(new_empleado(legajo, genero, nombre, apellido, edad, calle, localidad, provincia, email, sector, sueldo))


def new_empleado(legajo: int, genero: str,nombre: str, apellido: str, edad: int, calle: str, localidad: str, provincia: str, email: str, sector: str, sueldo: float) -> dict:

    empleado = {}

    empleado["legajo"] = legajo
    empleado["genero"] = genero
    empleado["nombre"] = nombre
    empleado["apellido"] = apellido
    empleado["edad"] = edad
    empleado["calle"] = calle
    empleado["localidad"] = localidad
    empleado["provincia"] = provincia
    empleado["email"] = email
    empleado["sector"] = sector
    empleado["sueldo"] = sueldo

    return empleado


def mostrar_empleados(empleados: list) -> None:
    print("                                          *********Lista de empleados**********")
    print(f"{"Legajo"} {"Genero"} {"Nombre":>10} {"Apellido":>10}  {"Edad"}       {"Calle":13} {"Localidad":10}  {"Provincia"} {"email":>22} {"Sector":>25} {"Sueldo":>15}")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------")

    for empleado in empleados:
        print(f"{empleado["legajo"]:<8} {empleado["genero"]:4} {empleado["nombre"]:>10} {empleado["apellido"]:>10} {empleado["edad"]:>4}   {empleado["calle"]:>}   {empleado["localidad"]:<11} {empleado["provincia"]:<15} {empleado["email"]:35} {empleado["sector"]:<15} {empleado["sueldo"]}")

empleados = []
cargar_empleados_random(empleados, 5)
mostrar_empleados(empleados)