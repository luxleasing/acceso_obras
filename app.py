from pathlib import Path
import streamlit as st

st.set_page_config(layout="wide")

# Obtener la ruta del directorio raíz del repositorio
BASE_DIR = Path(__file__).resolve().parent

# Apuntar directamente a index.html en la raíz
html_file_path = BASE_DIR / "index.html"

if html_file_path.exists():
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    st.components.v1.html(html_content, height=800, scrolling=True)
else:
    st.error(f"No se encontró index.html en: {html_file_path}")
