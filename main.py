import streamlit as st

# 1. IDENTIDAD DEL RASCACIELOS
st.set_page_config(page_title="Terminal X - Mando Miami", layout="wide")

# 2. ESCUDO CORPORATIVO (ESTRUCTURA DE ALTA DISPONIBILIDAD)
# Usamos un contenedor HTML para forzar la renderización del logo 
# bajo el Registro Federal FRN-0038392759
with st.container():
    col_logo, col_info = st.columns([1, 3])
    with col_logo:
        # Forzamos la carga desde el repositorio central de confianza
        logo_url = "https://raw.githubusercontent.com/fccinternationalus/TerminalX/main/logo.jpg"
        st.markdown(
            f"""
            <div style="display: flex; justify-content: center;">
                <img src="{logo_url}" width="210" style="border-radius: 12px; border: 2px solid #30363d;">
            </div>
            """, 
            unsafe_allow_html=True
        )
    with col_info:
        st.title("🏗️ TERMINAL X: RASCACIELOS GRÁFICO")
        st.markdown("## **PHELPS TUCKER GROUP LLC**")
        st.write("📍 **Sede:** 8345 NW 66st Miami, Florida, USA 33166")
        st.caption("Registro Federal: FRN-0038392759 | Estatus: ACTIVO")

st.divider()

# 3. MÓDULO DE REGISTRO (CONEXIÓN SEGURA)
st.header("👤 REGISTRO DE SOCIOS FEDERALES")
st.success("🛰️ Enlace de Datos Miami 33166: OPERATIVO")

form_id = "mvzlvnyn"
registro_html = f"""
<div style="background-color: #0e1117; padding: 25px; border-radius: 15px; border: 1px solid #30363d; color: white;">
    <form action="https://formspree.io/f/{form_id}" method="POST">
        <label style="font-weight: bold; color: #8b949e;">NOMBRE Y APELLIDO:</label><br>
        <input type="text" name="name" style="width: 100%; padding: 12px; margin: 10px 0; border-radius: 5px; border: 1px solid #30363d; background: #161b22; color: white;" placeholder="Ej: Gustavo Sanabria" required><br>
        
        <label style="font-weight: bold; color: #8b949e;">ID / PASAPORTE:</label><br>
        <input type="text" name="id" style="width: 100%; padding: 12px; margin: 10px 0; border-radius: 5px; border: 1px solid #30363d; background: #161b22; color: white;" placeholder="V-XXXXXXX" required><br>
        
        <label style="font-weight: bold; color: #8b949e;">EMAIL DE CONTACTO:</label><br>
        <input type="email" name="_replyto" style="width: 100%; padding: 12px; margin: 10px 0; border-radius: 5px; border: 1px solid #30363d; background: #161b22; color: white;" placeholder="socio@phelps.com" required><br>
        
        <input type="hidden" name="_subject" value="NUEVA ACTIVACIÓN: TERMINAL X">
        <button type="submit" style="width: 100%; padding: 18px; background-color: #238636; color: white; border: none; border-radius: 8px; font-weight: bold; cursor: pointer; text-transform: uppercase; font-size: 16px;">
            VERIFICAR Y ACTIVAR PERFIL
        </button>
    </form>
</div>
"""
st.components.v1.html(registro_html, height=480)

# 4. SISTEMA TRONLINK
st.divider()
st.header("🔑 VINCULACIÓN TRONLINK")
st.text_input("Llave TRC-20 para Transacciones:", placeholder="Txxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
if st.button("Sincronizar Bóveda"):
    st.info("Estableciendo conexión con la red Tron...")

# 5. PIE DE PÁGINA
st.divider()
st.caption("Fuerza y Honor. Operación Miami 33166 | Registro FRN-0038392759")
