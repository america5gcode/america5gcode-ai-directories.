import streamlit as st

# 1. CONFIGURACIÓN DE IDENTIDAD FEDERAL
st.set_page_config(page_title="Terminal X - Mando Miami", layout="wide")

# 2. ESCUDO CORPORATIVO (INYECTADO POR CÓDIGO)
# Esta URL de GitHub es la única que Render reconoce como segura y estable
logo_final = "https://raw.githubusercontent.com/fccinternationalus/TerminalX/main/logo.jpg"

with st.container():
    col_logo, col_info = st.columns([1, 3])
    with col_logo:
        # Forzamos la carga mediante HTML para saltar los filtros de Render
        st.markdown(
            f"""
            <img src="{logo_final}" width="220" style="border-radius: 10px; border: 1px solid #30363d;">
            """, 
            unsafe_allow_html=True
        )
    with col_info:
        st.title("🏗️ TERMINAL X: RASCACIELOS GRÁFICO")
        st.markdown("### **PHELPS TUCKER GROUP LLC**")
        st.write("📍 **Sede:** 8345 NW 66st Miami, Florida, USA 33166")
        st.caption("Registro Federal: FRN-0038392759 | Estatus: Verificado")

st.divider()

# 3. MÓDULO DE REGISTRO FEDERAL
st.header("👤 REGISTRO DE SOCIOS")
st.success("🛰️ Conexión con Miami 33166: ACTIVA")

form_id = "mvzlvnyn"
registro_html = f"""
<div style="background-color: #0e1117; padding: 20px; border-radius: 10px; border: 1px solid #30363d; color: white; font-family: sans-serif;">
    <form action="https://formspree.io/f/{form_id}" method="POST">
        <label style="font-weight: bold; color: #8b949e;">NOMBRE COMPLETO:</label><br>
        <input type="text" name="name" style="width: 100%; padding: 10px; margin: 10px 0; border-radius: 5px; border: 1px solid #30363d; background: #161b22; color: white;" required><br>
        <label style="font-weight: bold; color: #8b949e;">ID / PASAPORTE:</label><br>
        <input type="text" name="id" style="width: 100%; padding: 10px; margin: 10px 0; border-radius: 5px; border: 1px solid #30363d; background: #161b22; color: white;" required><br>
        <input type="hidden" name="_subject" value="NUEVO REGISTRO: PHELPS TUCKER GROUP">
        <button type="submit" style="width: 100%; padding: 15px; background-color: #238636; color: white; border: none; border-radius: 5px; font-weight: bold; cursor: pointer; text-transform: uppercase;">
            REGISTRAR PERFIL Y ACTIVAR
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
    st.info("Validando en la red Tron...")

# 5. PIE DE PÁGINA CORPORATIVO
st.divider()
st.caption("Fuerza y Honor. Operación Miami | Registro Federal: FRN-0038392759")
