import pdfplumber
import os
import re

# Ruta al archivo PDF
pdf_path = os.path.expanduser(r'C:\Github\Ampa\documentos\Cartones.pdf')

print(f"Buscando archivo en: {pdf_path}")

if not os.path.exists(pdf_path):
    print(f"❌ ERROR: No se encontró el archivo {pdf_path}")
    exit(1)

# Abrir el PDF
print("📂 Abriendo PDF...")

# Generar el markdown
md_lines = ['# Cartones de Bingo Musical', '']
card_index = 1
diapositiva = 1

# Patrón para detectar canciones: ID + espacio + artista - canción
# Ejemplo: "4 Coyote Dax - No Rompas Más"
song_pattern = re.compile(r'^\d+\s+.+\s+-\s+.+')

with pdfplumber.open(pdf_path) as pdf:
    print(f"✅ Se encontraron {len(pdf.pages)} páginas")
    
    for page_num, page in enumerate(pdf.pages, start=1):
        # Extraer todo el texto de la página
        text = page.extract_text()
        
        if not text:
            print(f"  ⚠️  Página {page_num}: Sin texto extraíble")
            continue
        
        # Dividir en líneas y limpiar
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        
        # Filtrar solo las líneas que son canciones
        songs = [line for line in lines if song_pattern.match(line)]
        
        # Eliminar duplicados manteniendo el orden
        unique_songs = []
        seen = set()
        for song in songs:
            if song not in seen:
                unique_songs.append(song)
                seen.add(song)
        
        songs = unique_songs
        
        print(f"  Página {page_num}: {len(songs)} canciones únicas detectadas")
        
        # Cada página = 1 diapositiva con 3 cartones (36 canciones)
        if len(songs) != 36:
            print(f"    ⚠️  ADVERTENCIA: {len(songs)} canciones (se esperaban 36 para 3 cartones)")
        
        # Añadir encabezado de diapositiva
        md_lines.append(f'# Diapositiva {diapositiva}')
        md_lines.append('')
        
        # Agrupar en 3 cartones de 12 canciones cada uno
        for card_num in range(3):
            start_idx = card_num * 12
            end_idx = min(start_idx + 12, len(songs))
            card_songs = songs[start_idx:end_idx]
            
            md_lines.append(f'## Cartón {card_index}')
            md_lines.append('')
            
            if len(card_songs) != 12:
                print(f"    ⚠️  ERROR: Cartón {card_index} tiene {len(card_songs)} canciones en lugar de 12")
            
            for idx, entry in enumerate(card_songs, start=1):
                md_lines.append(f'{idx} - {entry}')
            
            md_lines.append('')
            md_lines.append('---')
            card_index += 1
        
        md_lines.append('')
        diapositiva += 1

# Guardar en archivo
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
output_file = os.path.join(parent_dir, 'cartones-extraidos-pdf.md')

md_text = '\n'.join(md_lines)
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(md_text)

print(f'\n✅ Procesadas {len(pdf.pages)} páginas')
print(f'✅ Extraídos {card_index - 1} cartones')
print(f'✅ Archivo guardado: {output_file}')
print(f'\n💡 Revisa las advertencias arriba para identificar páginas con problemas.')
