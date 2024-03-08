import qrcode
import streamlit as st

filename = "./qr.png"

def generate_qr_code(url, filename):
    # Crear el objeto QRCode con sus parametros
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    # anadir datos de url a qr
    qr.add_data(url) 
    qr.make(fit=True)

    img = qr.make_image(fill_color='black', back_color="white") # genera la imagen
    img.save(filename) # gguarda la imagen

# Create a streamlit app
st.set_page_config(page_title="QR Code Generator", page_icon="🏿", layout="centered")
st.image("C:\\Users\\enriq\\Documents\\Proyectos LIFI\\PythonProjects\\url_shortener\\image\\banner_luis.png", use_column_width=True)
st.title("QR Code Generator")
url = st.text_input("Enter the URL")

if st.button("Generate QR Code"):
    generate_qr_code(url, filename)
    st.image(filename, use_column_width=True)
    with open(filename, "rb") as f:
        image_data = f.read()
    download = st.download_button(label="Download QR", data=image_data, file_name="qr_generated.png")