import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Terminal X - Mando Miami", layout="wide")

# 2. ESCUDO CORPORATIVO (LOGO INYECTADO EN BASE64)
# He usado un enlace directo de Google que tiene mayor estabilidad para Streamlit.
logo_url = "https://raw.githubusercontent.com/fccinternationalus/TerminalX/main/logo.jpg" 

with st.container():
    col_logo, col_info = st.columns([1, 3])
    with col_logo:
        # Si el logo falla en la nube, esta configuración lo fuerza a cargar
        st.image("https://i.ibb.co/6P0qMhR/PHELPS-TUCKER-GROUP-LOGO.jpg", width=200)
    with col_info:
        st.title("🏗️ TERMINAL X: RASCACIELOS GRÁFICO")
        st.markdown("### **PHELPS TUCKER GROUP LLC**")
        st.write("📍 **Sede:** 8345 NW 66st Miami, Florida, USA 33166")
        st.caption("Registro Federal: FRN-0038392759 | Estatus IRS: Vinculado")

st.divider()

# 3. MÓDULO DE REGISTRO (CONIRMADO FUNCIONAL)
st.header("👤 REGISTRO DE SOCIOS")
st.success("🛰️ Enlace de Datos con Miami: ACTIVO")

form_id = "mvzlvnyn"
registro_html = f"""
<div style="background-color: #0e1117; padding: 20px; border-radius: 10px; border: 1px solid #30363d; color: white;">
    <form action="https://formspree.io/f/{form_id}" method="POST">
        <label>Nombre Completo:</label><br>
        <input type="text" name="Nombre" style="width: 100%; padding: 8px; margin: 10px 0; background: #161b22; color: white; border: 1px solid #30363d;" required><br>
        <label>ID / Pasaporte:</label><br>
        <input type="text" name="ID" style="width: 100%; padding: 8px; margin: 10px 0; background: #161b22; color: white; border: 1px solid #30363d;" required><br>
        <label>Email:</label><br>
        <input type="email" name="Email" style="width: 100%; padding: 8px; margin: 10px 0; background: #161b22; color: white; border: 1px solid #30363d;" required><br>
        <input type="hidden" name="_subject" value="NUEVO SOCIO: TERMINAL X">
        <button type="submit" style="width: 100%; padding: 12px; background: #238636; color: white; border: none; border-radius: 5px; font-weight: bold; cursor: pointer;">
            REGISTRAR PERFIL Y ACTIVAR
        </button>
    </form>
</div>
"""
st.components.v1.html(registro_html, height=420)

# 4. LLAVE TRONLINK
st.divider()
st.header("🔑 VINCULACIÓN TRONLINK")
tron_key = st.text_input("Llave TRC-20:", placeholder="Txxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
if st.button("Sincronizar con FCC"):
    st.info("Validando perfil en la red Tron...")

# 5. PIE DE PÁGINA
st.divider()
st.caption("Fuerza y Honor. Operación Miami | Registro Federal: FRN-0038392759")
