import pdfplumber
import os
import re

# Ruta al archivo PDF
pdf_path = r'C:\Github\Ampa\documentos\Cartones.pdf'
output_path = r'C:\Github\Ampa\cartones-extraidos-pdf.md'

# Patrón para identificar el ID de una canción (número seguido de texto)
id_pattern = re.compile(r'(\d+)\s+(.+)')

def extraer_canciones_de_celda(celda):
    """Extrae canciones de una celda que puede tener múltiples líneas"""
    if not celda:
        return []
    
    canciones = []
    # Dividir por líneas
    lines = celda.split('\n')
    
    # Buscar líneas que empiecen con números
    current_song = None
    for line in lines:
        line = line.strip()
        match = id_pattern.match(line)
        if match:
            # Si hay una canción anterior, guardarla
            if current_song:
                canciones.append(current_song)
            # Iniciar nueva canción
            current_song = line
        elif current_song and line:
            # Continuar la canción anterior
            current_song += ' ' + line
    
    # Guardar última canción
    if current_song:
        canciones.append(current_song)
    
    return canciones

def extraer_cartones_pdf(pdf_path, output_path):
    with pdfplumber.open(pdf_path) as pdf:
        print(f"Total de páginas en el PDF: {len(pdf.pages)}")
        
        with open(output_path, 'w', encoding='utf-8') as f:
            for page_num, page in enumerate(pdf.pages, 1):
                print(f"\nProcesando página {page_num}...")
                
                canciones = []
                
                # Extraer tablas
                tables = page.extract_tables()
                
                if tables:
                    print(f"Encontradas {len(tables)} tablas")
                    for table_idx, table in enumerate(tables):
                        print(f"  Procesando tabla {table_idx + 1} con {len(table)} filas")
                        for row_idx, row in enumerate(table):
                            for cell_idx, cell in enumerate(row):
                                canciones_celda = extraer_canciones_de_celda(cell)
                                canciones.extend(canciones_celda)
                
                # Eliminar duplicados manteniendo orden
                canciones_unicas = []
                seen = set()
                for cancion in canciones:
                    if cancion not in seen:
                        canciones_unicas.append(cancion)
                        seen.add(cancion)
                
                print(f"Página {page_num}: {len(canciones_unicas)} canciones únicas encontradas")
                
                # Mostrar primeras 3 canciones para debug
                if len(canciones_unicas) > 0:
                    print(f"  Primeras: {canciones_unicas[:3]}")
                
                # Verificar que tengamos 36 canciones (3 cartones de 12)
                if len(canciones_unicas) != 36:
                    print(f"⚠️ ADVERTENCIA: Se esperaban 36 canciones, se encontraron {len(canciones_unicas)}")
                
                # Escribir diapositiva
                f.write(f"# Diapositiva {page_num}\n\n")
                
                # Dividir en 3 cartones de 12 canciones cada uno
                for carton_idx in range(3):
                    carton_num = (page_num - 1) * 3 + carton_idx + 1
                    start_idx = carton_idx * 12
                    end_idx = start_idx + 12
                    
                    canciones_carton = canciones_unicas[start_idx:end_idx] if start_idx < len(canciones_unicas) else []
                    
                    f.write(f"## Cartón {carton_num}\n\n")
                    
                    if len(canciones_carton) < 12:
                        f.write(f"⚠️ ADVERTENCIA: Solo se encontraron {len(canciones_carton)} canciones (se esperaban 12)\n\n")
                    
                    for cancion in canciones_carton:
                        f.write(f"{cancion}\n")
                    
                    f.write("\n")
        
        print(f"\n✅ Extracción completada. Archivo guardado en: {output_path}")

if __name__ == "__main__":
    extraer_cartones_pdf(pdf_path, output_path)
