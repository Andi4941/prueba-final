import random
import csv
import math


empleados = ["Juan Pérez", "Maria Garcia", "Carlos López", "Ana Martínez", "Pedro Rodriguez",
             "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

sueldos = {}


def asignar_sueldos():
    global sueldos
    sueldos = {empleado: random.randint(300000, 2500000) for empleado in empleados}
    print("Sueldos asignados.")


def clasificar_sueldos():
    menores_800 = {k: v for k, v in sueldos.items() if v < 800000}
    entre_800_2000 = {k: v for k, v in sueldos.items() if 800000 <= v <= 2000000}
    superiores_2000 = {k: v for k, v in sueldos.items() if v > 2000000}
    print("\nClasificación de sueldos:")
    print("Menores a $800,000:", menores_800)
    print("Entre $800,000 y $2,000,000:", entre_800_2000)
    print("Superiores a $2,000,000:", superiores_2000)


def ver_estadisticas():
    if not sueldos:
        print("Primero asigne los sueldos.")
        return
    valores = list(sueldos.values())
    print("\nEstadísticas:")
    print(f"Sueldo más alto: ${max(valores)}")
    print(f"Sueldo más bajo: ${min(valores)}")
    print(f"Promedio de sueldos: ${sum(valores) / len(valores)}")
    print(f"Media geométrica de sueldos: ${math.exp(sum(math.log(x) for x in valores) / len(valores))}")


def generar_reporte():
    if not sueldos:
        print("Primero asigne los sueldos.")
        return
    with open("reporte_sueldos.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])
        for empleado, sueldo in sueldos.items():
            descuento_salud = sueldo * 0.07
            descuento_afp = sueldo * 0.12
            sueldo_liquido = sueldo - descuento_salud - descuento_afp
            writer.writerow([empleado, sueldo, descuento_salud, descuento_afp, sueldo_liquido])
    print("\nReporte exportado a 'reporte_sueldos.csv'")


def mostrar_menu():
    print("\nMenu:")
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadísticas")
    print("4. Reporte de sueldos")
    print("5. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            asignar_sueldos()
        elif opcion == "2":
            clasificar_sueldos()
        elif opcion == "3":
            ver_estadisticas()
        elif opcion == "4":
            generar_reporte()
        elif opcion == "5":
            print("Finalizando programa...")
            print("Desarrollado por [andi nuñez]")
            print("RUT [20292939-7]")
            break
        else:
            print("Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    main()

