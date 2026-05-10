import streamlit as st

st.set_page_config(page_title="Terminal X - Mando Miami", layout="wide")

# CABECERA ESTRUCTURAL
st.title("🏗️ TERMINAL X: RASCACIELOS GRÁFICO")
st.subheader("PHELPS TUCKER GROUP LLC")
st.caption("Registro Federal: FRN-0038392759 | Miami, FL")

st.divider()

# RECONEXIÓN DE PLANES Y ENLACES
st.header("📋 OFERTA DE PLANES OPERATIVOS")
col1, col2, col3 = st.columns(3)

with col1:
    st.info("### PLAN FREE")
    st.write("Patrocinado por Anunciantes")
    st.write("Coste: $5 por anuncio")
    st.write("**PROMO:** 50 anuncios = Salto a PLATINO")
    st.link_button("Acceso Free", "https://v0-ia-creation-system.vercel.app/")

with col2:
    st.success("### PLAN PRO")
    st.write("Incluye Registro Federal")
    st.write("Soporte Élite")
    st.write("**PROMO:** Afiliación al Club = Salto a PLATINO")
    st.link_button("Obtener PRO", "https://formspree.io/f/mvzlvnyn")

with col3:
    st.warning("### PLAN PLATINO")
    st.write("Directo a Wall Street")
    st.write("Máxima Jerarquía")
    st.write("Inversión Corporativa")
    st.link_button("Ir a Wall Street", "https://github.com/fccinternationalus/TerminalX")

st.divider()
st.caption("Fuerza y Honor. Todos los enlaces han sido restaurados en el ADN del código.")
