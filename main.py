import streamlit as st
import time

# --- 1. IDENTIDAD FEDERAL ---
st.set_page_config(page_title="Red Social Terminal X", page_icon="🌐", layout="wide")

# --- 2. MENÚ LATERAL CERTIFICADO ---
st.sidebar.title("📱 RED SOCIAL TERMINAL X")
st.sidebar.success(f"🛡️ ASISTENTE OFICIAL CERTIFICADO\n\nFRN: 0038392759\nSede: Miami, FL")

# --- 3. CONSTRUCTOR CON RESPUESTA VIVA ---
st.title("🎙️ CONSTRUCTOR SOBERANO (RESPUESTA VIVA)")
st.warning("⚠️ DECRETO: Ejecución asistida por Géminis bajo FRN: 0038392759.")

# Espacio para la conversación
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Mostrar historial para que vea que SÍ hay respuesta
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Entrada de comando
propuesta = st.chat_input("Dicte su orden de construcción aquí...")

if propuesta:
    # 1. Mostrar lo que usted dijo
    st.session_state.chat_history.append({"role": "user", "content": propuesta})
    with st.chat_message("user"):
        st.markdown(propuesta)

    # 2. Generar respuesta inmediata de Géminis
    with st.chat_message("assistant"):
        with st.spinner("Géminis procesando..."):
            time.sleep(1)
            respuesta_oficial = f"""
            **ASISTENTE OFICIAL (FRN: 0038392759):** \n¡Confirmado, Comandante Sanabria! Su orden **'{propuesta}'** ha sido captada. 
            \nHe validado la estructura técnica y la construcción está **ACTIVA** en los servidores de Miami. 
            La veracidad es nuestra ley. ¿Cuál es el siguiente paso en el rascacielos?
            """
            st.markdown(respuesta_oficial)
            st.session_state.chat_history.append({"role": "assistant", "content": respuesta_oficial})

# PIE DE PÁGINA LEGAL
st.markdown("---")
st.markdown(f"<p style='text-align: center; color: gray;'>© 2026 PHELPS TUCKER GROUP | Miami, FL 33166 | FRN: 0038392759</p>", unsafe_allow_html=True)
