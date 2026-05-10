import streamlit as st

# --- PÁGINA 1620: MODELO DE NEGOCIO Y CONVERSIÓN ---
st.header("💎 MODELO DE ASCENSO: TERMINAL X")
st.markdown(f"**Registro Federal:** FRN-0038392759 | **Estatus IRS:** Vinculado")

# 1. EL MOTOR DE CONVERSIÓN FREE -> PLATINO
with st.container():
    st.subheader("🆓 VERSIÓN FREE (Patrocinada)")
    st.write("""
    Navegación y exploración ilimitada. Operación sostenida por anunciantes.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Costo por Anuncio (AD)", value="$5.00")
    with col2:
        st.metric(label="Umbral de Ascenso", value="50 Anuncios")
        
    st.success("🎯 **Conversión Automática:** Al alcanzar los 50 anuncios, el usuario asciende directamente al nivel **PLATINO**.")

st.divider()

# 2. EL PODER DE LA VERSIÓN PRO (Registro de Comercio FCC)
with st.container():
    st.subheader("🚀 VERSIÓN PRO (Comercialización Directa)")
    st.info("Punto clave: Incluye Registro de Comercio FCC.")
    st.write("""
    Esta versión incluye el registro **FCC**, permitiendo la comercialización legal 
    y técnica de activos digitales. Al estar vinculada directamente con el **IRS**, 
    facilita una gestión financiera de alto nivel.
    """)
    
    st.warning("⚡ **AFILIACIÓN PHELPS TUCKER GROUP:** Al afiliarse a la casa matriz, el usuario recibe automáticamente el estatus **PLATINO**.")

st.divider()

# 3. EL NIVEL PLATINO (Wall Street & Inversión Directa)
with st.container():
    st.subheader("👑 VERSIÓN PLATINO (Inversionistas)")
    st.write("""
    **Destino final: Wall Street.** Los usuarios Platino operan como inversionistas directos 
    bajo el respaldo de **PHELPS TUCKER GROUP**.
    """)
    st.markdown("""
    * **Beneficio:** Ganancias directas basadas en la ejecución operativa del imperio.
    * **Alcance:** Participación en el flujo de capital de mercados globales.
    """)
