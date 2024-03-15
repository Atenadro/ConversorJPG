Image-to-PDF Converter
Este script en Python toma un conjunto de imágenes en formato JPG y las combina en un único archivo PDF. Es ideal para consolidar visualizaciones gráficas, fotos, o diagramas en un solo documento, facilitando la compartición o el almacenamiento eficiente de múltiples imágenes.

Características
Conversión Eficiente: Convierte y combina múltiples imágenes JPG en un solo archivo PDF.
Compatibilidad de Formato: Asegura la conversión de imágenes en formato RGBA a RGB para evitar cualquier problema de incompatibilidad.
Automatización: Procesa automáticamente una lista predefinida de imágenes desde una carpeta específica, simplificando el flujo de trabajo.
Instalación
No se requiere instalación específica para el script en sí, pero debes tener Python y PIL (Pillow) instalados en tu sistema. Si aún no los tienes, puedes instalarlos usando pip:


Copy code
pip install pillow
Uso
Para utilizar el script, sigue estos pasos:

Coloca todas tus imágenes JPG en la carpeta image1 dentro del directorio del script.

Ejecuta el script con Python:


Copy code
python nombre_del_script.py
Encuentra el archivo union.pdf generado en el mismo directorio del script, que contendrá todas tus imágenes combinadas.

Personalización
Puedes modificar el script para cambiar la carpeta de origen de las imágenes o el nombre del archivo PDF resultante ajustando las variables al principio del script.

Contribución
Si tienes sugerencias para mejorar este script, siéntete libre de contribuir:

Haz un fork del proyecto.
Crea tu rama de características (git checkout -b feature/AmazingFeature).
Haz commit de tus cambios (git commit -m 'Add some AmazingFeature').
Push a la rama (git push origin feature/AmazingFeature).
Abre un Pull Request.
Licencia
Distribuido bajo la licencia MIT. Consulta el archivo LICENSE para más información.

