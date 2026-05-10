import streamlit as st

st.set_page_config(page_title="Terminal X - Mando Miami", layout="wide")

# CABECERA FEDERAL
st.title("🏗️ TERMINAL X: RASCACIELOS GRÁFICO")
st.subheader("PHELPS TUCKER GROUP LLC")
st.caption("Registro Federal: FRN-0038392759 | Miami, FL")

st.divider()

# MATRIZ DE PLANES CON ASCENSOS AUTOMÁTICOS
st.header("📋 OFERTA DE PLANES Y RUTAS DE ASCENSO")
col1, col2, col3 = st.columns(3)

with col1:
    st.info("### PLAN FREE")
    st.write("**Patrocinado por Anunciantes**")
    st.markdown("- 📈 **A PRO:** 200 Referidos")
    st.markdown("- 💎 **A PLATINO:** 50 Anuncios ($5 c/u)")
    st.link_button("Denominación: ACCESO FREE", "https://v0-ia-creation-system.vercel.app/")

with col2:
    st.success("### PLAN PRO")
    st.write("**$200 (6m) / $100 (Anual)**")
    st.markdown("- 🛡️ **Estatus:** Registro Federal")
    st.markdown("- 💎 **A PLATINO:** Afiliación al Club")
    st.link_button("Denominación: REGISTRO PRO", "https://formspree.io/f/mvzlvnyn")

with col3:
    st.warning("### PLAN PLATINO")
    st.write("**Inversión Mínima: $400,000**")
    st.markdown("- 🏦 **Nivel:** Wall Street Direct")
    st.markdown("- ⭐ **Jerarquía:** Máxima Soberanía")
    st.link_button("Denominación: MANDO PLATINO", "https://github.com/fccinternationalus/TerminalX")

st.divider()
st.caption("Fuerza y Honor. La estructura ha sido restaurada según el diseño original.")
