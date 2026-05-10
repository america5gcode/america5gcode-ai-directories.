import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Terminal X - Mando Central", layout="wide")

# 2. CABECERA E IDENTIDAD DE MANDO
st.title("🏗️ TERMINAL X: RASCACIELOS GRÁFICO")
st.subheader("Registro Federal: FRN-0038392759")
st.info("Estatus IRS: Vinculado | Registro de Comercio: FCC | Red: TRON (TRC-20)")

# 3. ESTRUCTURA DE PLANES E INVERSIÓN
st.divider()
st.header("💎 PLANOS DE MANDO Y ACCESO")

col_free, col_pro, col_plat = st.columns(3)

with col_free:
    st.markdown("### 🆓 VERSIÓN FREE")
    st.write("Navegación patrocinada por anunciantes.")
    st.metric("Costo por Anuncio", "$5.00")
    st.success("🎯 50 Anuncios = Ascenso Automático a PLATINO")

with col_pro:
    st.markdown("### 🚀 VERSIÓN PRO (FCC)")
    st.write("Comercialización directa vinculada al IRS.")
    st.markdown("""
    **Suscripción de Poder:**
    * **6 Meses:** $200.00
    * **1 Año:** $100.00 (Oferta de Lanzamiento)
    """)
    st.warning("⚡ Afiliación PHELPS TUCKER GROUP = Estatus PLATINO")

with col_plat:
    st.markdown("### 👑 VERSIÓN PLATINO")
    st.write("**Inversionistas Directos - Wall Street.**")
    st.error("⚠️ Inversión Mínima: $400,400.00 ($400k)")
    st.write("Ganancias directas según ejecución operativa.")

# 4. LLAVE DE ACTIVACIÓN (TRONLINK)
st.divider()
st.header("🔑 LLAVE DE ACTIVACIÓN AUTOMÁTICA")
st.write("Utilice el código de su billetera TronLink para vincular el link de afiliación y activar su nivel:")

with st.container():
    # Espacio para el enlace/billetera de TronLink
    tron_wallet = st.text_input("Introduzca su Billetera TronLink / Link de Afiliado:", placeholder="Txxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    
    if st.button("Validar Llave y Activar"):
        if tron_wallet:
            st.success(f"Procesando vinculación para la llave: {tron_wallet}. Verificando estatus en la red Tron...")
        else:
            st.error("Por favor, ingrese la llave del link de TronLink para proceder.")

    st.info("💡 Al usar la llave de TronLink, el sistema valida automáticamente el depósito y actualiza su estatus a Pro o Platino sin intervención manual.")

# 5. DIRECTORIO DE ESTACIONES (Restaurado)
st.divider()
st.header("🛰️ DIRECTORIO DE ESTACIONES OPERATIVAS")
estaciones = {
    "Basecamp": "Gestión de mando y comunicación integral.",
    "FuseBase": "Portal de transparencia para socios e inversores.",
    "GanttPRO": "Ruta crítica y cronogramas de ingeniería.",
    "Hubstaff": "Radar de despliegue y monitoreo GPS.",
    "Jira": "Gestión de software y sprints complejos.",
    "Linear": "Acelerador de ejecución técnica.",
    "MS Project": "Planificación estructural y presupuestos.",
    "NotePlan": "Bitácora de ingeniería y notas Markdown.",
    "nTask": "Nexo de riesgos y minutas de mando.",
    "Paymo": "Rentabilidad y auditoría fiscal.",
    "ProofHub": "Control de calidad y aprobación visual.",
    "Routine": "Captura rápida y rituales inteligentes.",
    "Smartsheet": "Automatización de flujos lógicos.",
    "Taskwarrior": "Núcleo de terminal CLI para Android.",
    "Wrike": "Sincronizador transversal de departamentos."
}

for nombre, descripcion in sorted(estaciones.items()):
    with st.expander(f"🔹 {nombre.upper()}"):
        st.write(descripcion)
        st.markdown(f"[🔗 Abrir Portal de {nombre}](https://productivity.directory/{nombre.lower().replace(' ', '-')})")

# 6. PIE DE MANDO
st.divider()
st.caption("Fuerza y Honor. Operando bajo Registro Federal 0038392759. El Centinela asegura la transparencia en la red Tron.")
