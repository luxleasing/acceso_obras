from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="LUXVision | Visor de tramo",
    layout="wide",
    initial_sidebar_state="collapsed"
)

BASE_DIR = Path(__file__).resolve().parent
html_file_path = BASE_DIR / "index.html"

st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"] { background: #101315; }
[data-testid="stHeader"] { display: none; }
.block-container { padding: 0 !important; max-width: 100% !important; }
iframe { display: block; }
</style>
""", unsafe_allow_html=True)

if html_file_path.exists():
    html_content = html_file_path.read_text(encoding="utf-8")
    st.components.v1.html(html_content, height=900, scrolling=False)
else:
    st.error(f"No se encontró index.html en: {html_file_path}")
