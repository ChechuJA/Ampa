import os
from pathlib import Path
import re

# Ruta de la carpeta con los MP3
ruta_mp3 = r"C:\Github\Ampa\canciones_bingo_mp3"

# Verificar que la ruta existe
if not os.path.exists(ruta_mp3):
    print(f"ERROR: La ruta {ruta_mp3} no existe")
    exit(1)

# Obtener todos los archivos MP3
archivos_mp3 = []
for archivo in os.listdir(ruta_mp3):
    if archivo.lower().endswith('.mp3'):
        # Extraer el número al inicio del nombre
        match = re.match(r'^(\d+)', archivo)
        if match:
            numero = int(match.group(1))
            archivos_mp3.append((numero, archivo))
        else:
            # Si no tiene número, lo ponemos al final
            archivos_mp3.append((999, archivo))

# Ordenar por número
archivos_mp3.sort(key=lambda x: x[0])

print("=" * 100)
print(f"ARCHIVOS MP3 ENCONTRADOS: {len(archivos_mp3)}")
print("=" * 100)

# Guardar en archivo
with open('recursos/listado-mp3.md', 'w', encoding='utf-8') as f:
    f.write("# Listado de Archivos MP3 - Bingo Musical\n\n")
    f.write(f"**Total de archivos: {len(archivos_mp3)}**\n\n")
    f.write("---\n\n")
    
    for numero, archivo in archivos_mp3:
        # Eliminar la extensión .mp3 para mostrar solo el título
        titulo = archivo[:-4] if archivo.lower().endswith('.mp3') else archivo
        print(f"{titulo}")
        f.write(f"{titulo}\n")
    
    f.write("\n---\n")

print("\n" + "=" * 100)
print("✓ Archivo 'recursos/listado-mp3.md' creado exitosamente")
print("=" * 100)
