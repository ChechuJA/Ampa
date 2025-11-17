import re

# Leer el archivo
with open('cartones-bingo-musical.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Extraer todas las canciones únicas
canciones_set = set()
canciones_pattern = r'\d+ - (\d+) (.+)'
matches = re.findall(canciones_pattern, content)

for id_cancion, nombre_cancion in matches:
    canciones_set.add(f"{id_cancion} {nombre_cancion}")

# Ordenar por número de ID
canciones_lista = sorted(canciones_set, key=lambda x: int(x.split()[0]))

print("=" * 80)
print(f"TOTAL DE CANCIONES DISTINTAS: {len(canciones_lista)}")
print("=" * 80)

for cancion in canciones_lista:
    print(cancion)

# Obtener el ID máximo
ids = [int(x.split()[0]) for x in canciones_lista]
print("\n" + "=" * 80)
print(f"ID mínimo: {min(ids)}")
print(f"ID máximo: {max(ids)}")
print(f"Siguiente ID disponible: {max(ids) + 1}")
print("=" * 80)
