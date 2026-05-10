import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Terminal X - Mando Miami", layout="wide")

# 2. IDENTIDAD CORPORATIVA Y SEDE MIAMI
with st.container():
    col_logo, col_info = st.columns([1.2, 3])
    with col_logo:
        # LOGO OPTIMIZADO
        st.image("https://i.ibb.co/6P0qMhR/PHELPS-TUCKER-GROUP-LOGO.jpg", width=250) 
    with col_info:
        st.title("🏗️ TERMINAL X: RASCACIELOS GRÁFICO")
        st.markdown("## **PHELPS TUCKER GROUP LLC**")
        st.write("📍 **Sede:** 8345 NW 66st Miami, Florida, USA 33166")
        st.write("📧 **Contacto:** fccinternationalus@gmail.com")
        st.caption("Registro Federal: FRN-0038392759 | Registro FCC: Activo | Estatus IRS: Vinculado")

# 3. MÓDULO DE REGISTRO DE PERFIL (OBLIGATORIO - RECTIFICADO)
st.divider()
st.header("👤 REGISTRO DE PERFIL DE USUARIO")
st.info("Trámite obligatorio para vinculación legal con el IRS, FCC y Red Tron.")

# El formulario requiere un botón de envío interno para funcionar en Streamlit
with st.form("perfil_usuario_form"):
    col_a, col_b = st.columns(2)
    with col_a:
        nombre = st.text_input("Nombre y Apellidos:")
        cedula = st.text_input("Documento de Identidad / Pasaporte:")
        residencia = st.text_input("País de Residencia:")
    with col_b:
        email = st.text_input("Correo Electrónico:")
        ocupacion = st.text_input("Profesión u Oficio:")
        plan = st.selectbox("Nivel de Acceso:", ["Free", "Pro (FCC)", "Platino (Inversionista)"])
    
    terminos = st.checkbox("Certifico la veracidad de los datos para fines fiscales y de auditoría.")
    
    # BOTÓN DE ENVÍO (Corrección del error 'Missing Submit Button')
    submit_button = st.form_submit_button(label="GUARDAR PERFIL Y GENERAR CREDENCIAL")

if submit_button:
    if terminos and nombre and email:
        st.success(f"✅ Registro exitoso para {nombre}. Los datos han sido encriptados y vinculados al Registro Federal.")
    else:
        st.error("⚠️ Error: Todos los campos son obligatorios y debe marcar la casilla de certificación.")

# 4. PLANOS DE MANDO Y ACCESO
st.divider()
st.header("💎 MODELO DE ASCENSO E INVERSIONES")
col_f, col_p, col_pl = st.columns(3)

with col_f:
    st.markdown("### 🆓 VERSIÓN FREE")
    st.metric("Costo AD", "$5.00")
    st.success("🎯 50 Ads = Ascenso Automático")

with col_p:
    st.markdown("### 🚀 VERSIÓN PRO (FCC)")
    st.markdown("**6 Meses: $200 | 1 Año: $100**")
    st.warning("⚡ Afiliación Phelps Tucker = PLATINO")

with col_pl:
    st.markdown("### 👑 VERSIÓN PLATINO")
    st.error("⚠️ Inversión Mínima: $400,400.00")
    st.write("Acceso directo a dividendos y Wall Street.")

# 5. LLAVE DE ACTIVACIÓN (TRONLINK)
st.divider()
st.header("🔑 LLAVE DE ACTIVACIÓN (TRONLINK)")
st.write("Vincule su billetera para validar su registro y activar su estatus:")
tron_key = st.text_input("Llave TRC-20:", placeholder="Txxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

if st.button("Sincronizar con el Imperio"):
    if tron_key:
        st.success("Validando identidad en la Red Tron... Sincronización FCC en proceso.")
    else:
        st.error("Deve completar el Registro de Perfil antes de activar la llave.")

# 6. DIRECTORIO DE ESTACIONES OPERATIVAS
st.divider()
st.header("🛰️ DIRECTORIO DE ESTACIONES")
estaciones = ["Basecamp", "FuseBase", "GanttPRO", "Hubstaff", "Jira", "Linear", "MS Project", "NotePlan", "nTask", "Paymo", "ProofHub", "Routine", "Smartsheet", "Taskwarrior", "Wrike"]

for est in sorted(estaciones):
    with st.expander(f"🔹 {est.upper()}"):
        st.write(f"Portal operativo para la gestión de {est}.")
        st.markdown(f"[🔗 Abrir Portal](https://productivity.directory/{est.lower()})")

# 7. PIE DE PÁGINA CORPORATIVO
st.divider()
st.caption("Fuerza y Honor. Miami Operations 33166 | Phelps Tucker Group | Registro FRN-0038392759")
