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
