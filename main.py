import streamlit as st

# Configuración de la página (Título en la pestaña del navegador)
st.set_page_config(page_title="Terminal X - Centro de Mando", layout="wide")

# Cabecera del Imperio
st.header("🏗️ RASCACIELOS GRÁFICO: DIRECTORIO DE POTENCIA")
st.subheader("Registro Federal: FRN-0038392759")

st.info("Comandante: Gestión de infraestructura, logística y capital de inversión.")

# --- SECCIÓN: EL ASADO DE ESTACIONES (18-32) ---
st.markdown("### 🛰️ Estaciones de Control de Proyectos")

# Diccionario de datos para automatizar la creación de la interfaz
estaciones = {
    "18. ROUTINE": {"desc": "Nexo Inteligente: Captura rápida y rituales operativos.", "link": "https://productivity.directory/routine"},
    "19. NOTEPLAN": {"desc": "Bitácora de Ingeniería: Notas diarias en Markdown y tareas.", "link": "https://productivity.directory/noteplan"},
    "20. TASKWARRIOR": {"desc": "Núcleo de Terminal: Gestión CLI para entornos Android/Termux.", "link": "https://productivity.directory/taskwarrior"},
    "21. JIRA": {"desc": "Ingeniería Pesada: Gestión ágil de sprints y tickets de desarrollo.", "link": "https://productivity.directory/jira"},
    "22. MS PROJECT": {"desc": "Planificación Estructural: Ruta crítica y presupuestos corporativos.", "link": "https://productivity.directory/microsoft-project"},
    "23. PROOFHUB": {"desc": "Centro de Aprobación: Revisión visual y auditoría de documentos.", "link": "https://productivity.directory/proofhub"},
    "24. GANTTPRO": {"desc": "Refinería de Cronogramas: Planificación visual de dependencias.", "link": "https://productivity.directory/ganttpro"},
    "25. NTASK": {"desc": "Nexo Multi-Dimensional: Control de riesgos, tiempos y reuniones.", "link": "https://productivity.directory/ntask"},
    "26. FUSEBASE": {"desc": "Portal de Transparencia: Marca blanca para inversores y socios.", "link": "https://productivity.directory/fusebase"},
    "27. PAYMO": {"desc": "Central de Rentabilidad: Facturación y auditoría de eficiencia.", "link": "https://productivity.directory/paymo"},
    "28. HUBSTAFF": {"desc": "Radar de Despliegue: Monitoreo por GPS y productividad en tiempo real.", "link": "https://productivity.directory/hubstaff"},
    "29. LINEAR": {"desc": "Acelerador de Sprints: Gestión de issues a velocidad supersónica.", "link": "https://productivity.directory/linear"},
    "30. SMARTSHEET": {"desc": "Tablero Maestro: Automatización lógica de flujos empresariales.", "link": "https://productivity.directory/smartsheet"},
    "31. WRIKE": {"desc": "Sincronizador Transversal: Unificación de departamentos en un solo flujo.", "link": "https://productivity.directory/wrike"},
    "32. BASECAMP": {"desc": "Búnker de Comunicación: Colaboración centralizada libre de ruido.", "link": "https://productivity.directory/basecamp"}
}

# Generación automática de los expanders (el "asado")
for nombre, info in estaciones.items():
    with st.expander(f"🔹 {nombre}"):
        st.write(info["desc"])
        st.markdown(f"[🔗 Acceder a la Estación]({info['link']})")

# Pie de página con Sentencia del Asistente
st.divider()
st.caption("Fuerza y Honor. Operación activa y normal bajo supervisión del Centinela.")
