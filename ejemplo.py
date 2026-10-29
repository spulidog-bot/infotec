while True:
    try:
        cantidad = int(input("¿Cuántos productos desea registrar? "))

        if cantidad > 0:
            break

        print("Error: debe registrar al menos un producto.")

    except ValueError:
        print("Solamente se permiten números enteros. Ingrese un número entero.")


for i in range(cantidad):
    print(f"\nRegistro del Producto {i + 1}")

    while True:
        try:
            nombre = input("Ingrese el nombre del producto: ")

            if nombre:
                break

            print("Error: el nombre no puede estar vacío.")
        except ValueError:
            print("Error: ingrese un nombre válido.")

    while True:
            try:
                cantidad = input("Ingrese el ca del producto: ")
    
                if nombre:
                    break
    
                print("Error: el nombre no puede estar vacío.")
            except ValueError:
                print("Error: ingrese un nombre válido.")