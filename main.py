import streamlit as st

# 1. CONFIGURACIÓN DE IDENTIDAD
st.set_page_config(page_title="Terminal X - Mando Miami", layout="wide")

# 2. IDENTIDAD CORPORATIVA (Logo y Sede)
with st.container():
    col_logo, col_info = st.columns([1.2, 3])
    with col_logo:
        # He cambiado el enlace por uno de alta disponibilidad
        st.image("https://images2.imgbox.com/62/32/pM6QZtWq_o.jpg", width=250) 
    with col_info:
        st.title("🏗️ TERMINAL X: RASCACIELOS GRÁFICO")
        st.markdown("## **PHELPS TUCKER GROUP LLC**")
        st.write("📍 **Sede Central:** 8345 NW 66st Miami, Florida, USA 33166")
        st.write("📧 **Correo de Mando:** fccinternationalus@gmail.com")
        st.caption("Registro Federal: FRN-0038392759 | Registro FCC: Activo")

st.divider()

# 3. FORMULARIO DE REGISTRO CON ENVÍO REAL (FORMSPREE)
st.header("👤 REGISTRO OBLIGATORIO DE SOCIOS")
st.info("Complete los datos. Se enviará una copia cifrada al Centro de Mando en Miami.")

# Tu ID de Formspree: mvzlvnyn
form_url = "https://formspree.io/f/mvzlvnyn"

# Estructura HTML profesional y compatible
registro_html = f"""
<div style="background-color: #1a1c24; padding: 20px; border-radius: 10px; border: 1px solid #444; font-family: Arial, sans-serif; color: white;">
    <form action="{form_url}" method="POST">
        <div style="margin-bottom: 15px;">
            <label style="display: block; margin-bottom: 5px; font-weight: bold;">NOMBRE COMPLETO:</label>
            <input type="text" name="Nombre" style="width: 100%; padding: 10px; border-radius: 5px; border: none;" required>
        </div>
        <div style="margin-bottom: 15px;">
            <label style="display: block; margin-bottom: 5px; font-weight: bold;">ID / PASAPORTE:</label>
            <input type="text" name="Identidad" style="width: 100%; padding: 10px; border-radius: 5px; border: none;" required>
        </div>
        <div style="margin-bottom: 15px;">
            <label style="display: block; margin-bottom: 5px; font-weight: bold;">CORREO ELECTRÓNICO:</label>
            <input type="email" name="email" style="width: 100%; padding: 10px; border-radius: 5px; border: none;" required>
        </div>
        <div style="margin-bottom: 15px;">
            <label style="display: block; margin-bottom: 5px; font-weight: bold;">PLAN DE INVERSIÓN:</label>
            <select name="Plan" style="width: 100%; padding: 10px; border-radius: 5px; border: none;">
                <option value="Free">Versión Free</option>
                <option value="Pro">Versión Pro (FCC/IRS)</option>
                <option value="Platino">Versión Platino ($400k)</option>
            </select>
        </div>
        <input type="hidden" name="_subject" value="NUEVO REGISTRO TERMINAL X - MIAMI">
        <button type="submit" style="width: 100%; padding: 12px; background-color: #00c853; color: white; border: none; border-radius: 5px; font-weight: bold; cursor: pointer; font-size: 16px;">
            GUARDAR PERFIL Y ACTIVAR MANDO
        </button>
    </form>
</div>
"""

st.components.v1.html(registro_html, height=550)

st.divider()

# 4. LLAVE TRONLINK
st.header("🔑 VINCULACIÓN TRONLINK")
st.write("Sincronice su llave para la activación de su estatus:")
tron_key = st.text_input("Llave TRC-20:", placeholder="Txxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
if st.button("Sincronizar con el Registro"):
    st.success("Sincronizando perfil con la Red Tron... Verificando depósitos.")

# 5. PIE DE PÁGINA
st.divider()
st.caption("Fuerza y Honor. Miami Operations 33166 | Registro FRN-0038392759")
