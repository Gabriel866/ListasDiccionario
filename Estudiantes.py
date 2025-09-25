import json

# Aqui se guardarán los estudiantes
ARCHIVO_JSON = "estudiantes.json"
ARCHIVO_TXT = "estudiantes.txt"

# Lista global
estudiantes = []

# --- Funciones de carga y guardado ---
def cargar_estudiantes():
    """Carga los estudiantes desde el archivo JSON si existe"""
    global estudiantes
    try:
        with open(ARCHIVO_JSON, "r", encoding="utf-8") as f:
            estudiantes = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        estudiantes = []  # Si el archivo no existe o está vacío

def guardar_estudiantes():
    """Guarda la lista completa en JSON y en TXT legible"""
    # Guardar en JSON
    with open(ARCHIVO_JSON, "w", encoding="utf-8") as f_json:
        json.dump(estudiantes, f_json, indent=4, ensure_ascii=False)
    
    # Guardar en TXT legible
    with open(ARCHIVO_TXT, "w", encoding="utf-8") as f_txt:
        for est in estudiantes:
            f_txt.write(f"Nombre: {est['nombre']}\n")
            f_txt.write(f"Edad: {est['edad']}\n")
            f_txt.write("Calificaciones:\n")
            for c in est["calificaciones"]:
                f_txt.write(f"   {c['materia']}: {c['nota']}\n")
            f_txt.write("-" * 30 + "\n")


# --- Funciones del programa ---
def agregar_estudiante():
    """Agrega un estudiante a la lista"""
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))

    calificaciones = []
    for i in range(4):
        materia = input(f"Ingrese el nombre de la materia {i+1}: ")
        nota = float(input(f"Ingrese la calificación de {materia}: "))
        calificaciones.append({"materia": materia, "nota": nota})

    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "calificaciones": calificaciones
    }
    estudiantes.append(estudiante)
    print(f"Estudiante {nombre} agregado.\n")


def eliminar_estudiante():
    """Elimina un estudiante por nombre"""
    nombre = input("Ingrese el nombre del estudiante a eliminar: ")
    for estudiante in estudiantes:
        if estudiante["nombre"].lower() == nombre.lower():
            estudiantes.remove(estudiante)
            print(f"Estudiante {nombre} eliminado.\n")
            return
    print(f"No se encontró al estudiante con nombre: {nombre}\n")


def promedio_estudiante():
    """Calcula el promedio de un estudiante por nombre"""
    nombre = input("Ingrese el nombre del estudiante: ")
    for estudiante in estudiantes:
        if estudiante["nombre"].lower() == nombre.lower():
            notas = [c["nota"] for c in estudiante["calificaciones"]]
            promedio = sum(notas) / len(notas)
            print(f"El promedio de {nombre} es: {promedio:.2f}\n")
            return
    print(f"No se encontró al estudiante con nombre: {nombre}\n")


def mostrar_estudiantes():
    """Muestra todos los estudiantes"""
    if not estudiantes:
        print("No hay estudiantes registrados.\n")
        return

    print("Lista de estudiantes:")
    for est in estudiantes:
        print(f"- {est['nombre']} (Edad: {est['edad']})")
        for c in est["calificaciones"]:
            print(f"   {c['materia']}: {c['nota']}")
    print()


# --- Menú interactivo ---
def menu():
    while True:
        print("===== MENÚ PRINCIPAL =====")
        print("1. Agregar estudiante")
        print("2. Eliminar estudiante")
        print("3. Calcular promedio de un estudiante")
        print("4. Mostrar todos los estudiantes")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_estudiante()
        elif opcion == "2":
            eliminar_estudiante()
        elif opcion == "3":
            promedio_estudiante()
        elif opcion == "4":
            mostrar_estudiantes()
        elif opcion == "5":
            guardar_estudiantes()  # Guardar la lista completa en ambos archivos antes de salir
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.\n")


# --- Ejecutar programa ---
cargar_estudiantes()  # Carga los datos existentes al iniciar
menu()