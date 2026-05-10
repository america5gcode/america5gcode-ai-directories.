import streamlit as st

# --- PÁGINA 1620: MODELO DE NEGOCIO Y CONVERSIÓN ---
st.header("💎 MODELO DE ASCENSO: TERMINAL X")
st.markdown(f"**Registro Federal:** FRN-0038392759 | **Estatus IRS:** Vinculado")

# 1. EL MOTOR DE CONVERSIÓN FREE -> PLATINO
with st.container():
    st.subheader("🆓 VERSIÓN FREE (Patrocinada)")
    st.write("""
    Navegación y exploración ilimitada. El usuario es patrocinado por anunciantes.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Costo por Anuncio (AD)", value="$5.00")
    with col2:
        st.metric(label="Umbral de Ascenso", value="50 Anuncios")
        
    st.success("🎯 **Conversión Automática:** Al alcanzar los 50 anuncios, el usuario asciende directamente al nivel **PLATINO**.")

st.divider()

# 2. EL PODER DE LA VERSIÓN PRO (Exclusión del Registro FSCC)
with st.container():
    st.subheader("🚀 VERSIÓN PRO (Comercialización Directa)")
    st.info("Punto clave: Exclusión del registro FSCC de Marketing Digital.")
    st.write("""
    Esta versión está diseñada para quienes desean comercializar sin las trabas del registro FSCC. 
    Al estar vinculada directamente con el **IRS**, permite una gestión de ingresos profesional.
    """)
    
    st.warning("⚠️ **AFILIACIÓN AL GRUPO FIRST:** Al inscribirse en Pro, el usuario recibe automáticamente los estándares del Nivel Platino.")

st.divider()

# 3. EL NIVEL PLATINO (Wall Street & Inversión Directa)
with st.container():
    st.subheader("👑 VERSIÓN PLATINO (Inversionistas)")
    st.write("""
    **Destino final: Wall Street.** Los usuarios Platino son inversionistas directos.
    Sus ganancias están ligadas al desempeño operativo de la Red Social Terminal X.
    """)
    st.markdown("""
    * **Beneficio:** Reciben dividendos directos según la ejecución del proyecto.
    * **Alcance:** Máxima visibilidad en los mercados financieros globales.
    """)
