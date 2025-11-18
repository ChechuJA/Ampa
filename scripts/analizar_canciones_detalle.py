import re
from collections import defaultdict
import sys

# Configurar la salida para UTF-8
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

# Leer el archivo (ahora en la carpeta recursos)
with open('recursos/cartones-bingo-musical-original.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Diccionario para almacenar canciones por ID
canciones_por_id = defaultdict(set)
lineas_con_error = []

# Patrón para detectar líneas de canciones
patron = r'^(\d{1,2}) - (\d+)\s*(.+?)$'

for num_linea, linea in enumerate(lines, 1):
    match = re.match(patron, linea.strip())
    if match:
        posicion = match.group(1)
        id_cancion = int(match.group(2))
        nombre_cancion = match.group(3).strip()
        
        canciones_por_id[id_cancion].add((nombre_cancion, num_linea, linea.strip()))

# Mostrar todas las canciones agrupadas por ID
print("=" * 100)
print("ANÁLISIS DE CANCIONES POR ID")
print("=" * 100)

for id_cancion in sorted(canciones_por_id.keys()):
    variantes = canciones_por_id[id_cancion]
    if len(variantes) > 1:
        print(f"\n⚠️  ID {id_cancion} tiene {len(variantes)} variantes:")
        for nombre, linea_num, linea_completa in sorted(variantes):
            print(f"   Línea {linea_num}: {nombre}")
    else:
        nombre, _, _ = list(variantes)[0]
        print(f"✓ ID {id_cancion}: {nombre}")

# Buscar IDs problemáticos
print("\n" + "=" * 100)
print("ANÁLISIS DE POSIBLES ERRORES")
print("=" * 100)

# Verificar si "42 King Africa - Bomba" aparece
if 42 in canciones_por_id:
    print(f"\n⚠️  ID 42 encontrado:")
    for nombre, linea_num, linea_completa in canciones_por_id[42]:
        print(f"   Línea {linea_num}: {nombre}")
        if "King Africa" in nombre:
            print(f"   ❌ ERROR: King Africa debería ser ID 45, no 42")

if 45 in canciones_por_id:
    print(f"\n✓ ID 45 encontrado:")
    for nombre, linea_num, linea_completa in canciones_por_id[45]:
        print(f"   Línea {linea_num}: {nombre}")

# IDs faltantes
ids_encontrados = set(canciones_por_id.keys())
id_max = max(ids_encontrados)
ids_faltantes = []
for i in range(1, id_max + 1):
    if i not in ids_encontrados:
        ids_faltantes.append(i)

print(f"\n" + "=" * 100)
print(f"RESUMEN")
print("=" * 100)
print(f"Total de IDs únicos encontrados: {len(ids_encontrados)}")
print(f"Rango de IDs: {min(ids_encontrados)} - {id_max}")
if ids_faltantes:
    print(f"IDs faltantes: {ids_faltantes}")
else:
    print("No hay IDs faltantes")

# Contar ocurrencias de cada canción
print(f"\n" + "=" * 100)
print("FRECUENCIA DE CADA CANCIÓN")
print("=" * 100)

conteo_canciones = defaultdict(int)
for id_cancion, variantes in canciones_por_id.items():
    # Tomar el nombre más común o el primero
    nombres = [nombre for nombre, _, _ in variantes]
    nombre_principal = max(variantes, key=lambda x: len([n for n in nombres if n.lower() == x[0].lower()]))[0]
    
    # Contar en todo el archivo
    patron_busqueda = rf'^\d+ - {id_cancion}\s'
    conteo = sum(1 for linea in lines if re.match(patron_busqueda, linea.strip()))
    conteo_canciones[id_cancion] = conteo

for id_cancion in sorted(conteo_canciones.keys()):
    variantes = canciones_por_id[id_cancion]
    nombre = list(variantes)[0][0]
    conteo = conteo_canciones[id_cancion]
    print(f"ID {id_cancion:2d}: {nombre:50s} - Aparece {conteo:3d} veces")
