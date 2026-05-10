import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Terminal X - Mando Central", layout="wide")

# 2. CABECERA E IDENTIDAD DE MANDO
st.title("🏗️ TERMINAL X: RASCACIELOS GRÁFICO")
st.subheader("Registro Federal: FRN-0038392759")
st.info("Estatus IRS: Vinculado | Supervisión: El Centinela")

# 3. MODELO DE ASCENSO Y OFERTAS (Lógica de Negocio)
st.divider()
st.header("💎 MODELO DE ASCENSO Y PLANES")

col_free, col_pro, col_plat = st.columns(3)

with col_free:
    st.markdown("### 🆓 VERSIÓN FREE")
    st.write("Navegación patrocinada por anunciantes.")
    st.metric("Costo por Anuncio", "$5.00")
    st.success("🎯 REGLA: 50 Anuncios = Ascenso a PLATINO")

with col_pro:
    st.markdown("### 🚀 VERSIÓN PRO")
    st.write("**Incluye Registro de Comercio FCC.**")
    st.write("Vinculación directa con el IRS para comercialización técnica.")
    st.warning("⚡ Afiliación PHELPS TUCKER GROUP = Estatus PLATINO")

with col_plat:
    st.markdown("### 👑 VERSIÓN PLATINO")
    st.write("**Inversionistas Directos - Wall Street.**")
    st.write("Ganancias basadas en la ejecución operativa del imperio.")
    st.info("Auditoría total y transparencia de capital.")

# 4. RESTAURACIÓN DEL MENÚ DE ENLACES (Las Estaciones)
st.divider()
st.header("🛰️ DIRECTORIO DE ESTACIONES OPERATIVAS")
st.write("Seleccione una estación para desplegar el mando:")

# Base de datos de estaciones (Orden Alfabético)
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

# Generación del menú desplegable
for nombre, descripcion in sorted(estaciones.items()):
    with st.expander(f"🔹 {nombre.upper()}"):
        st.write(descripcion)
        # Enlace genérico (sustituir por los específicos si es necesario)
        st.markdown(f"[🔗 Abrir Portal de {nombre}](https://productivity.directory/{nombre.lower().replace(' ', '-')})")

# 5. PIE DE MANDO
st.divider()
st.caption("Fuerza y Honor. Operando bajo Registro Federal 0038392759. Todo sistema está Activo y Normal.")
