import streamlit as st

st.set_page_config(layout="wide")

# Cambiar "index.html" por "web/index.html"
with open("web/index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

st.components.v1.html(html_content, height=800, scrolling=True)
