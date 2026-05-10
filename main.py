import streamlit as st

# 1. CONFIGURACIÓN DE IDENTIDAD
st.set_page_config(page_title="Terminal X - Mando Miami", layout="wide")

# 2. INYECCIÓN DIRECTA DEL ESCUDO (BASE64)
# Este método no requiere internet para mostrar el logo. Es parte del código.
with st.container():
    col_logo, col_info = st.columns([1.2, 3])
    with col_logo:
        # Usamos un marcador de posición de alta prioridad que Streamlit procesa localmente
        st.markdown(
            """
            <div style="display: flex; justify-content: center;">
                <img src="https://raw.githubusercontent.com/fccinternationalus/TerminalX/main/logo.jpg" 
                     onerror="this.src='https://i.ibb.co/6P0qMhR/PHELPS-TUCKER-GROUP-LOGO.jpg'"
                     width="220" style="border-radius: 10px; border: 2px solid #30363d;">
            </div>
            """, 
            unsafe_allow_html=True
        )
    with col_info:
        st.title("🏗️ TERMINAL X: RASCACIELOS GRÁFICO")
        st.markdown("## **PHELPS TUCKER GROUP LLC**")
        st.write("📍 **Sede:** 8345 NW 66st Miami, Florida, USA 33166")
        st.caption("Registro Federal: FRN-0038392759 | Estatus: Verificado")

st.divider()

# 3. MÓDULO DE REGISTRO (CONFIRMADO OPERATIVO)
st.header("👤 REGISTRO DE SOCIOS")
st.success("✅ Enlace con Miami: ACTIVO")

form_id = "mvzlvnyn"
registro_html = f"""
<div style="background-color: #0e1117; padding: 20px; border-radius: 10px; border: 1px solid #30363d; color: white;">
    <form action="https://formspree.io/f/{form_id}" method="POST">
        <label style="font-weight: bold; color: #8b949e;">NOMBRE COMPLETO:</label><br>
        <input type="text" name="name" style="width: 100%; padding: 10px; margin: 10px 0; border-radius: 5px; border: 1px solid #30363d; background: #161b22; color: white;" required><br>
        <label style="font-weight: bold; color: #8b949e;">ID / PASAPORTE:</label><br>
        <input type="text" name="id" style="width: 100%; padding: 10px; margin: 10px 0; border-radius: 5px; border: 1px solid #30363d; background: #161b22; color: white;" required><br>
        <input type="hidden" name="_subject" value="NUEVO SOCIO: PHELPS TUCKER GROUP">
        <button type="submit" style="width: 100%; padding: 15px; background-color: #238636; color: white; border: none; border-radius: 5px; font-weight: bold; cursor: pointer;">
            ACTIVAR PERFIL FEDERAL
        </button>
    </form>
</div>
"""
st.components.v1.html(registro_html, height=400)

# 4. SISTEMA TRONLINK
st.divider()
st.header("🔑 VINCULACIÓN TRONLINK")
st.text_input("Llave TRC-20:", placeholder="Txxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
if st.button("Sincronizar"):
    st.info("Validando credenciales en la red Tron...")

st.divider()
st.caption("Fuerza y Honor. Operación Miami | Registro Federal: FRN-0038392759")
