import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Terminal X - Mando Miami", layout="wide")

# 2. IDENTIDAD CORPORATIVA
with st.container():
    col_logo, col_info = st.columns([1.2, 3])
    with col_logo:
        # Logo oficial restaurado
        st.image("https://i.ibb.co/6P0qMhR/PHELPS-TUCKER-GROUP-LOGO.jpg", width=250) 
    with col_info:
        st.title("🏗️ TERMINAL X: RASCACIELOS GRÁFICO")
        st.markdown("## **PHELPS TUCKER GROUP LLC**")
        st.write("📍 **Sede:** 8345 NW 66st Miami, Florida, USA 33166")
        st.write("📧 **Contacto:** fccinternationalus@gmail.com")
        st.caption("Registro Federal: FRN-0038392759 | Registro FCC Activo")

# 3. MÓDULO DE REGISTRO DE PERFIL (OBLIGATORIO)
st.divider()
st.header("👤 REGISTRO DE PERFIL DE USUARIO (REQUISITO OBLIGATORIO)")
st.info("Este registro es indispensable para la vinculación con el IRS, la FCC y la red Tron.")

with st.form("registro_usuario"):
    col_a, col_b = st.columns(2)
    with col_a:
        nombre_completo = st.text_input("Nombre y Apellidos Reales:")
        documento_id = st.text_input("Documento de Identidad (ID/Pasaporte):")
        pais_residencia = st.text_input("País de Residencia:")
    with col_b:
        correo_personal = st.text_input("Correo Electrónico de Contacto:")
        profesion_oficio = st.text_input("Profesión / Cargo:")
        nivel_interes = st.selectbox("Nivel de Interés:", ["Free", "Pro (FCC)", "Platino (Inversionista)"])
    
    confirmacion = st.checkbox("Certifico que los datos proporcionados son veraces para fines legales y fiscales.")
    
    submit_registro = st.form_submit_with_button("Guardar Perfil y Generar Credencial")

if submit_registro:
    if confirmacion and nombre_completo and correo_personal:
        st.success(f"✅ Perfil de {nombre_completo} registrado exitosamente. Procesando credencial para el Registro Federal.")
    else:
        st.error("⚠️ Error: Todos los campos son obligatorios y debe certificar la veracidad de los datos.")

# 4. PLANOS DE MANDO Y ACCESO
st.divider()
st.header("💎 MODELO DE ASCENSO E INVERSIONES")
col_f, col_p, col_pl = st.columns(3)

with col_f:
    st.markdown("### 🆓 VERSIÓN FREE")
    st.metric("Costo AD", "$5.00")
    st.success("🎯 50 Ads = Ascenso a PLATINO")

with col_p:
    st.markdown("### 🚀 VERSIÓN PRO (FCC)")
    st.markdown("**6 Meses: $200 | 1 Año: $100**")
    st.warning("⚡ Afiliación Phelps Tucker = PLATINO")

with col_pl:
    st.markdown("### 👑 VERSIÓN PLATINO")
    st.error("⚠️ Inversión Mínima: $400,400.00")
    st.write("Acceso directo a Wall Street.")

# 5. ACTIVACIÓN VÍA TRONLINK (VINCULADA AL PERFIL)
st.divider()
st.header("🔑 LLAVE DE ACTIVACIÓN (TRONLINK)")
st.write("Ingrese la llave de su link para validar el registro y activar su estatus:")
tron_key = st.text_input("Llave TRC-20:", placeholder="Txxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

if st.button("Sincronizar Perfil y Activar"):
    if tron_key:
        st.success("Sincronizando identidad con la Red Tron... Activación en proceso.")
    else:
        st.error("Debe registrar su perfil antes de activar la llave.")

# 6. DIRECTORIO DE ESTACIONES
st.divider()
st.header("🛰️ DIRECTORIO DE ESTACIONES")
estaciones = ["Basecamp", "FuseBase", "GanttPRO", "Hubstaff", "Jira", "Linear", "MS Project", "NotePlan", "nTask", "Paymo", "ProofHub", "Routine", "Smartsheet", "Taskwarrior", "Wrike"]
for est in sorted(estaciones):
    with st.expander(f"🔹 {est.upper()}"):
        st.write(f"Acceso operativo a la estación {est}.")
        st.markdown(f"[🔗 Abrir Portal](https://productivity.directory/{est.lower()})")

# 7. PIE DE PÁGINA
st.divider()
st.caption("Fuerza y Honor. Miami Operations | Registro FRN-0038392759")
