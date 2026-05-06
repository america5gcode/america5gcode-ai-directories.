import streamlit as st

# --- TERMINAL X CONTROL ---
st.set_page_config(page_title="Terminal X", layout="wide")

st.sidebar.title("🏙️ MENU X")
opcion = st.sidebar.radio("IR A:", ["Aduana", "Ascenso", "Mina de Oro"])

if opcion == "Aduana":
    st.title("🛡️ ADUANA")
    id_ia = st.text_input("Proyecto:")
    if st.button("VALIDAR"):
        st.success(f"✅ ACCESO: {id_ia}")

elif opcion == "Ascenso":
    st.title("📈 ASCENSOS")
    ref = st.number_input("Referidos (Meta 200):", 0)
    if ref >= 200: st.success("🚀 ASCENSO A PRO!")
    
    st.write("---")
    ads = st.number_input("Anuncios (Meta 50):", 0)
    if ads >= 50: st.success("🏆 ASCENSO A PLATINO!")

elif opcion == "Mina de Oro":
    st.title("⛏️ MINA DE ORO")
    st.info("Sincronizando Leads y Operaciones...")
