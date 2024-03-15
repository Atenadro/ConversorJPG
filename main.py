from PIL import Image

# Lista de tus imágenes JPG almacenadas en image1
imagenes = [
    'image1.jpg',
    'image2.jpg',
    'image3.jpg',
    'image4.jpg',
    'image5.jpg',
    'image6.jpg',
    'image7.jpg',
    'image8.jpg'
]

#Toma las imagenes de una carpeta en el directorio de la app, debe cambiar el nombre de la carpeta en que desea procesar
imagenes = [f'image1/{nombre}' for nombre in imagenes]

# Convertir todas las imágenes a objetos Image de Pillow y guardarlas en una lista
imagenes_convertidas = []
for imagen in imagenes:
    img = Image.open(imagen)
    # Convertir a RGB en caso de que esté en modo RGBA (para evitar errores)
    if img.mode == 'RGBA':
        img = img.convert('RGB')
    imagenes_convertidas.append(img)

# Guardar la lista de imágenes como un PDF llamado union.pdf
imagenes_convertidas[0].save('union.pdf', save_all=True, append_images=imagenes_convertidas[1:])
