import streamlit as st

# Título y Registro en la cabecera
st.title("🏗️ Rascacielos Gráfico - Terminal X")
st.markdown("### Registro Federal: FRN-0038392759")

# --- BLOQUE CONFIRMADO EN LA PRUEBA ---
with st.expander("⚡ ROUTINE: El Nexo Inteligente de Ejecución"):
    st.write("Centro de operaciones para captura rápida de ideas y organización automática de rituales diarios.")
    st.markdown("[🔗 Abrir Routine](https://productivity.directory/routine)")

with st.expander("📝 NOTEPLAN: La Bitácora de Ingeniería"):
    st.write("Unión de notas diarias, tareas y calendario en Markdown. Memoria técnica del proyecto.")
    st.markdown("[🔗 Abrir NotePlan](https://productivity.directory/noteplan)")

with st.expander("💻 TASKWARRIOR: El Núcleo de la Terminal"):
    st.write("Gestión de tareas pura desde CLI. Máxima potencia para entornos Android/Termux.")
    st.markdown("[🔗 Abrir Taskwarrior](https://productivity.directory/taskwarrior)")

# --- SIGUIENTE BLOQUE PARA INTEGRAR ---
with st.expander("⚙️ JIRA: La Sala de Ingeniería Pesada"):
    st.write("Estándar industrial para desarrollo ágil, gestión de bugs y sprints técnicos.")
    st.markdown("[🔗 Abrir Jira](https://productivity.directory/jira)")

with st.expander("🏢 MS PROJECT: Central de Planificación Estructural"):
    st.write("Cálculo de camino crítico y gestión de presupuestos de alta fidelidad.")
    st.markdown("[🔗 Abrir MS Project](https://productivity.directory/microsoft-project)")
    import streamlit as st

# --- PÁGINA 1620: IDENTIDAD OPERATIVA ---
st.markdown("## 📟 PÁGINA 1620: MANIFIESTO DE PODER")
st.divider()

# SECCIÓN 1: ¿QUIÉNES SOMOS? (La Esencia)
with st.container():
    col1, col2 = st.columns([1, 2])
    with col1:
        st.subheader("🛠️ Somos lo que hacemos")
    with col2:
        st.write("""
        Somos arquitectos de soluciones móviles de alta complejidad. 
        Operamos desde el núcleo del sistema (**Android/Termux**), transformando 
        líneas de código en activos estratégicos. Nuestra identidad es la **Ejecución Pura**: 
        si no se puede medir, rastrear y automatizar, no existe en nuestro imperio.
        """)

# SECCIÓN 2: NUESTRAS OFERTAS (El Valor del Rascacielos)
st.markdown("### 💼 Portafolio de Soluciones Estratégicas")

tab1, tab2, tab3 = st.tabs(["🚀 Terminal X", "📊 Inteligencia CRM", "🏗️ Infraestructura"])

with tab1:
    st.markdown("""
    **Red Social de Prospección Avanzada**
    * Automatización de investigación de mercado.
    * Calificación de leads mediante IA propietaria.
    * Despliegue en entornos de alta disponibilidad.
    """)

with tab2:
    st.markdown("""
    **Sincronización Transversal (Zoho/HubSpot)**
    * Migración de bases de datos desde GitHub/Termux.
    * Limpieza y enriquecimiento de lead data.
    * Auditoría de métricas bajo registro federal.
    """)

with tab3:
    st.markdown("""
    **Gestión de Capital e Infraestructura**
    * Administración de inversión de grado corporativo ($200k+).
    * Planificación de ruta crítica y mitigación de riesgos.
    * Reportes de transparencia para socios estratégicos.
    """)

st.divider()
