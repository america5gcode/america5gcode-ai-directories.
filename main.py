import streamlit as st

# 1. CONFIGURACIÓN ESTRUCTURAL
st.set_page_config(page_title="Terminal X - Centro de Mando", layout="wide")

# 2. CABECERA DEL IMPERIO (Registro Federal)
st.title("🏗️ RASCACIELOS GRÁFICO: TERMINAL X")
st.subheader("Registro Federal: FRN-0038392759")
st.info("Estatus Operativo: Activo y Normal | Supervisión: El Centinela")

# 3. PÁGINA 1620: MANIFIESTO E IDENTIDAD
st.divider()
st.markdown("## 📟 PÁGINA 1620: ¿QUIÉNES SOMOS Y QUÉ HACEMOS?")
col_id1, col_id2 = st.columns([1, 2])
with col_id1:
    st.image("https://img.icons8.com/wired/512/84cc16/building-stats.png", width=150)
with col_id2:
    st.write("""
    **Somos lo que hacemos:** Arquitectos de soluciones móviles de alta fidelidad, operando desde el núcleo 
    Android/Termux. Nuestra oferta se basa en la eliminación de bardas administrativas y la 
    aceleración de activos hacia los mercados globales.
    """)

# 4. LÓGICA DE PLANES Y OFERTAS (Modelo de Ascenso)
st.divider()
st.markdown("### 💎 PLANOS DE MANDO Y CONVERSIÓN")

col_plan1, col_plan2, col_plan3 = st.columns(3)

with col_plan1:
    st.markdown("#### 🆓 VERSIÓN FREE")
    st.write("Navegación patrocinada por anunciantes.")
    st.metric("Costo por AD", "$5.00")
    st.caption("🎯 REGLA DE ORO: 50 Anuncios = Ascenso Automático a PLATINO.")

with col_plan2:
    st.markdown("#### 🚀 VERSIÓN PRO")
    st.write("Exclusión del Registro FSCC de Marketing Digital.")
    st.write("Vínculo directo con el **IRS** para comercialización.")
    st.success("Afiliación Grupo First = Estándar Platino.")

with col_plan3:
    st.markdown("#### 👑 VERSIÓN PLATINO")
    st.write("Inversionistas directos. Destino: **Wall Street**.")
    st.write("Ganancias según ejecución y dividendos del imperio.")

# 5. MENÚ DE DESPLIEGUE: LAS 32 ESTACIONES (Orden Alfabético)
st.divider()
st.markdown("### 🛰️ DIRECTORIO ALFABÉTICO DE ESTACIONES (EL ASADO)")

# Diccionario maestro de estaciones
estaciones = {
    "Basecamp": {"desc": "Búnker de comunicación integral libre de ruido.", "url": "https://productivity.directory/basecamp"},
    "FuseBase": {"desc": "Portal de transparencia para socios e inversores.", "url": "https://productivity.directory/fusebase"},
    "GanttPRO": {"desc": "Refinería de cronogramas y visualización de dependencias.", "url": "https://productivity.directory/ganttpro"},
    "Hubstaff": {"desc": "Radar de despliegue, GPS y monitoreo de actividad real.", "url": "https://productivity.directory/hubstaff"},
    "Jira": {"desc": "Sala de ingeniería pesada para gestión ágil de software.", "url": "https://productivity.directory/jira"},
    "Linear": {"desc": "Acelerador de sprints con velocidad de respuesta extrema.", "url": "https://productivity.directory/linear"},
    "MS Project": {"desc": "Central de planificación estructural y ruta crítica.", "url": "https://productivity.directory/microsoft-project"},
    "NotePlan": {"desc": "Bitácora de ingeniería en Markdown y tareas diarias.", "url": "https://productivity.directory/noteplan"},
    "nTask": {"desc": "Nexo multi-dimensional para riesgos y presupuestos.", "url": "https://productivity.directory/ntask"},
    "Paymo": {"desc": "Central de rentabilidad, facturación y auditoría IRS.", "url": "https://productivity.directory/paymo"},
    "ProofHub": {"desc": "Centro de aprobación y control de calidad visual.", "url": "https://productivity.directory/proofhub"},
    "Routine": {"desc": "Nexo inteligente de captura rápida y rituales.", "url": "https://productivity.directory/routine"},
    "Smartsheet": {"desc": "Tablero maestro con automatización de flujos lógicos.", "url": "https://productivity.directory/smartsheet"},
    "Taskwarrior": {"desc": "Núcleo de terminal CLI para máxima potencia móvil.", "url": "https://productivity.directory/taskwarrior"},
    "Wrike": {"desc": "Sincronizador transversal para unificación de departamentos.", "url": "https://productivity.directory/wrike"}
}

# Generación automática ordenada
for nombre in sorted(estaciones.keys()):
    info = estaciones[nombre]
    with st.expander(f"🔹 Estación: {nombre.upper()}"):
        st.write(info["desc"])
        st.markdown(f"[🔗 Acceder a la Estación]({info['url']})")

# 6. PIE DE PÁGINA (La Sentencia Final)
st.divider()
st.caption("Fuerza y Honor. Registro FRN-0038392759. El rascacielos gráfico está en el aire.")
