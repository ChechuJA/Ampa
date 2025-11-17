import re
from collections import Counter
import os

# Obtener la ruta del directorio padre (donde está el archivo .md)
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
md_file = os.path.join(parent_dir, 'cartones-bingo-musical.md')

# Leer el archivo
with open(md_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Extraer todos los cartones con sus canciones
carton_pattern = r'## Cartón (\d+).*?\n\n((?:\d+ - .*\n)+)'
cartones = re.findall(carton_pattern, content)

print("=" * 80)
print("BUSCANDO DUPLICADOS EN CARTONES DE BINGO MUSICAL")
print("=" * 80)

# TIPO 1: Canciones duplicadas dentro del mismo cartón
print("\n📋 TIPO 1: Canciones duplicadas DENTRO del mismo cartón")
print("-" * 80)

tipo1_encontrados = False
for carton_num, canciones_text in cartones:
    # Extraer las canciones del cartón
    canciones = re.findall(r'\d+ - (.+)', canciones_text)
    
    # Contar duplicados
    contador = Counter(canciones)
    duplicados = {cancion: count for cancion, count in contador.items() if count > 1}
    
    if duplicados:
        tipo1_encontrados = True
        print(f"\n⚠️  CARTÓN {carton_num} tiene canciones duplicadas:")
        for cancion, veces in duplicados.items():
            print(f"   - '{cancion}' aparece {veces} veces")

if not tipo1_encontrados:
    print("\n✅ No se encontraron canciones duplicadas dentro de ningún cartón")

# TIPO 2: Cartones con las mismas canciones (diferente orden)
print("\n\n📋 TIPO 2: Cartones con las MISMAS canciones (distinto orden)")
print("-" * 80)

# Crear diccionario con conjuntos de canciones por cartón
cartones_dict = {}
for carton_num, canciones_text in cartones:
    canciones = re.findall(r'\d+ - (.+)', canciones_text)
    # Usar frozenset para comparar sin importar el orden
    canciones_set = frozenset(canciones)
    
    if canciones_set not in cartones_dict:
        cartones_dict[canciones_set] = []
    cartones_dict[canciones_set].append(carton_num)

# Buscar duplicados
tipo2_encontrados = False
for canciones_set, numeros_carton in cartones_dict.items():
    if len(numeros_carton) > 1:
        tipo2_encontrados = True
        print(f"\n⚠️  Los cartones {', '.join(numeros_carton)} tienen las MISMAS canciones:")
        for cancion in sorted(canciones_set):
            print(f"   - {cancion}")

if not tipo2_encontrados:
    print("\n✅ No se encontraron cartones con las mismas canciones")

print("\n" + "=" * 80)
print("ANÁLISIS COMPLETADO")
print("=" * 80)
