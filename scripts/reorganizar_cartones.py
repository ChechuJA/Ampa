import re

# Leer el archivo actual
with open('cartones-bingo-musical.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Extraer el encabezado
header = """# Cartones de Bingo Musical

Este documento contiene el listado completo de las canciones de todos los cartones del Bingo Musical del AMPA Colegio Peñamiel.

---
"""

# Encontrar todos los cartones usando expresión regular
carton_pattern = r'## Cartón (\d+)\n\n((?:.*\n)*?)(?=\n---\n|$)'
cartones = re.findall(carton_pattern, content, re.MULTILINE)

# Crear el nuevo contenido
nuevo_contenido = header

# Agrupar cartones en diapositivas de 3
for i in range(0, len(cartones), 3):
    diapositiva_num = (i // 3) + 1
    nuevo_contenido += f"# Diapositiva {diapositiva_num}\n\n"
    
    # Añadir los 3 cartones de esta diapositiva
    for j in range(3):
        if i + j < len(cartones):
            carton_num, carton_content = cartones[i + j]
            nuevo_contenido += f"## Cartón {carton_num}\n\n{carton_content}\n---\n"
            
            # Solo añadir separación si no es el último cartón de la diapositiva
            if j < 2 and i + j + 1 < len(cartones):
                nuevo_contenido += "\n"

# Guardar el nuevo archivo
with open('cartones-bingo-musical.md', 'w', encoding='utf-8') as f:
    f.write(nuevo_contenido)

print(f"✅ Archivo reorganizado exitosamente!")
print(f"📊 Total de cartones: {len(cartones)}")
print(f"📑 Total de diapositivas: {(len(cartones) + 2) // 3}")
