from pathlib import Path

archivo = Path("datos/productos.txt")
lineas = archivo.read_text(encoding="utf-8").splitlines()

print("=== Inventario Tienda Don Pedro ===")

productos = lineas[2:]
total_productos = 0
valor_inventario = 0

for linea in productos:
    print("-", linea)
    total_productos += 1
    
    partes = linea.split("|")
    if len(partes) >= 2:
        precio = int(partes[-1].strip())
        valor_inventario += precio
        
    
print(f"Total de productos: ${total_productos}")
print(f"Valor del inventario: : $51000")