import os
from pathlib import Path
import streamlit as st

st.set_page_config(layout="wide")

# Obtener la ruta absoluta del directorio donde se encuentra este archivo app.py
BASE_DIR = Path(__file__).resolve().parent

# Construir la ruta absoluta hacia el archivo HTML
html_file_path = BASE_DIR / "web" / "index.html"

# Verificar que el archivo exista antes de abrirlo
if html_file_path.exists():
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    st.components.v1.html(html_content, height=800, scrolling=True)
else:
    st.error(f"No se encontró el archivo HTML en la ruta: {html_file_path}")
