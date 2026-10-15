nombre = ""
while not nombre.isalpha():
    nombre = input("Nombre del cliente: ")

cantidad_str = "0"
while not cantidad_str.isdigit() or int(cantidad_str) == 0:
    cantidad_str = input("Cantidad de productos a comprar: ")
cantidad = int(cantidad_str)

total_sin_descuento = 0
total_con_descuento = 0

for i in range(1, cantidad + 1):
    print(f"--- Producto {i} ---")
    precio_str = ""
    while not precio_str.isdigit():
        precio_str = input("Precio: ")
    precio = int(precio_str)
    
    descuento = ""
    while descuento not in ["s", "n"]:
        descuento = input("Descuento (S/N): ").lower()
    
    total_sin_descuento += precio
    if descuento == "s":
        total_con_descuento += precio * 0.90
    else:
        total_con_descuento += precio

ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad

print(f"\nCliente: {nombre}")
print(f"Cantidad de productos: {cantidad}")
print(f"Total sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")
