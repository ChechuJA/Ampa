import os
import re
from pathlib import Path

# Ruta de la carpeta con los MP3
ruta_mp3 = r"C:\Github\Ampa\canciones_bingo_mp3"

# Diccionario con los nombres correctos del listado-canciones.md (recursos/listado-canciones.md)
nombres_correctos = {
    1: "Los Del Rio - La Macarena",
    2: "La Oreja de Van Gogh - Rosas",
    3: "El Consorcio - El Chacacha del Tren",
    4: "Coyote Dax - No Rompas Más",
    5: "Isabel Aaiun - El himno de mi peña",
    6: "Georgie Dann - La Barbacoa",
    7: "Raphael - Mi gran noche",
    8: "Alaska - A quien le importa",
    9: "Radio Futura - Escuela de Calor",
    10: "CNCO - Reguetón Lento",
    11: "Baby Lores - La mujer del pelotero",
    12: "Joaquín Sabina - Y nos dieron las 10",
    13: "Nino Bravo - Libre",
    14: "Don Omar - Danza Kuduro",
    15: "Pereza - Princesa",
    16: "Izal - La Mujer de Verde",
    17: "Zapato veloz - Tractor amarillo",
    18: "Amaral - Mis amigos",
    19: "Myke Towers - Esa Falda",
    20: "La pegatina - Maní Carmen",
    21: "Gente de zona - La Gozadera",
    22: "Daddy Yankee - Gasolina",
    23: "King Africa - Paquito el Chocolatero",
    24: "El Canto del Loco - Zapatillas",
    25: "Los refrescos - Aquí no hay playa",
    26: "Aitana - Las Babys",
    27: "Chocolate Latino - Mayonesa",
    28: "Shakira - Pa Tipos Como Tú",
    29: "Luck Ra - La morocha",
    30: "José Luis Perales - Un Velero Llamado Libertad",
    31: "Lola Indigo - La reina",
    32: "Melendi - Caminando por la vida",
    33: "Proyecto Uno - El Tiburón",
    34: "Estopa - Por la Raja de tu Falda",
    35: "Las ketchup - Asereje",
    36: "Karol G - Si antes te hubiera conocido",
    37: "La fiesta - Quiero montarme en tu velero",
    38: "David Civera - Que la detengan",
    39: "Paulina Rubio - Y yo sigo aquí",
    40: "Vicco - Nochentera",
    41: "Camela - Cuando zarpa el amor",
    42: "Bad Bunny - Yo perreo sola",
    43: "El simbolo - Levantando las manos",
    44: "David Bisbal - Bulería",
    45: "King Africa - Bomba",
    46: "Katy Perry - Roar",
    47: "Sebastian Yatra - Tacones rojos",
    48: "Juan Magan - Ayer la vi",
    49: "ROSÉ & Bruno Mars - APT",
}

# Verificar que la ruta existe
if not os.path.exists(ruta_mp3):
    print(f"ERROR: La ruta {ruta_mp3} no existe")
    exit(1)

print("=" * 100)
print("PREVISUALIZACIÓN DE CAMBIOS")
print("=" * 100)
print()

# Obtener todos los archivos MP3 y preparar cambios
cambios = []
archivos_sin_numero = []

for archivo in os.listdir(ruta_mp3):
    if archivo.lower().endswith('.mp3'):
        # Extraer el número al inicio del nombre
        match = re.match(r'^(\d+)', archivo)
        if match:
            numero = int(match.group(1))
            if numero in nombres_correctos:
                nombre_nuevo = f"{numero} {nombres_correctos[numero]}.mp3"
                ruta_antigua = os.path.join(ruta_mp3, archivo)
                ruta_nueva = os.path.join(ruta_mp3, nombre_nuevo)
                
                if archivo != nombre_nuevo:
                    cambios.append((ruta_antigua, ruta_nueva, archivo, nombre_nuevo))
                    print(f"[{numero:2d}] {archivo}")
                    print(f"  ➜  {nombre_nuevo}")
                    print()
            else:
                archivos_sin_numero.append((numero, archivo))
        else:
            archivos_sin_numero.append((None, archivo))

if archivos_sin_numero:
    print("\n⚠️  Archivos sin número o con número no encontrado:")
    for num, archivo in archivos_sin_numero:
        print(f"  - {archivo}")
    print()

print("=" * 100)
print(f"RESUMEN: {len(cambios)} archivos para renombrar")
print("=" * 100)
print()

if len(cambios) == 0:
    print("✓ Todos los archivos ya tienen los nombres correctos")
    exit(0)

# Preguntar confirmación
respuesta = input("¿Deseas proceder con el renombrado? (S/N): ").strip().upper()

if respuesta == 'S':
    print("\n" + "=" * 100)
    print("RENOMBRANDO ARCHIVOS...")
    print("=" * 100)
    print()
    
    errores = 0
    exitosos = 0
    
    for ruta_antigua, ruta_nueva, nombre_antiguo, nombre_nuevo in cambios:
        try:
            os.rename(ruta_antigua, ruta_nueva)
            print(f"✓ Renombrado: {nombre_nuevo}")
            exitosos += 1
        except Exception as e:
            print(f"✗ ERROR al renombrar {nombre_antiguo}: {e}")
            errores += 1
    
    print("\n" + "=" * 100)
    print(f"COMPLETADO: {exitosos} exitosos, {errores} errores")
    print("=" * 100)
else:
    print("\n❌ Operación cancelada por el usuario")
