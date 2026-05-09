import streamlit as st

# 1. IDENTIDAD FEDERAL MIAMI ---
st.set_page_config(page_title="Terminal X - Red Social", layout="wide")

# 2. MENÚ LATERAL CON ENLACES SOBERANOS
st.sidebar.title("🛡️ RED SOCIAL TERMINAL X")
st.sidebar.success("✅ REGISTRO FEDERAL: 0038392759")

st.sidebar.markdown("---")
st.sidebar.subheader("📥 DESCARGAS SOBERANAS")

# Enlaces RAW extraídos de su repositorio
st.sidebar.markdown("[🚀 Descargar main.py](https://github.com/america5gcode/TerminalX/raw/main/main.py)")
st.sidebar.markdown("[📜 Ver Documentación (README)](https://github.com/america5gcode/TerminalX/raw/main/README.md)")
st.sidebar.markdown("[📦 Librerías Necesarias](https://github.com/america5gcode/TerminalX/raw/main/requirements.txt)")

# 3. CONSTRUCTOR DE RESPUESTA CON ENLACES
st.title("🏙️ RED SOCIAL TERMINAL X")
st.warning("⚠️ DECRETO: Distribución de activos autorizada bajo FRN: 0038392759")

propuesta = st.text_area("Dicte su instrucción (ej: 'Dame los enlaces'):")

if st.button("🔴 EJECUTAR Y OBTENER ACCESOS"):
    if propuesta.strip() != "":
        st.markdown("---")
        with st.chat_message("assistant"):
            st.write(f"**🛡️ INFORME DE DISTRIBUCIÓN FEDERAL**")
            
            # Lógica para entregar enlaces según la instrucción
            if "enlace" in propuesta.lower() or "acceso" in propuesta.lower():
                st.info("✅ **ACCESOS CONCEDIDOS POR EL COMANDANTE**")
                st.write("- **Repositorio Principal:** https://github.com/america5gcode/TerminalX")
                st.write("- **Archivo de Ejecución:** https://github.com/america5gcode/TerminalX/raw/main/main.py")
                st.success("La veracidad de este rascacielos es absoluta.")
            else:
                st.write(f"Instrucción '{propuesta}' procesada. El sistema está normal.")
    else:
        st.error("⚠️ El núcleo requiere una instrucción válida para operar.")
