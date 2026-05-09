import streamlit as st

# --- 1. IDENTIDAD FEDERAL MIAMI ---
st.set_page_config(page_title="Terminal X - Núcleo Soberano", page_icon="🌐", layout="wide")

# --- 2. MENÚ LATERAL CERTIFICADO ---
st.sidebar.title("📱 RED SOCIAL TERMINAL X")
st.sidebar.success(f"🛡️ ASISTENTE OFICIAL CERTIFICADO\n\nFRN: 0038392759\nSede: Miami, FL")

# --- 3. CONSTRUCTOR CON PROCESAMIENTO PERSISTENTE ---
st.title("🎙️ RED SOCIAL TERMINAL X")
st.warning("⚠️ DECRETO: Inteligencia Federal Activa. Ejecución bajo FRN: 0038392759.")

# Inicializar el cerebro si no existe
if 'respuesta_soberana' not in st.session_state:
    st.session_state['respuesta_soberana'] = ""

propuesta = st.text_area("Dicte su instrucción:", 
                         height=100, 
                         placeholder="Ej: '¿Qué es la inteligencia dinamita?'...")

if st.button("🔴 EJECUTAR", use_container_width=True):
    if propuesta.strip() != "":
        # MOTOR DE LÓGICA DINAMITA
        p = propuesta.lower()
        if "dinamita" in p:
            st.session_state['respuesta_soberana'] = "La **Inteligencia Dinamita** es la potencia de explosión cognitiva que descompone y valida datos masivos para el PHELPS TUCKER GROUP."
        elif "scout" in p:
            st.session_state['respuesta_soberana'] = "El **AI Scout** es el centinela autónomo que garantiza la veracidad de cada lead B2B en el ecosistema soberano."
        else:
            st.session_state['respuesta_soberana'] = f"Instrucción '{propuesta}' procesada y blindada bajo el Registro Federal FRN: 0038392759."
    else:
        st.error("⚠️ Ingrese una instrucción para activar el núcleo.")

# --- 4. EMISIÓN BLINDADA (Faltaba esto para que no desaparezca) ---
if st.session_state['respuesta_soberana'] != "":
    st.markdown("---")
    st.subheader("🛡️ INFORME SOBERANO:")
    st.info(st.session_state['respuesta_soberana'])
    st.write("📍 *Veracidad técnica certificada en Miami, FL.*")

# PIE DE PÁGINA INSTITUCIONAL
st.markdown("---")
st.markdown(f"<p style='text-align: center; color: gray;'>FRN: 0038392759 | Sede Federal: 8345 NW 66st Miami, FL</p>", unsafe_allow_html=True)
