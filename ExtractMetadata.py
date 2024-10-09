from PIL import Image
from PIL.ExifTags import TAGS
import os

def extract_metadata(file_path):
    try:
        with Image.open(file_path) as img:
            exif_data = img._getexif()

        if exif_data is None:
            print(f"No se encontraron metadatos EXIF en {file_path}")
            return

        print(f"Metadatos para {file_path}:")
        for tag_id, value in exif_data.items():
            tag = TAGS.get(tag_id, tag_id)
            if isinstance(value, bytes):
                value = value.decode()
            print(f"{tag:25}: {value}")

    except IOError:
        print(f"No se pudo abrir el archivo: {file_path}")
    except Exception as e:
        print(f"Error al procesar {file_path}: {str(e)}")

# Ruta del archivo
file_path = "C:/Users/ismae/OneDrive/Imágenes/Pruebas/cor.jpg"

# Verificar si el archivo existe
if os.path.exists(file_path):
    extract_metadata(file_path)
else:
    print(f"El archivo no existe: {file_path}")