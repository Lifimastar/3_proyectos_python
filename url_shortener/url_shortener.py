import pyshorteners
import streamlit as st

def shorten_url(url):
    # Funcion que pasame las url a acortar
    s = pyshorteners.Shortener() # objeto de pyshorteners
    shortened_url = s.tinyurl.short(url) # acortar url
    return shortened_url # url acortada

# creamos app web con streamlit
st.set_page_config(page_title="URL Shortener", page_icon="/", layout="centered") # configurar pagina
st.image(image="image/banner_luis.png") # imagen
st.title("URL Shortener") # titulo
url = st.text_input("Enter the url") # url a insertar
if st.button("Generate new URL"): # si se presiona el boton:
    st.write("URL shortened: ", shorten_url(url)) # devuelve

