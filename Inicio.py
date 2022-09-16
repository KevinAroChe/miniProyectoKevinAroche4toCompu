from persona import persona
misContactos = []

def crearContacto():
    print("Creando contacto")


def main():
    op = 0
    while op != 7:
     print("Agende")
     print("1 Crear contacto")
     print("2 Buscar contacto")
     print("3 ver contacto")
     print("4 moodificar contacto")
     print("5 eliminar contacto")
     print("6 Crear reporte en HTML")
     print("")
    op = int(input("ingrese el nnumero de opcion: "))
    if op ==1:
        numero = int(input("ingrse el numero de telefono"))
        nombre = int(input("ingrse el nombre:"))
        direccion = int(input("ingrse la direccion"))
        crearContacto()

#iniciar programa
main()

    
