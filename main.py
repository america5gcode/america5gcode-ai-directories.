import streamlit as st

# --- CONFIGURACIÓN DE IDENTIDAD OFICIAL ---
st.set_page_config(page_title="Red Social Terminal X", page_icon="🌐", layout="wide")

# --- MENÚ LATERAL ---
st.sidebar.title("📱 RED SOCIAL TERMINAL X")
st.sidebar.info("Asistente Oficial: Certificación en Trámite (FCC/Google Studio)")
seccion = st.sidebar.radio("CENTRO DE MANDO:", 
    ["Dashboard & TronLink", "Foro General Transparente", "Constructor por Voz", "Perfil Soberano"])

# --- 1. DASHBOARD CON TRONLINK OBLIGATORIO ---
if seccion == "Dashboard & TronLink":
    st.title("📊 DASHBOARD DE OPERACIONES FINANCIERAS")
    st.write("Vincule su billetera para activar las funciones comerciales.")
    
    # ENTRADA DE BILLETERA (EL ANCLA)
    wallet = st.text_input("🔗 Ingrese su dirección TronLink (Requisito para cobros/pagos):", placeholder="T...")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Estatus de Red", "Activo")
    with col2:
        st.metric("Referidos", "0 / 200")
    with col3:
        st.metric("Cartera", "Vinculada" if wallet.startswith("T") else "Pendiente")

    st.write("---")
    
    # SERVICIOS CON PAGO INTEGRADO
    st.subheader("🚀 ACCESO A VERSIONES PAGAS")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.info("📣 **Plan Pro (Influencers)**")
        if st.button("🔓 Activar Plan Pro"):
            if wallet.startswith("T"):
                st.success("Procesando suscripción a través de TronLink...")
            else:
                st.error("⚠️ Error: Debe vincular su billetera TronLink para acceder a la versión paga.")
            
    with col_b:
        st.info("📈 **Plan Platino (Wall Street)**")
        if st.button("🔓 Activar Plan Platino"):
            if wallet.startswith("T"):
                st.success("Conectando con el nodo de liquidación Tron...")
            else:
                st.error("⚠️ Error: TronLink obligatorio para auditoría financiera.")

# --- 2. FORO GENERAL ---
elif seccion == "Foro General Transparente":
    st.title("🏛️ FORO PÚBLICO")
    st.warning("Transparencia Radical: Sin mensajes privados para auditoría de Wall Street.")
    st.text_input("Escriba su mensaje al foro:")
    st.button("Publicar")

# --- 3. CONSTRUCTOR POR VOZ ---
elif seccion == "Constructor por Voz":
    st.title("🎙️ CONSTRUCTOR GÉMINIS")
    st.write("Diga su propuesta para construir su red social.")
    st.button("🔴 Iniciar Micrófono")

# --- 4. PERFIL SOBERANO ---
elif seccion == "Perfil Soberano":
    st.title("👤 PERFIL: GUSTAVO SANABRIA")
    st.subheader("CEO & Registrador Principal")
