import streamlit as st
import pandas as pd # Para manejar la base de datos interna

# 1. CONFIGURACIÓN
st.set_page_config(page_title="Terminal X - Registro Miami", layout="wide")

# 2. CABECERA CORPORATIVA
col_logo, col_info = st.columns([1.2, 3])
with col_logo:
    st.image("https://i.ibb.co/6P0qMhR/PHELPS-TUCKER-GROUP-LOGO.jpg", width=250) 
with col_info:
    st.title("🏗️ TERMINAL X: RASCACIELOS GRÁFICO")
    st.write("📍 **Sede:** 8345 NW 66st Miami, Florida, USA 33166")
    st.write("📧 **Correo Oficial:** fccinternationalus@gmail.com")

st.divider()

# 3. FORMULARIO CON REDIRECCIÓN DE DATOS
st.header("👤 REGISTRO OBLIGATORIO DE SOCIOS")
st.info("Al completar este formulario, la información se enviará al Centro de Mando en Miami.")

with st.form("perfil_usuario_final"):
    col_a, col_b = st.columns(2)
    with col_a:
        nombre = st.text_input("Nombre Completo:")
        id_user = st.text_input("ID / Pasaporte:")
    with col_b:
        email_user = st.text_input("Correo Electrónico:")
        plan_elegido = st.selectbox("Plan:", ["Free", "Pro (FCC)", "Platino ($400k)"])
    
    # Checkbox de certificación legal
    certifico = st.checkbox("Certifico la veracidad de los datos ante PHELPS TUCKER GROUP.")
    
    submit = st.form_submit_button("ENVIAR REGISTRO A MIAMI")

if submit:
    if certifico and nombre and email_user:
        # LOGICA DE ENVÍO (Simulación de Backend)
        st.success(f"🚀 ¡REGISTRO ENVIADO! Los datos de {nombre} están siendo procesados por fccinternationalus@gmail.com.")
        
        # Aquí se integraría la API de correo o Google Sheets
        st.balloons() 
    else:
        st.error("⚠️ Error: Debe completar los campos y certificar la veracidad.")

st.divider()

# 4. LLAVE DE ACTIVACIÓN TRONLINK
st.header("🔑 VINCULACIÓN TRONLINK (LLAVE MAESTRA)")
tron_key = st.text_input("Introduzca su llave para activar su nivel automáticamente:")
if st.button("Sincronizar con el Registro Federal"):
    st.info("Sincronizando perfil registrado con la red Tron...")

# 5. PIE DE PÁGINA
st.caption("Fuerza y Honor. Operación Miami | Registro Federal: FRN-0038392759")
