import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Terminal X - Mando Central", layout="wide")

# 2. CABECERA E IDENTIDAD DE MANDO
st.title("🏗️ TERMINAL X: RASCACIELOS GRÁFICO")
st.subheader("Registro Federal: FRN-0038392759")
st.info("Estatus IRS: Vinculado | Registro de Comercio: FCC | Supervisión: El Centinela")

# 3. MODELO DE NEGOCIO Y PLANES DE INVERSIÓN
st.divider()
st.header("💎 ESTRUCTURA DE PLANES Y OFERTAS")

col_free, col_pro, col_plat = st.columns(3)

with col_free:
    st.markdown("### 🆓 VERSIÓN FREE")
    st.write("Exploración total patrocinada por anunciantes.")
    st.metric("Costo por Anuncio", "$5.00")
    st.success("🎯 REGLA: 50 Anuncios = Ascenso a PLATINO")

with col_pro:
    st.markdown("### 🚀 VERSIÓN PRO (FCC)")
    st.write("Comercialización directa vinculada al IRS.")
    st.markdown("""
    **Oferta Oficial:**
    * **6 Meses:** $200.00
    * **1 Año:** $100.00 (Promoción especial)
    """)
    st.warning("⚡ Afiliación PHELPS TUCKER GROUP = Estatus PLATINO")

with col_plat:
    st.markdown("### 👑 VERSIÓN PLATINO")
    st.write("**Inversionistas Directos - Wall Street.**")
    st.error("⚠️ Inversión Mínima: $400,000.00 ($400k)")
    st.write("Ganancias directas según ejecución operativa.")
    st.info("Transparencia total para el Grupo de Inversores.")

# 4. PASARELA DE DEPÓSITO (Datos de Cuenta)
st.divider()
with st.expander("💳 DATOS PARA DEPÓSITO Y ACTIVACIÓN"):
    st.write("Para activar su Versión Pro o Platino, realice el depósito en la siguiente cuenta:")
    # Aquí puedes rellenar con tus datos bancarios reales
    st.code("""
    Institución: [BANCO DE VENEZUELA / OTRO]
    Cuenta: [INSERTAR NÚMERO DE CUENTA AQUÍ]
    Beneficiario: PHELPS TUCKER GROUP
    Referencia: [Nombre de Usuario / ID Terminal X]
    """, language="text")
    st.caption("Una vez realizado el depósito, su cuenta pasará automáticamente al nivel correspondiente.")

# 5. DIRECTORIO DE ESTACIONES (Restaurado)
st.divider()
st.header("🛰️ DIRECTORIO DE ESTACIONES OPERATIVAS")
estaciones = {
    "Basecamp": "Búnker de comunicación integral y gestión de mando.",
    "FuseBase": "Portal de transparencia para socios e inversores.",
    "GanttPRO": "Visualización de ruta crítica y cronogramas de ingeniería.",
    "Hubstaff": "Radar de despliegue y monitoreo de actividad por GPS.",
    "Jira": "Gestión de software y sprints de alta complejidad.",
    "Linear": "Acelerador de ejecución y resolución técnica de issues.",
    "MS Project": "Central de planificación estructural y presupuestos.",
    "NotePlan": "Bitácora de ingeniería y organización de tareas en Markdown.",
    "nTask": "Nexo multi-dimensional para riesgos y minutas de mando.",
    "Paymo": "Central de rentabilidad, facturación y auditoría fiscal.",
    "ProofHub": "Control de calidad y aprobación visual de interfaces.",
    "Routine": "Nexo inteligente para captura rápida de ideas y rituales.",
    "Smartsheet": "Automatización de flujos operativos y tableros lógicos.",
    "Taskwarrior": "Núcleo de terminal para gestión de tareas desde CLI.",
    "Wrike": "Sincronizador transversal para unificación de departamentos."
}

for nombre, descripcion in sorted(estaciones.items()):
    with st.expander(f"🔹 {nombre.upper()}"):
        st.write(descripcion)
        st.markdown(f"[🔗 Abrir Portal de {nombre}](https://productivity.directory/{nombre.lower().replace(' ', '-')})")

# 6. PIE DE MANDO
st.divider()
st.caption("Fuerza y Honor. Operando bajo Registro Federal 0038392759. Todo sistema está Activo y Normal.")
