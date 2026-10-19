from pathlib import Path

archivo = Path("datos/productos.txt")
lineas = archivo.read_text(encoding="utf-8").splitlines()

print("=== Inventario Tienda Don Pedro ===")

productos = lineas[2:]
total_productos = 0
valor_inventario = 0

for linea in productos:
    if not linea.strip():
        continue

    print("-", linea)
    total_productos += 1

    precio_texto = linea.rsplit(" - ", 1)[-1]
    precio_limpio = precio_texto.replace("$", "").replace(".", "").strip()
    valor_inventario += int(precio_limpio)

print(f"Total de productos: {total_productos}")
print(f"Valor del inventario: ${valor_inventario:,}".replace(",", "."))