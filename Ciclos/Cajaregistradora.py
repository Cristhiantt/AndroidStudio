# Diccionario de productos con códigos y precios
productos = {
    "001": {"nombre": "Producto 1", "precio": 10.00},
    "002": {"nombre": "Producto 2", "precio": 15.00},
    "003": {"nombre": "Producto 3", "precio": 20.00},
}

# Inicialización de variables
carrito = {}  # Diccionario para mantener los productos comprados
subtotal = 0.0

# Función para agregar un producto al carrito
def agregar_producto():
    codigo = input("Ingrese el código del producto: ")
    if codigo in productos:
        cantidad = int(input("Ingrese la cantidad: "))
        if codigo in carrito:
            carrito[codigo]["cantidad"] += cantidad
        else:
            carrito[codigo] = {
                "nombre": productos[codigo]["nombre"],
                "precio": productos[codigo]["precio"],
                "cantidad": cantidad,
            }
        print(f"{productos[codigo]['nombre']} agregado al carrito.")
    else:
        print("Producto no encontrado.")

# Función para calcular el subtotal
def calcular_subtotal():
    global subtotal
    subtotal = sum(item["precio"] * item["cantidad"] for item in carrito.values())
    print(f"Subtotal: ${subtotal:.2f}")

# Función para aplicar descuentos
def aplicar_descuentos():
    # Aquí puedes implementar tu lógica de descuentos si es necesario
    pass

# Función para calcular el cambio
def calcular_cambio():
    total_pago = float(input("Ingrese el monto pagado: "))
    if total_pago >= subtotal:
        cambio = total_pago - subtotal
        print(f"Cambio: ${cambio:.2f}")
    else:
        print("El monto pagado es insuficiente.")

# Loop principal
while True:
    print("\nOpciones:")
    print("1. Agregar producto")
    print("2. Calcular subtotal")
    print("3. Aplicar descuentos")
    print("4. Calcular cambio")
    print("5. Finalizar compra")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        calcular_subtotal()
    elif opcion == "3":
        aplicar_descuentos()
    elif opcion == "4":
        calcular_cambio()
    elif opcion == "5":
        calcular_subtotal()
        aplicar_descuentos()
        calcular_cambio()
        break
    elif opcion == "6":
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
