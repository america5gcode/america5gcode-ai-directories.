import streamlit as st

# 1. IDENTIDAD Y SEDE (LO QUE NO APARECÍA)
st.set_page_config(page_title="Terminal X - Mando Miami", layout="wide")

st.title("🏗️ TERMINAL X: RASCACIELOS GRÁFICO")
st.markdown("### **PHELPS TUCKER GROUP LLC**")

# Bloque de Información Crítica (Sede y Correo)
st.markdown(f"""
<div style="background-color: #161b22; padding: 20px; border-radius: 10px; border-left: 5px solid #238636; color: white;">
    <p>📍 <strong>DIRECCIÓN SEDE MIAMI:</strong> 8345 NW 66st Miami, Florida, USA 33166</p>
    <p>📧 <strong>CORREO ELECTRÓNICO:</strong> fccinternationalus@gmail.com</p>
    <p>📜 <strong>REGISTRO FEDERAL:</strong> FRN-0038392759 | <strong>ESTATUS:</strong> VERIFICADO</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# 2. LOS 5 ENLACES DE INTELIGENCIA (LAS MANOS DEL PROYECTO)
st.header("🌐 DIRECTORIO DE POTENCIA (ENLACES DE MANDO)")

enlaces_reales = [
    {"página": "Bóveda de Red & Anuncios", "desc": "Sistema de monetización y gestión de tráfico para anunciantes.", "url": "https://www.profitablecpmratenetwork.com/qnhh1xucd?key=6a064f4f3516c4a968449ff9774f2d05"},
    {"página": "Chat de Desarrollo V0", "desc": "Canal técnico para ajustes de arquitectura y diseño en tiempo real.", "url": "https://v0.app/chat/v0-terminal-x-911-tao-hbr75to2yWl"},
    {"página": "Registro Federal Miami", "desc": "Portal de validación oficial para socios bajo estándares FCC.", "url": "https://formspree.io/f/mvzlvnyn"},
    {"página": "Repositorio Código Fuente", "desc": "Almacén maestro de seguridad y respaldo de datos en GitHub.", "url": "https://github.com/fccinternationalus/TerminalX"},
    {"página": "Terminal X - IA Central", "desc": "Núcleo neural de inteligencia artificial y despliegue gráfico.", "url": "https://v0-ia-creation-system.vercel.app/"}
]

for e in enlaces_reales:
    with st.expander(f"🔹 {e['página']}"):
        st.write(f"**Propósito:** {e['desc']}")
        st.link_button(f"Sincronizar con {e['página']}", e['url'])

st.divider()
st.caption("Fuerza y Honor. Operación Miami 33166 | Registro FRN-0038392759")
