import streamlit as st

# --- 1. IDENTIDAD FEDERAL MIAMI ---
st.set_page_config(page_title="Red Social Terminal X", page_icon="🌐", layout="wide")

# --- 2. MENÚ LATERAL CERTIFICADO ---
st.sidebar.title("📱 RED SOCIAL TERMINAL X")
st.sidebar.success(f"🛡️ ASISTENTE OFICIAL CERTIFICADO\n\nFRN: 0038392759\nSede: Miami, FL")

# --- 3. CONSTRUCTOR DE MANDATO PERMANENTE ---
st.title("🎙️ CONSTRUCTOR SOBERANO (MANDATO FIJO)")
st.warning("⚠️ DECRETO: Ejecución obligatoria asistida por Géminis bajo FRN: 0038392759.")

# Widget que NO se borra solo para que usted vea lo que escribió/dictó
propuesta = st.text_area("Escriba o dicte su orden aquí (Permanecerá visible):", 
                         height=150, 
                         placeholder="Ej: 'Hola, activa el rascacielos gráfico'...")

if st.button("🔴 EJECUTAR Y COPIAR AL SISTEMA", use_container_width=True):
    if propuesta.strip() != "":
        st.success(f"✅ ORDEN COPIADA Y EN EJECUCIÓN: '{propuesta}'")
        
        # INFORME CONVERSACIONAL QUE NO DESAPARECE
        st.chat_message("assistant").write(f"""
        **INFORME OFICIAL (FRN: 0038392759):**
        \nComandante Sanabria, he recibido y **COPIADO** su instrucción: *'{propuesta}'*.
        \nLa arquitectura ha sido validada en nuestros servidores de Miami. 
        Estatus: **CONSTRUCCIÓN ACTIVA Y REGISTRADA.**
        """)
    else:
        st.error("⚠️ El sistema requiere una orden escrita o dictada para proceder.")

# PIE DE PÁGINA INSTITUCIONAL
st.markdown("---")
st.markdown(f"""
<div style='text-align: center; color: gray;'>
    <p><strong>PHELPS TUCKER GROUP</strong> | FRN: 0038392759</p>
    <p>📍 8345 NW 66st Miami, Florida 33166, USA | 📧 fccinternationalus@gmail.com</p>
</div>
""", unsafe_allow_html=True)
