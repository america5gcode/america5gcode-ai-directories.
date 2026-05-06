import streamlit as st

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Terminal X | Constructor Soberano", layout="wide")

# --- MENÚ LATERAL ---
st.sidebar.title("🏙️ TERMINAL X")
seccion = st.sidebar.radio("DEPARTAMENTO:", ["Mi Perfil", "Centro de Construcción", "Sistema de Ascenso", "Mina de Oro"])

# --- 1. PERFIL ---
if seccion == "Mi Perfil":
    st.title("👤 PERFIL SOBERANO")
    st.write("Fundador: **Gustavo Sanabria**")
    st.info("Estatus: Registrador Principal")

# --- 2. CONSTRUCTOR (LA LIBERTAD) ---
elif seccion == "Centro de Construcción":
    st.title("🛠️ CONSTRUCTOR DE APLICACIONES ILIMITADO")
    st.write("Bienvenido. Aquí puede diseñar cualquier plataforma (Ventas, Servicios, Blogs).")
    
    tipo_pagina = st.text_input("¿Qué desea construir hoy? (Ej: Venta de Carros, Inmobiliaria)", "")
    
    if tipo_pagina:
        st.success(f"🏗️ Generando estructura para: **{tipo_pagina}**")
        st.info("Estatus: Construcción de Fachada y Catálogo completada al 100%.")
        
        st.write("---")
        st.subheader("🤝 MÓDULO DE NEGOCIACIÓN")
        if st.button("ACTIVAR BOTÓN DE VENTA Y CONTRATOS"):
            # AQUÍ ES DONDE APARECE LA BARRERA QUE USTED PIDE
            st.error("🚫 ACCIÓN RESTRINGIDA")
            st.warning("Para negociar legalmente y cerrar ventas, su perfil debe estar certificado en **FORMACIÓN PRO**.")
            if st.button("IR A FORMACIÓN PRO PARA ACTIVAR NEGOCIOS"):
                st.info("Redirigiendo al Departamento de Ascenso...")

# --- 3. SISTEMA DE ASCENSO (EL PUENTE) ---
elif seccion == "Sistema de Ascenso":
    st.title("📈 DEPARTAMENTO DE FORMACIÓN Y ASCENSO")
    st.subheader("💎 FORMACIÓN PRO")
    st.write("Requisito para Negociación Legal y cierre de transacciones en la red.")
    
    referidos = st.number_input("Número de Referidos actual:", 0)
    if referidos >= 200:
        st.success("🚀 ¡FELICIDADES! Usted ha ascendido a PRO. El botón de negociación ya está activo en sus páginas.")
    else:
        st.write(f"Faltan {200 - referidos} referidos para activar su capacidad legal de comercio.")

# --- 4. MINA DE ORO ---
elif seccion == "Mina de Oro":
    st.title("⛏️ MINA DE ORO (BI)")
    st.write("Registro de leads y movimientos financieros del rascacielos.")
