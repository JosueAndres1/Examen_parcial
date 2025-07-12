productos = {
    '8475HD': ['HP', 15.6,'8GB','DD','1T','Intel Core i5','Nvidia GTX1050'],
    '2175HD': ['lenovo',14,'4GB','SSD','512GB','Intel Core i5','Nvidia GTX1050'],
    'JjfFHD': ['Asus',14,'16GB','SSD','256GB','Intel Core i7', 'Nvidia RTX2080Ti'],
    'UWU131HD':['Dell',15.6,'8GB','DD','1T','AMD Ryzen 3','Nvidia GTX1050'],
}

stock = {
    '8475HD':[387990,10],'2175HD':[327990,4],'JjfFHD':[424990,1],'UWU131HD':[349990,1],
}

precio = 0
encontrados = 0
def mostrar_menu():
    print("\n---Menu Principal---")
    print("1. Stock marca")
    print("2. Busqueda por precio")
    print("3. Actualizar precio")
    print("4. Salir")
    

def opcion_sotck_marca():
    marca = input("Ingrese marca a buscar: ").strip().lower()
    encontrados = []
    for modelo, datos in productos.items():
        if datos[0].lower() == marca.lower():
            encontrados.append(modelo)
    
    if encontrados:
        for modelo in encontrados:
            print(f"{modelo}:{productos[modelo]} - Precio: ${stock[modelo][0]} - Stock: {stock[modelo][1]}")
    else:
        print("No se encontraron notebooks de esa marca.")

def opcion_busqueda_precio():
    try:
        min_precio = int(input("Ingresa el precio minimo: "))
        max_precio = int(input("Ingresa el precio maximo: "))
        modelos_encontrados = []
        
        for modelo,info in stock.items():
            precio = info[0]
            if min_precio <= precio <= max_precio:
                modelos_encontrados.append(modelo)
        
        if modelos_encontrados:
            for modelo in modelos_encontrados:
                print(f"{modelo}:{productos[modelo] - Precio: {stock[modelo[0]]}}")
        else:
            print("No hay notebooks en ese rango de precio.")
    except ValueError:
        print("Error: Debes ingresar un numero entero valido")


def opcion_actualizar_precio():
    modelo = input("Ingrese modelo a actualizar: ")
    modelo_in_stock = False
    if modelo in stock:
        modelo_in_stock = True
        try:
            nuevo_precio = int(input("Ingrese nuevo precio: "))
            stock[modelo][0] = nuevo_precio
            print("Precio actualizado con exito.")
        except ValueError:
            print("Error: Debes ingresar un numero valido")
    else:
        print("El modelo no existe.")
        respuesta = input("¿Desea actualiozar otro precio?(s/n): ")
        if respuesta == "s":
            opcion_actualizar_precio()


def ejecutar_menu():
    while True:
        mostrar_menu()
        opcion = input("Ingrese una opcion: ")
        
        if opcion == "1":
            opcion_sotck_marca()
        elif opcion == "2":
            opcion_busqueda_precio()
        elif opcion == "3":
            opcion_actualizar_precio()
        elif opcion == "4":
            print("Programa finalizado....")
            break
        else:
            print("Debe seleccionar una opcion valida(1,2,3,4).")



#funcion para ejecutar nuestro programa
ejecutar_menu()
