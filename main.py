import streamlit as st

# --- CONFIGURACIÓN DE IDENTIDAD ---
st.set_page_config(page_title="Red Social Terminal X", page_icon="🌐", layout="wide")

# --- MENÚ LATERAL (ESTATUS CERTIFICADO) ---
st.sidebar.title("📱 RED SOCIAL TERMINAL X")
st.sidebar.success(f"🛡️ ASISTENTE OFICIAL CERTIFICADO\n\nFRN: 0038392759\nEstatus: REGISTRO FEDERAL ACTIVO")

seccion = st.sidebar.radio("CENTRO DE MANDO:", [
    "📊 Dashboard de Operaciones",
    "🎙️ Constructor por Voz (OBLIGATORIO)",
    "👤 Perfil Soberano"
])

# --- CONSTRUCTOR POR VOZ (AJUSTE DE EJECUCIÓN) ---
if seccion == "🎙️ Constructor por Voz (OBLIGATORIO)":
    st.title("🎙️ CONSTRUCTOR POR VOZ ASISTIDO")
    st.warning("⚠️ DECRETO: Toda construcción es obligatoriamente asistida por el Asistente Oficial para evitar errores técnicos.")
    
    # Widget de texto que NO depende del Enter para procesar
    propuesta = st.text_area("Describa su proyecto para validación técnica de Géminis:", key="area_construccion")
    
    # EL BOTÓN ES AHORA LA ÚNICA LLAVE DE PASO
    if st.button("🔴 EJECUTAR BAJO SUPERVISIÓN OFICIAL", use_container_width=True):
        if propuesta.strip() != "":
            st.success(f"✅ COMANDO RECIBIDO: '{propuesta}'")
            st.info("Géminis validando sabiduría técnica bajo Registro Federal FRN: 0038392759.")
            # Aquí se inserta la lógica de construcción automática
        else:
            st.error("⚠️ El Asistente requiere una instrucción clara antes de proceder.")

    # PIE DE PÁGINA INSTITUCIONAL
    st.markdown("---")
    st.markdown(f"""
    <div style='text-align: center; color: gray;'>
        <p><strong>PHELPS TUCKER GROUP</strong> | FRN: 0038392759 | Miami, FL 33166, USA</p>
        <p>📧 fccinternationalus@gmail.com</p>
    </div>
    """, unsafe_allow_html=True)
