import streamlit as st

st.set_page_config(page_title="Terminal X - Mando Miami", layout="wide")

st.title("🏗️ TERMINAL X: RASCACIELOS GRÁFICO")
st.subheader("PHELPS TUCKER GROUP LLC")
st.caption("Registro Federal: FRN-0038392759 | Sede: Miami 33166")

st.divider()

# TABLERO DE CONTROL DE OFERTAS
st.header("📋 MATRIZ DE PLANES Y ASCENSOS")
col1, col2, col3 = st.columns(3)

with col1:
    st.info("### PLAN FREE")
    st.write("**Patrocinado**")
    st.markdown("🚀 **Ascenso a PRO:** 200 Referidos")
    st.markdown("💎 **Ascenso a PLATINO:** 50 Anuncios ($5 c/u)")
    st.link_button("Iniciar Carrera", "https://v0-ia-creation-system.vercel.app/")

with col2:
    st.success("### PLAN PRO")
    st.write("**Inversión:** $200 (6m) / $100 (Anual)")
    st.markdown("🛡️ **Beneficio:** Registro Federal Incluido")
    st.markdown("💎 **Ascenso a PLATINO:** Afiliación al Club")
    st.link_button("Activar Estatus PRO", "https://formspree.io/f/mvzlvnyn")

with col3:
    st.warning("### PLAN PLATINO")
    st.write("**Inversión Mínima:** $400,000")
    st.markdown("🏦 **Nivel:** Wall Street Direct")
    st.markdown("⭐ **Jerarquía:** Máxima Soberanía")
    st.link_button("Mando Corporativo", "https://github.com/fccinternationalus/TerminalX")

st.divider()
st.caption("Fuerza y Honor. El flujo de ascenso automático está blindado en el ADN del sistema.")
