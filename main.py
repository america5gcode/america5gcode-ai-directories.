import streamlit as st

# 1. CONFIGURACIÓN DE IDENTIDAD Y ESTILO
st.set_page_config(page_title="Terminal X - Mando Miami", layout="wide")

# 2. CABECERA CORPORATIVA DE ALTO NIVEL
with st.container():
    col_logo, col_info = st.columns([1.2, 3])
    with col_logo:
        # Escudo oficial de Phelps Tucker Group
        st.image("https://i.ibb.co/6P0qMhR/PHELPS-TUCKER-GROUP-LOGO.jpg", width=250) 
    with col_info:
        st.title("🏗️ TERMINAL X: RASCACIELOS GRÁFICO")
        st.markdown("## **PHELPS TUCKER GROUP LLC**")
        st.write("📍 **Sede Central:** 8345 NW 66st Miami, Florida, USA 33166")
        st.write("📧 **Correo de Mando:** fccinternationalus@gmail.com")
        st.caption("Registro Federal: FRN-0038392759 | Registro FCC: Activo | Red: TRON (TRC-20)")

st.divider()

# 3. FORMULARIO DE REGISTRO CON ENVÍO REAL A MIAMI
st.header("👤 REGISTRO OBLIGATORIO DE SOCIOS")
st.info("Trámite indispensable para validación ante el IRS y activación en la Red Tron.")

# URL de Formspree integrada
form_url = "https://formspree.io/f/mvzlvnyn"

# Estructura HTML para el envío directo de datos
registro_html = f"""
<div style="background-color: #0e1117; padding: 25px; border-radius: 15px; border: 1px solid #30363d; font-family: sans-serif;">
    <form action="{form_url}" method="POST">
        <label style="color: #8b949e; font-weight: bold; font-size: 14px;">NOMBRE COMPLETO:</label><br>
        <input type="text" name="nombre" placeholder="Ej: Gustavo Sanabria" style="width: 100%; padding: 10px; margin: 8px 0; background: #161b22; border: 1px solid #30363d; color: white; border-radius: 5px;" required><br><br>
        
        <label style="color: #8b949e; font-weight: bold; font-size: 14px;">DOCUMENTO DE IDENTIDAD / PASAPORTE:</label><br>
        <input type="text" name="identidad" placeholder="ID Legal" style="width: 100%; padding: 10px; margin: 8px 0; background: #161b22; border: 1px solid #30363d; color: white; border-radius: 5px;" required><br><br>
        
        <label style="color: #8b949e; font-weight: bold; font-size: 14px;">CORREO ELECTRÓNICO:</label><br>
        <input type="email" name="_replyto" placeholder="socio@ejemplo.com" style="width: 100%; padding: 10px; margin: 8px 0; background: #161b22; border: 1px solid #30363d; color: white; border-radius: 5px;" required><br><br>
        
        <label style="color: #8b949e; font-weight: bold; font-size: 14px;">PLAN ELEGIDO:</label><br>
        <select name="plan" style="width: 100%; padding: 10px; margin: 8px 0; background: #161b22; border: 1px solid #30363d; color: white; border-radius: 5px;">
            <option value="Free">Versión Free (Patrocinada)</option>
            <option value="Pro">Versión Pro (FCC/IRS)</option>
            <option value="Platino">Versión Platino ($400k)</option>
        </select><br><br>
        
        <label style="color: #8b949e; font-size: 12px;">
            <input type="checkbox" required> Certifico la veracidad de los datos para el Registro Federal FRN-0038392759.
        </label><br><br>
        
        <input type="hidden" name="_subject" value="NUEVO SOCIO REGISTRADO - TERMINAL X">
        <button type="submit" style="width: 100%; padding: 12px; background-color: #238636; color: white; border: none; border-radius: 5px; font-weight: bold; cursor: pointer; text-transform: uppercase;">
            Guardar Perfil y Enviar a Miami
        </button>
    </form>
</div>
"""

# Renderizado del formulario
st.components.v1.html(registro_html, height=520)

st.divider()
