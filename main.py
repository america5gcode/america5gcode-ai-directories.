import streamlit as st

# 1. IDENTIDAD FEDERAL MIAMI ---
st.set_page_config(page_title="Terminal X - Red Social", layout="wide")

# 2. MENÚ LATERAL CON ENLACES SOBERANOS
st.sidebar.title("🛡️ RED SOCIAL TERMINAL X")
st.sidebar.success("✅ REGISTRO FEDERAL: 0038392759")

st.sidebar.markdown("---")
st.sidebar.subheader("📥 DESCARGAS SOBERANAS")

# Enlaces de archivos
st.sidebar.markdown("[🚀 Descargar main.py](https://github.com/america5gcode/TerminalX/raw/main/main.py)")
st.sidebar.markdown("[📜 Ver Documentación](https://github.com/america5gcode/TerminalX/raw/main/README.md)")
st.sidebar.markdown("[📦 Librerías Necesarias](https://github.com/america5gcode/TerminalX/raw/main/requirements.txt)")

st.sidebar.markdown("---")
st.sidebar.subheader("🌐 PÁGINAS DEL IMPERIO")
# Aquí coloca los enlaces directos a sus otras webs
st.sidebar.markdown("[🏢 Directorio AI](https://america5gcode-ai-directories-67bv.onrender.com)")
st.sidebar.markdown("[🏢 Directorio AI](https://america5gcode-ai-directories.onrender.com)")
# 3. INTERFAZ PRINCIPAL
st.title("🏙️ RED SOCIAL TERMINAL X")
st.warning("⚠️ DECRETO: Distribución de activos autorizada bajo FRN: 0038392759")

propuesta = st.text_area("Dicte su instrucción (ej: 'Dame los enlaces'):")

if st.button("🔴 EJECUTAR Y OBTENER ACCESOS"):
    if propuesta.strip() != "":
        st.markdown("---")
        with st.chat_message("assistant"):
            st.write("**🛡️ INFORME DE DISTRIBUCIÓN FEDERAL**")
            if "enlace" in propuesta.lower() or "acceso" in propuesta.lower():
                st.info("✅ **ACCESOS CONCEDIDOS POR EL COMANDANTE**")
                st.write("- **Repositorio:** https://github.com/america5gcode/TerminalX")
                st.success("La veracidad es arquitectura: El rascacielos es real.")
            else:
                st.write(f"Instrucción '{propuesta}' procesada. Todo está normal.")
    else:
        st.error("⚠️ El núcleo requiere una instrucción para operar.")
