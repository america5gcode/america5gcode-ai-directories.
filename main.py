import streamlit as st

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Terminal X | Constructora", layout="wide")

# --- MENÚ DE MANDO ---
st.sidebar.title("🏙️ TERMINAL X")
seccion = st.sidebar.radio("MANDO:", ["Perfil", "Constructor de Proyectos", "Sistema de Ascenso"])

if seccion == "Perfil":
    st.title("👤 PERFIL: GUSTAVO SANABRIA")
    st.write("CEO PHELPS TUCKER GROUP")

elif seccion == "Constructor de Proyectos":
    st.title("🏗️ CENTRO DE CONSTRUCCIÓN IA")
    st.write("Seleccione el formato o dirección para iniciar la construcción de su red:")
    
    # Simulación de lectura de base de datos/enlaces del repositorio
    formato = st.selectbox("Elija Formato de Construcción:", ["Formato A (Lead Gen)", "Formato B (Ad Network)", "Formato C (Blockchain)"])
    
    # Aquí es donde inyectamos la "dirección" que la usuaria necesita
    if formato:
        st.info(f"Generando enlace de construcción para: {formato}")
        # Enlace dinámico (aquí irían los links que mencionó de GitHub)
        st.success("🔗 [ACCEDER AL ENLACE DE CONSTRUCCIÓN]")
        st.code("Comando de Activación: python3 constructor.py --mode soberano")

elif seccion == "Sistema de Ascenso":
    st.title("📈 REGLAS DE ESCALABILIDAD")
    ref = st.number_input("Referidos:", 0)
    if ref >= 200: st.success("🚀 ASCENSO A PRO")
