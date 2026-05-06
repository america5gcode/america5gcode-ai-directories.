import streamlit as st

# --- CONFIGURACIÓN DE IDENTIDAD SOBERANA ---
st.set_page_config(page_title="Terminal X | Global Hub", page_icon="🌐", layout="wide")

# --- MENÚ LATERAL DE MANDO ---
st.sidebar.title("🏙️ TERMINAL X")
st.sidebar.write("Phelps Tucker Group")
st.sidebar.write("---")

seccion = st.sidebar.radio(
    "CONTROL DE PISOS:",
    ["Mi Perfil Soberano", "Teoría de Construcción", "Sistema de Ascenso (Free/Pro/Platino)", "Aduana & BI"]
)

# --- 1. PÁGINA DE PERFIL (RESTAURADA) ---
if seccion == "Mi Perfil Soberano":
    st.title("👤 PERFIL DEL COMANDANTE")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.info("Estatus: CEO / Fundador")
    with col2:
        st.subheader("Gustavo Sanabria")
        st.write("**Corporación:** PHELPS TUCKER GROUP")
        st.write("**Jurisdicción:** Maracay, Aragua")
        st.write("**Especialidad:** Derecho Registral & IA Soberana")
    st.success("✅ Identidad Blindada en la Red")

# --- 2. PÁGINA DE TEORÍA (RESTAURADA) ---
elif seccion == "Teoría de Construcción":
    st.title("🏗️ TEORÍA DEL RASCACIELOS DIGITAL")
    st.markdown("""
    ### Arquitectura de la Red Terminal X
    El rascacielos gráfico se basa en la **Veracidad Operativa**:
    * **Piso 1 (Cimientos):** Python 3 ejecutando el alma del proyecto.
    * **Piso 2 (Estructura):** Sincronización GitHub-Render para soberanía absoluta.
    * **Piso 3 (Propósito):** Generación de capital e inteligencia de ventas.
    """)
    st.info("El rascacielos es un ente vivo que crece con cada línea de código.")

# --- 3. SISTEMA DE ASCENSO (REGLAS DE HOY) ---
elif seccion == "Sistema de Ascenso (Free/Pro/Platino)":
    st.title("📈 ESCALABILIDAD AUTOMÁTICA")
    
    # Lógica Free a Pro (200 Referidos)
    st.subheader("🆓 PLAN FREE")
    referidos = st.number_input("Introduzca Referidos (Meta 200):", min_value=0, value=0)
    if referidos >= 200:
        st.success("🚀 ASCENSO A PRO: VALIDADO AUTOMÁTICAMENTE.")
    else:
        st.write(f"Faltan {200 - referidos} referidos para el nivel PRO.")

    st.write("---")
    
    # Lógica Anunciantes a Platino (50 Anuncios)
    st.subheader("📢 ANUNCIANTES DIRECTOS")
    anuncios = st.number_input("Introduzca Anuncios (Meta 50):", min_value=0, value=0)
    if anuncios >= 50:
        st.success("🏆 NIVEL PLATINO: CONEXIÓN DIRECTA Y MENCION HONORÍFICA.")

# --- 4. ADUANA & BUSINESS INTELLIGENCE ---
elif seccion == "Aduana & BI":
    st.title("🛡️ ADUANA ÉTICA & MINA DE ORO")
    st.markdown("#### Registro Global de Operaciones")
    st.metric("Sincronización LatAm", "100%", "Activa")
    st.table({
        "Departamento": ["Seguridad IA", "Ventas Globales", "Legal Tech"],
        "Estatus": ["Certificado", "Liquidando", "Verificado"]
    })
