import streamlit as st

# 1. CONFIGURACIÓN DEL RASCACIELOS
st.set_page_config(page_title="Terminal X - Red Social", layout="wide")

# 2. BARRA LATERAL CON ENLACES SOBERANOS
st.sidebar.title("🛡️ TERMINAL X")
st.sidebar.subheader("📥 DESCARGAS FEDERALES")

# AQUÍ PEGAMOS EL ENLACE QUE USTED CONSIGUIÓ
("[🚀 Descargar main.py](https://github.com/america5gcode/TerminalX/raw/main/main.py)")
st.sidebar.markdown("[📜 Ver Documentación](https://github.com/america5gcode/TerminalX/raw/main/README.md)")

# 3. INTERFAZ PRINCIPAL
st.title("🏙️ RED SOCIAL TERMINAL X")
st.write("Bienvenido al centro de mando de la Inteligencia Dinamita.")
st.info("Utilice la barra lateral para descargar los activos del sistema.")
