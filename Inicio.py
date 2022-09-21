from persona import persona
misContactos = []

def crearContacto(numero, nombre, direccion):
    misContactos.append(persona(numero, nombre, direccion))
    print("Contato almacenado")

def buscarContactos(nombre):
    if len(misContactos) == 0:
       print("La lista esta vacia, no  hay contatos que buscar")
    else:
        encontrado = False
        for i in range(len(misContactos)):
            if misContactos[i].verNombre() == nombre:
               print("El telefono es", misContactos[i].verNumero())
               print("La direccion es ", misContactos[i].verDireccion())
               encontrado = True
               break
            else:
                encontrado - False
        if encontrado == False:
         print("Dato no existente..")

def mostrarContactos():
    if len(misContactos) == 0:
        print("La lista esta vacía, no hay contactos que buscar...")
    else:
        for i in range(len(misContactos)):
            print('Nombre: ', misContactos[i].verNombre(), ' Dirección', misContactos[i].verDireccion(), ' Teléfono', misContactos[i].verNumero())

def modificarContacto(nombre):
    if len(misContactos) == 0:
        print("La lista esta vacía, no hay contactos que buscar...")
    else:
        encontrado = False
        posicion = None
        for i in range(len(misContactos)):
            if misContactos[i].verNombre() == nombre:
                posicion = i
                encontrado = True
                break
            else:
                encontrado = False
        if encontrado:
            nuevoNumero = int(input("Ingrese el nuevo número: "))
            nuevoNombre = input("Ingrese nuevo nombre: ")
            nuevaDireccion = input("Ingrese la nueva dirección: ")
            misContactos[posicion].modificarNumero(nuevoNumero)
            misContactos[posicion].modificarNombre(nuevoNombre)
            misContactos[posicion].modificarDireccion(nuevaDireccion)
            print("Datos actualizados con éxito...")
        else:
            print("Dato no encontrado...")

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
        crearContacto(numero, nombre, direccion)
    elif op ==2:
        nombre = input("Ingrese el nombre del contacto a buscar ")
        buscarContactos(nombre)

#iniciar programa
main()

    
