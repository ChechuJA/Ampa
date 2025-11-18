# AMPA Colegio Peñamiel - Sonseca

Sitio web oficial de la Asociación de Madres y Padres de Alumnos del Colegio Peñamiel de Sonseca.

## 🌐 Ver el sitio web

El sitio está desplegado en GitHub Pages: [https://chechuja.github.io/Ampa/](https://chechuja.github.io/Ampa/)

## 📋 Características

- **Inicio**: Página de bienvenida con información sobre el AMPA
- **Noticias**: Últimas novedades y anuncios
- **Calendario**: Eventos programados (excursiones, mercadillo navideño, fiesta fin de curso)
- **Cuotas**: Información sobre las cuotas anuales (2,50 € por niño/a)
- **Galería**: Fotos de actividades y eventos
- **Juegos**: Bingo Musical con cartones y canciones descargables
- **Voluntariado**: Oportunidades para colaborar
- **Patrocinadores**: Empresas que apoyan al AMPA
- **Documentos**: Enlaces a formularios y documentación importante
- **Contacto**: Formulario para ponerse en contacto

## � Bingo Musical

El sitio incluye material completo para jugar al Bingo Musical:
- **63 cartones** en formato PDF y PowerPoint (versiones original y corregida)
- **49 canciones** en formato MP3 descargables en ZIP (68MB)
- Listado completo de canciones con artistas
- Instrucciones del juego y premios

### Descargas disponibles:
- [Cartones Corregidos (PDF)](https://github.com/ChechuJA/Ampa/raw/main/documentos/Cartones%20Corregidos.pdf)
- [Cartones Corregidos (PPTX)](https://github.com/ChechuJA/Ampa/raw/main/documentos/Cartones%20Corregidos.pptx)
- [Canciones MP3 (ZIP)](https://github.com/ChechuJA/Ampa/raw/main/documentos/canciones-bingo-musical.zip)
- [Listado de Canciones](recursos/listado-canciones.md)

## �🎨 Diseño

- Diseño responsive (adaptado a móviles y tablets)
- Colores alegres y familiares
- Navegación intuitiva
- Animaciones suaves

## 🚀 Despliegue en GitHub Pages

El sitio se despliega automáticamente en GitHub Pages cuando se hace push a la rama principal.

### Pasos para activar GitHub Pages:

1. Ve a la configuración del repositorio (Settings)
2. En el menú lateral, selecciona "Pages"
3. En "Source", selecciona la rama principal (main/master)
4. Guarda los cambios
5. El sitio estará disponible en: `https://chechuja.github.io/Ampa/`

## 📁 Estructura del proyecto

```
Ampa/
├── index.html                    # Página principal
├── styles.css                    # Estilos CSS
├── script.js                     # JavaScript para interactividad
├── README.md                     # Este archivo
├── CNAME                         # Dominio personalizado
├── .nojekyll                     # Evita procesamiento Jekyll
├── .gitignore                    # Excluye MP3, incluye ZIP
│
├── documentos/                   # Archivos descargables públicos
│   ├── Cartones Corregidos.pdf
│   ├── Cartones Corregidos.pptx
│   ├── Cartones Originales.pdf
│   ├── Cartones Originales.pptx
│   └── canciones-bingo-musical.zip  # 49 canciones MP3 (68MB)
│
├── recursos/                     # Archivos de referencia
│   ├── listado-canciones.md      # Listado oficial de canciones
│   ├── cartones-bingo-musical-corregido.md
│   ├── cartones-bingo-musical-original.md
│   ├── listado-mp3.md
│   ├── cartones-extraidos-pdf.md
│   └── analisis-canciones.txt
│
├── scripts/                      # Scripts Python de utilidad
│   ├── contar_canciones.py
│   ├── encontrar_duplicados.py
│   ├── renombrar_mp3.py
│   ├── crear_zip_canciones.py
│   └── otros scripts...
│
└── canciones_bingo_mp3/          # Carpeta local con MP3 (no en Git)
    └── (49 archivos MP3 - excluidos por .gitignore)
```

## 🔒 .gitignore

El archivo `.gitignore` está configurado para:
- ✅ **Excluir** la carpeta `canciones_bingo_mp3/` (archivos MP3 grandes)
- ✅ **Incluir** el archivo ZIP comprimido en `documentos/`
- ✅ Excluir archivos temporales, cache de Python, y archivos de sistema

## 🛠️ Tecnologías utilizadas

- HTML5
- CSS3 (con variables CSS y Flexbox/Grid)
- JavaScript (Vanilla JS)
- Google Fonts (Poppins)

## 📝 Cómo actualizar el contenido

### Actualizar noticias

Edita el archivo `index.html` y busca la sección `<!-- Noticias Section -->`. Modifica o añade nuevos artículos siguiendo la estructura existente.

### Añadir eventos

Busca la sección `<!-- Calendario de Eventos -->` en `index.html` y actualiza las tarjetas de eventos.

### Modificar información de contacto

Edita los datos en la sección `<!-- Formulario de Contacto -->`.

## 💡 Soporte

Para cualquier consulta sobre el sitio web, contacta con el AMPA:
- 📧 Email: ampa@colegiopenamiel.com
- 📱 Teléfono: 925 38 00 00

---

© 2024 AMPA Colegio Peñamiel. Todos los derechos reservados.
