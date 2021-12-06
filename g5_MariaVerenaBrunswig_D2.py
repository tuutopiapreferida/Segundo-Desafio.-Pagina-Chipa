#Desafio 2: Diseñar un programa en Pyhton, que usando diccionario nos permita:
# a) cargar la agenda telefonica de nuestros colegas(al menos 5)
# b) nos permita buscar el teléfono de algun contacto

agenda = {"Juana": 624558954,
          "Belen": 3624335896,
          "Nicolas": 3624412255,
          "Roberto": 3624614789,
          "Monica": 3624225541}

consultar = True

while consultar:
    print("-------")
    print("MI AGENDA")
    print("-------")
    print("1. Consultar")
    print("2. Agregar")
    print("3. Modificar")
    print("4. Borrar")
    print("-------")
    
    seleccionar = ""
    while seleccionar not in ("1", "2", "3", "4"):
        seleccionar = input("-> ")
    if seleccionar == "1":
        nombre = input("Nombre: ")
        if nombre not in agenda:
            print("Ese contacto no existe")
        else:
              telefono = agenda[nombre]
              print(nombre, ":", telefono)
              
    elif seleccionar == "2":
           nombre = input("Nombre: ")
           if nombre in agenda:
              print("Ese contacto ya esta agendado")
           else:
               telefono = int(input("Télefono: "))
               agenda[nombre] = telefono
               print("El contacto se agendo correctamente")
            
    elif seleccionar == "3":
           nombre = input("Nombre: ")
           if nombre not in agenda:
               print("Ese contacto no existe")
           else:
                telefono = int(input("Télefono: "))
                agenda[nombre] = telefono
                print("El contacto de ha modificado")
    elif seleccionar == "4":
           nombre = input("Nombre: ")
           if nombre not in agenda:
               print("Ese contacto no existe")
           else:
                del agenda[nombre]
                print("El contacto se ha eliminado correctamente")
                
    
    
          