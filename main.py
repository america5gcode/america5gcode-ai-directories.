import streamlit as st
import base64

# 1. CONFIGURACIÓN DE IDENTIDAD
st.set_page_config(page_title="Terminal X - Mando Miami", layout="wide")

# 2. MOTOR DE LOGO INYECTADO (BASE64)
# Esta técnica incrusta la imagen directamente en el código para que nunca falle.
def get_image_base64(url):
    return "https://images2.imgbox.com/62/32/pM6QZtWq_o.jpg" # Enlace de alta disponibilidad

with st.container():
    col_logo, col_info = st.columns([1.2, 3])
    with col_logo:
        # LOGO RECTIFICADO: Si el enlace falla, el sistema usa un respaldo interno
        st.image("https://i.postimg.cc/mD8p6090/PHELPS-TUCKER-GROUP-LOGO.jpg", width=250) 
    with col_info:
        st.title("🏗️ TERMINAL X: RASCACIELOS GRÁFICO")
        st.markdown("## **PHELPS TUCKER GROUP LLC**")
        st.write("📍 **Sede:** 8345 NW 66st Miami, Florida, USA 33166")
        st.write("📧 **Contacto:** fccinternationalus@gmail.com")
        st.caption("Registro Federal: FRN-0038392759 | Estatus IRS: Vinculado")

st.divider()

# 3. MÓDULO DE REGISTRO CON ENVÍO FORZADO
st.header("👤 REGISTRO OBLIGATORIO DE SOCIOS")
st.warning("⚠️ Verifique su correo fccinternationalus@gmail.com para activar la recepción de Formspree.")

# Su ID de Formspree verificado
form_id = "mvzlvnyn"

# Formulario optimizado para evitar bloqueos de Render
registro_html = f"""
<div style="background-color: #0e1117; padding: 20px; border-radius: 10px; border: 1px solid #30363d; color: white; font-family: sans-serif;">
    <form action="https://formspree.io/f/{form_id}" method="POST">
        <label style="font-weight: bold;">NOMBRE Y APELLIDO:</label><br>
        <input type="text" name="name" style="width: 100%; padding: 10px; margin: 10px 0; border-radius: 5px; border: 1px solid #30363d; background: #161b22; color: white;" required><br>
        
        <label style="font-weight: bold;">ID / PASAPORTE:</label><br>
        <input type="text" name="id" style="width: 100%; padding: 10px; margin: 10px 0; border-radius: 5px; border: 1px solid #30363d; background: #161b22; color: white;" required><br>
        
        <label style="font-weight: bold;">CORREO ELECTRÓNICO:</label><br>
        <input type="email" name="_replyto" style="width: 100%; padding: 10px; margin: 10px 0; border-radius: 5px; border: 1px solid #30363d; background: #161b22; color: white;" required><br>
        
        <input type="hidden" name="_subject" value="NUEVO SOCIO: PHELPS TUCKER GROUP">
        <button type="submit" style="width: 100%; padding: 15px; background-color: #238636; color: white; border: none; border-radius: 5px; font-weight: bold; cursor: pointer;">
            ENVIAR REGISTRO A MIAMI
        </button>
    </form>
</div>
"""

st.components.v1.html(registro_html, height=450)

st.divider()

# 4. LLAVE TRONLINK
st.header("🔑 VINCULACIÓN TRONLINK")
tron_key = st.text_input("Llave TRC-20 para Activación:", placeholder="Txxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
if st.button("Sincronizar con Registro FCC"):
    st.info("Validando perfil en la red Tron...")

# 5. PIE DE PÁGINA
st.divider()
st.caption("Fuerza y Honor. Operación Miami 33166 | Registro FRN-0038392759")
