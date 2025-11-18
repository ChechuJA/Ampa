import re
from collections import defaultdict

# Leer el archivo (ahora en la carpeta recursos)
with open('recursos/cartones-bingo-musical-original.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Diccionario de normalización de nombres (para unificar variantes)
normalizacion = {
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
    42: "Bad Bunny - Yo perreo sola",  # Corregido de "Bab Bunny" a "Bad Bunny"
    43: "El simbolo - Levantando las manos",
    44: "David Bisbal - Si Tu la Quieres",
    45: "King Africa - Bomba",
    47: "Sebastian Yatra - Tacones rojos",
    48: "Juan Magan - Ayer la vi",
}

# Extraer todas las canciones del archivo
patron = r'^\d{1,2} - (\d+)\s*(.+?)$'
matches = re.findall(patron, content, re.MULTILINE)

# Contar apariciones de cada ID
conteo = defaultdict(int)
for id_str, nombre in matches:
    id_cancion = int(id_str)
    # No contar "42 King Africa" porque es un error
    if not (id_cancion == 42 and "King Africa" in nombre):
        conteo[id_cancion] += 1

print("=" * 100)
print("LISTADO COMPLETO Y NORMALIZADO DE CANCIONES")
print("=" * 100)
print()

total_canciones = len(normalizacion)
print(f"**Total de canciones: {total_canciones}**\n")

for id_cancion in sorted(normalizacion.keys()):
    nombre = normalizacion[id_cancion]
    veces = conteo.get(id_cancion, 0)
    print(f"{id_cancion} - {nombre}")

# IDs faltantes
ids_existentes = set(normalizacion.keys())
id_max = max(ids_existentes)
ids_faltantes = []
for i in range(1, id_max + 1):
    if i not in ids_existentes:
        ids_faltantes.append(i)

print("\n" + "=" * 100)
print("NOTAS")
print("=" * 100)
if ids_faltantes:
    print(f"- IDs faltantes en el rango 1-{id_max}: {', '.join(map(str, ids_faltantes))}")
else:
    print(f"- Todas las canciones del 1 al {id_max} están presentes (excepto IDs faltantes)")

print("\n- ERRORES ENCONTRADOS EN EL ARCHIVO ORIGINAL:")
print("  * 4 instancias de '42 King Africa - Bomba' que deberían ser '45 King Africa - Bomba'")
print("  * El ID 46 no existe en los cartones originales")
print("  * 'Bab Bunny' debería ser 'Bad Bunny' (error de ortografía)")

# Guardar en archivo
with open('recursos/listado-canciones-final.md', 'w', encoding='utf-8') as f:
    f.write("# Listado de Canciones - Bingo Musical AMPA Colegio Peñamiel\n\n")
    f.write("Este documento contiene todas las canciones utilizadas en el Bingo Musical.\n\n")
    f.write(f"**Total de canciones: {total_canciones}**\n\n")
    f.write("---\n\n")
    
    for id_cancion in sorted(normalizacion.keys()):
        nombre = normalizacion[id_cancion]
        f.write(f"{id_cancion} - {nombre}\n")
    
    f.write("\n---\n\n")
    f.write("**Notas:**\n")
    if ids_faltantes:
        f.write(f"- IDs faltantes: {', '.join(map(str, ids_faltantes))}\n")
    f.write("- ERRORES ENCONTRADOS EN EL ARCHIVO ORIGINAL:\n")
    f.write("  * 4 instancias de '42 King Africa - Bomba' que deberían ser '45 King Africa - Bomba'\n")
    f.write("  * El ID 46 no existe en los cartones originales\n")
    f.write("  * 'Bab Bunny' debería ser 'Bad Bunny' (error de ortografía)\n")

print("\n✓ Archivo 'recursos/listado-canciones-final.md' generado exitosamente")
