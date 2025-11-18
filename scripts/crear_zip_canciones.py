import zipfile
import os
from pathlib import Path

# Rutas
ruta_mp3 = r"C:\Github\Ampa\canciones_bingo_mp3"
ruta_zip = r"C:\Github\Ampa\documentos\canciones-bingo-musical.zip"

# Verificar que la carpeta existe
if not os.path.exists(ruta_mp3):
    print(f"ERROR: La carpeta {ruta_mp3} no existe")
    exit(1)

print("=" * 100)
print("CREANDO ZIP CON CANCIONES MP3")
print("=" * 100)
print()

# Obtener todos los archivos MP3
archivos_mp3 = []
for archivo in os.listdir(ruta_mp3):
    if archivo.lower().endswith('.mp3'):
        archivos_mp3.append(archivo)

archivos_mp3.sort()

print(f"📁 Encontrados {len(archivos_mp3)} archivos MP3")
print()

# Crear el archivo ZIP
with zipfile.ZipFile(ruta_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for archivo in archivos_mp3:
        ruta_completa = os.path.join(ruta_mp3, archivo)
        # Añadir al ZIP sin la ruta completa, solo el nombre del archivo
        zipf.write(ruta_completa, archivo)
        print(f"  ✓ Añadido: {archivo}")

# Obtener tamaño del ZIP
tamaño_bytes = os.path.getsize(ruta_zip)
tamaño_mb = tamaño_bytes / (1024 * 1024)

print()
print("=" * 100)
print(f"✓ ZIP CREADO EXITOSAMENTE")
print(f"  Ubicación: {ruta_zip}")
print(f"  Archivos: {len(archivos_mp3)}")
print(f"  Tamaño: {tamaño_mb:.2f} MB")
print("=" * 100)
