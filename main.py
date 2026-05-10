import streamlit as st

# 1. IDENTIDAD Y COORDINADAS DE SEDE
st.set_page_config(page_title="Terminal X - Mando Miami", layout="wide")

st.title("🏗️ TERMINAL X: RASCACIELOS GRÁFICO")
st.markdown("### **PHELPS TUCKER GROUP LLC**")

# Bloque de Identidad Federal (Sede y Contacto)
st.markdown(f"""
<div style="background-color: #161b22; padding: 20px; border-radius: 10px; border-left: 5px solid #238636; color: white;">
    <p>📍 <strong>DIRECCIÓN SEDE MIAMI:</strong> 8345 NW 66st Miami, Florida, USA 33166</p>
    <p>📧 <strong>CORREO ELECTRÓNICO:</strong> fccinternationalus@gmail.com</p>
    <p>📜 <strong>REGISTRO FEDERAL:</strong> FRN-0038392759 | <strong>ESTATUS:</strong> ACTIVO</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# 2. MATRIZ DE PLANES Y RUTAS DE ASCENSO
st.header("📋 OFERTA DE PLANES Y ESCALABILIDAD")
col1, col2, col3 = st.columns(3)

with col1:
    st.info("### PLAN FREE")
    st.write("**Estatus:** Patrocinado")
    st.markdown("- 🚀 **A PRO:** 200 Referidos")
    st.markdown("- 💎 **A PLATINO:** 50 Anuncios ($5 c/u)")
    st.caption("Denominación: ACCESO FREE")

with col2:
    st.success("### PLAN PRO")
    st.write("**Inversión:** $200 (6m) / $100 (Anual)")
    st.markdown("- 🛡️ **Estatus:** Registro Federal")
    st.markdown("- 💎 **A PLATINO:** Afiliación al Club")
    st.caption("Denominación: REGISTRO PRO")

with col3:
    st.warning("### PLAN PLATINO")
    st.write("**Inversión Mínima:** $400,000")
    st.markdown("- 🏦 **Nivel:** Wall Street Direct")
    st.markdown("- ⭐ **Jerarquía:** Máxima Soberanía")
    st.caption("Denominación: MANDO PLATINO")

st.divider()

# 3. REGISTRO DE PERFIL (MÓDULO DE ACCIÓN)
st.header("👤 REGISTRO DE PERFIL")
form_html = """
<div style="background-color: #0d1117; padding: 20px; border-radius: 10px; border: 1px solid #30363d; color: white;">
    <form action="https://formspree.io/f/mvzlvnyn" method="POST">
        <label>NOMBRE COMPLETO:</label><br>
        <input type="text" name="name" style="width: 100%; padding: 10px; margin: 10px 0; background: #161b22; color: white; border: 1px solid #30363d;" required><br>
        <label>ID / PASAPORTE:</label><br>
        <input type="text" name="id" style="width: 100%; padding: 10px; margin: 10px 0; background: #161b22; color: white; border: 1px solid #30363d;" required><br>
        <input type="hidden" name="_subject" value="ACTIVACIÓN FEDERAL - TERMINAL X">
        <button type="submit" style="width: 100%; padding: 15px; background-color: #238636; color: white; border: none; border-radius: 5px; font-weight: bold; cursor: pointer;">
            VERIFICAR Y ACTIVAR PERFIL
        </button>
    </form>
</div>
"""
st.components.v1.html(form_html, height=350)

st.divider()

# 4. NODOS DE INTELIGENCIA (ENLACES DE MANDO)
st.header("🌐 DIRECTORIO DE POTENCIA (ENLACES PROPIOS)")

enlaces_oficiales = [
    {"página": "Terminal X - IA Central", "desc": "Núcleo neural de inteligencia artificial y despliegue gráfico.", "url": "https://v0-ia-creation-system.vercel.app/"},
    {"página": "Bóveda de Red & Anuncios", "desc": "Sistema de monetización y gestión de tráfico para anunciantes.", "url": "https://www.profitablecpmratenetwork.com/qnhh1xucd?key=6a064f4f3516c4a968449ff9774f2d05"},
    {"página": "Registro Federal Miami", "desc": "Portal de validación oficial para socios bajo estándares FCC.", "url": "https://formspree.io/f/mvzlvnyn"},
    {"página": "Chat de Desarrollo V0", "desc": "Canal técnico para ajustes de arquitectura y diseño en tiempo real.", "url": "https://v0.app/chat/v0-terminal-x-911-tao-hbr75to2yWl"},
    {"página": "Repositorio Código Fuente", "desc": "Almacén maestro de seguridad y respaldo de datos en GitHub.", "url": "https://github.com/fccinternationalus/TerminalX"}
]

for e in enlaces_oficiales:
    with st.expander(f"🔹 {e['página']}"):
        st.write(f"**Propósito:** {e['desc']}")
        st.link_button(f"Sincronizar con {e['página']}", e['url'], use_container_width=True)

st.divider()
st.caption("Fuerza y Honor. Operación Miami 33166 | Registro FRN-0038392759")
