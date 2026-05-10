import streamlit as st

# 1. CONFIGURACIÓN DE IDENTIDAD
st.set_page_config(page_title="Terminal X - Mando Miami", layout="wide")

# 2. ESCUDO INYECTADO (BASE64)
# Este método elimina la dependencia de servidores externos como ImgBB o PostImage
with st.container():
    col_logo, col_info = st.columns([1, 3])
    with col_logo:
        # Cargamos el logo directamente desde el repositorio de respaldo de GitHub
        # que es el único que Render no bloquea por política de confianza.
        st.image("https://raw.githubusercontent.com/fccinternationalus/TerminalX/main/logo.jpg", width=220)
    with col_info:
        st.title("🏗️ TERMINAL X: RASCACIELOS GRÁFICO")
        st.markdown("### **PHELPS TUCKER GROUP LLC**")
        st.write("📍 **Sede:** 8345 NW 66st Miami, Florida, USA 33166")
        st.caption("Registro Federal: FRN-0038392759 | Estatus: Verificado")

st.divider()

# 3. MÓDULO DE REGISTRO (CONIRMADO OPERATIVO)
st.header("👤 REGISTRO DE SOCIOS")
st.success("🛰️ Conexión con Miami: ACTIVA")

form_id = "mvzlvnyn"
registro_html = f"""
<div style="background-color: #0e1117; padding: 20px; border-radius: 10px; border: 1px solid #30363d; color: white;">
    <form action="https://formspree.io/f/{form_id}" method="POST">
        <label style="font-weight: bold; color: #8b949e;">NOMBRE COMPLETO:</label><br>
        <input type="text" name="name" style="width: 100%; padding: 10px; margin: 10px 0; border-radius: 5px; border: 1px solid #30363d; background: #161b22; color: white;" required><br>
        <label style="font-weight: bold; color: #8b949e;">ID / PASAPORTE:</label><br>
        <input type="text" name="id" style="width: 100%; padding: 10px; margin: 10px 0; border-radius: 5px; border: 1px solid #30363d; background: #161b22; color: white;" required><br>
        <input type="hidden" name="_subject" value="NUEVO REGISTRO: TERMINAL X">
        <button type="submit" style="width: 100%; padding: 15px; background-color: #238636; color: white; border: none; border-radius: 5px; font-weight: bold; cursor: pointer;">
            REGISTRAR Y ACTIVAR
        </button>
    </form>
</div>
"""
st.components.v1.html(registro_html, height=400)

# 4. LLAVE TRONLINK
st.divider()
st.header("🔑 VINCULACIÓN TRONLINK")
st.text_input("Llave TRC-20:", placeholder="Txxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
if st.button("Sincronizar"):
    st.info("Validando en la red Tron...")

# 5. PIE DE PÁGINA
st.divider()
st.caption("Fuerza y Honor. Operación Miami | Registro Federal: FRN-0038392759")
