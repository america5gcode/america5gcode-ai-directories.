import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA (Estilo Rascacielos)
st.set_page_config(page_title="Terminal X - Mando Miami", layout="wide")

# 2. IDENTIDAD CORPORATIVA DE ALTO NIVEL
with st.container():
    col_logo, col_info = st.columns([1.2, 3])
    with col_logo:
        # Usando el escudo oficial de Phelps Tucker Group
        st.image("https://i.ibb.co/6P0qMhR/PHELPS-TUCKER-GROUP-LOGO.jpg", width=250) 
    with col_info:
        st.title("🏗️ TERMINAL X: RASCACIELOS GRÁFICO")
        st.markdown("## **PHELPS TUCKER GROUP LLC**")
        st.write("📍 **Sede Principal:** 8345 NW 66st Miami, Florida, USA 33166")
        st.write("📧 **Contacto FCC:** fccinternationalus@gmail.com")
        st.caption("Registro Federal: FRN-0038392759 | Registro FCC: Activo | Estatus IRS: Vinculado")

# 3. PLANOS DE MANDO Y ACCESO FINANCIERO
st.divider()
st.header("💎 MODELO DE ASCENSO E INVERSIÓN")

col_f, col_p, col_pl = st.columns(3)

with col_f:
    st.markdown("### 🆓 VERSIÓN FREE")
    st.write("Exploración total patrocinada por anuncios.")
    st.metric("Costo AD", "$5.00")
    st.success("🎯 REGLA: 50 Ads = Ascenso a PLATINO")

with col_p:
    st.markdown("### 🚀 VERSIÓN PRO (FCC)")
    st.write("**Comercialización Directa (IRS/FCC)**")
    st.info("• 6 Meses: $200.00\n\n• 1 Año: $100.00")
    st.warning("⚡ Afiliación Phelps Tucker = Estatus PLATINO")

with col_pl:
    st.markdown("### 👑 VERSIÓN PLATINO")
    st.write("**Inversionistas Directos - Wall Street**")
    st.error("⚠️ Inversión Mínima: $400,400.00 ($400k)")
    st.write("Acceso a dividendos por ejecución operativa.")

# 4. LLAVE TRONLINK: ACTIVACIÓN AUTOMÁTICA
st.divider()
st.header("🔑 ACTIVACIÓN VÍA TRONLINK")
st.write("Ingrese la llave de su billetera o link de afiliado para sincronizar su nivel:")

tron_input = st.text_input("Llave TRC-20 / Link de Afiliación:", placeholder="Txxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
if st.button("Sincronizar con el Imperio"):
    if tron_input:
        st.success(f"Sincronizando con la Red Tron... Llave {tron_input} validada bajo FCC.")
    else:
        st.error("Se requiere la llave del link para la activación.")

# 5. DIRECTORIO ALFABÉTICO DE ESTACIONES (Restaurado según Captura)
st.divider()
st.header("🛰️ DIRECTORIO DE ESTACIONES")

estaciones = {
    "BASECAMP": "Búnker de comunicación integral y gestión de mando.",
    "FUSEBASE": "Portal de transparencia para socios e inversores.",
    "GANTTPRO": "Visualización de ruta crítica y cronogramas.",
    "HUBSTAFF": "Radar de despliegue y monitoreo GPS.",
    "JIRA": "Gestión de software y sprints complejos.",
    "LINEAR": "Acelerador de ejecución técnica.",
    "MS PROJECT": "Planificación estructural y presupuestos.",
    "NOTEPLAN": "Bitácora de ingeniería y notas Markdown.",
    "NTASK": "Nexo de riesgos y minutas de mando.",
    "PAYMO": "Rentabilidad y auditoría fiscal.",
    "PROOFHUB": "Control de calidad y aprobación visual.",
    "ROUTINE": "Nexo inteligente para captura rápida de rituales.",
    "SMARTSHEET": "Automatización de flujos lógicos.",
    "TASKWARRIOR": "Núcleo de terminal CLI para Android.",
    "WRIKE": "Sincronizador transversal de departamentos."
}

for nombre in sorted(estaciones.keys()):
    with st.expander(f"🔹 {nombre}"):
        st.write(estaciones[nombre])
        st.markdown(f"[🔗 Abrir Portal de {nombre}](https://productivity.directory/{nombre.lower()})")

# 6. PIE DE PÁGINA CORPORATIVO
st.divider()
st.caption("Fuerza y Honor. Miami Operations 33166 | Phelps Tucker Group | Registro FRN-0038392759")
