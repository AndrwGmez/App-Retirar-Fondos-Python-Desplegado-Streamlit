import streamlit as st
from PIL import Image
import os

# Título de la aplicación
st.title("Convertir Formatos de Imágenes")

# Instrucciones
st.write("Sube una imagen y selecciona el formato al que deseas convertirla.")

# Subir imagen
uploaded_file = st.file_uploader("Elige una imagen", type=["png", "jpg", "jpeg", "bmp", "tiff", "gif"])

# Seleccionar el formato de salida
format_options = ["PNG", "JPEG", "BMP", "TIFF", "GIF"]
output_format = st.selectbox("Selecciona el formato de salida", format_options)

# Botón para convertir la imagen
if st.button("Convertir"):
    if uploaded_file is not None:
        # Abrir la imagen
        image = Image.open(uploaded_file)

        # Crear nombre de archivo para la imagen convertida
        output_filename = os.path.splitext(uploaded_file.name)[0] + f".{output_format.lower()}"

        # Convertir la imagen
        image = image.convert("RGB")
        image.save(output_filename, output_format)

        # Mostrar la imagen convertida
        st.image(image, caption=f"Imagen en formato {output_format}", use_column_width=True)

        # Descargar la imagen convertida
        with open(output_filename, "rb") as file:
            st.download_button(
                label="Descargar Imagen Convertida",
                data=file,
                file_name=output_filename,
                mime=f"image/{output_format.lower()}"
            )

        # Limpiar el archivo después de la descarga
        os.remove(output_filename)
    else:
        st.error("Por favor, sube una imagen primero.")
