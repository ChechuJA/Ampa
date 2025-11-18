import re

# Leer el archivo (ahora en la carpeta recursos)
with open('recursos/cartones-bingo-musical-original.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Extraer todas las canciones únicas
# Patrón mejorado que captura líneas que comienzan con número - número
canciones_set = set()

# Buscar líneas que empiecen con "1 - " hasta "12 - " (posiciones en el cartón)
# Seguido del número de canción y el nombre
canciones_pattern = r'^\d{1,2} - (\d+)\s*(.+?)$'
matches = re.findall(canciones_pattern, content, re.MULTILINE)

print(f"Total de coincidencias encontradas: {len(matches)}")

for id_cancion, nombre_cancion in matches:
    # Limpiar el nombre de la canción
    nombre_cancion = nombre_cancion.strip()
    canciones_set.add((int(id_cancion), nombre_cancion))

# Ordenar por número de ID
canciones_lista = sorted(canciones_set, key=lambda x: x[0])

print("\n" + "=" * 80)
print(f"TOTAL DE CANCIONES DISTINTAS: {len(canciones_lista)}")
print("=" * 80)
print()

for id_cancion, nombre_cancion in canciones_lista:
    print(f"{id_cancion} - {nombre_cancion}")

# Verificar qué números faltan
ids_encontrados = [x[0] for x in canciones_lista]
print("\n" + "=" * 80)
print(f"ID mínimo: {min(ids_encontrados)}")
print(f"ID máximo: {max(ids_encontrados)}")
print(f"Total de IDs únicos: {len(ids_encontrados)}")

# Buscar IDs faltantes en el rango
ids_faltantes = []
for i in range(1, max(ids_encontrados) + 1):
    if i not in ids_encontrados:
        ids_faltantes.append(i)

if ids_faltantes:
    print(f"\nIDs FALTANTES: {ids_faltantes}")
else:
    print("\nNo hay IDs faltantes en el rango 1-" + str(max(ids_encontrados)))

print("=" * 80)

# Guardar en archivo
with open('recursos/listado-canciones-extraido.md', 'w', encoding='utf-8') as f:
    f.write("# Listado de Canciones - Bingo Musical AMPA Colegio Peñamiel\n\n")
    f.write("Este documento contiene todas las canciones utilizadas en el Bingo Musical.\n\n")
    f.write(f"**Total de canciones: {len(canciones_lista)}**\n\n")
    f.write("---\n\n")
    
    for id_cancion, nombre_cancion in canciones_lista:
        f.write(f"{id_cancion} - {nombre_cancion}\n")
    
    f.write("\n---\n\n")
    f.write("**Notas:**\n")
    if ids_faltantes:
        f.write(f"- IDs faltantes: {', '.join(map(str, ids_faltantes))}\n")

print("\n✓ Archivo 'recursos/listado-canciones-extraido.md' creado exitosamente")
