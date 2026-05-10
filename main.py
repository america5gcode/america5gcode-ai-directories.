import streamlit as st

st.set_page_config(page_title="Terminal X - Restauración", layout="wide")

# CABECERA DE EMERGENCIA FEDERAL
st.error("🚨 ALERTA DE SISTEMA: RECONECTANDO NODOS DE INTELIGENCIA")
st.markdown(f"""
    **SEDE MIAMI:** 8345 NW 66st Miami, FL 33166 | **REGISTRO:** FRN-0038392759
    **CORREO:** fccinternationalus@gmail.com
""")

st.divider()

# REANCLAJE FORZADO DE ENLACES (ESTO NO PUEDE FALLAR)
st.header("🌐 ACCESO DIRECTO A LAS MANOS (NIVELES DE MANDO)")

# Definimos los enlaces con su descripción oficial
mando = [
    {"página": "Terminal X - IA Central", "url": "https://v0-ia-creation-system.vercel.app/", "desc": "Núcleo de IA y despliegue gráfico."},
    {"página": "Bóveda de Red & Anuncios", "url": "https://www.profitablecpmratenetwork.com/qnhh1xucd?key=6a064f4f3516c4a968449ff9774f2d05", "desc": "Monetización y tráfico ($5/u)."},
    {"página": "Registro Federal Miami", "url": "https://formspree.io/f/mvzlvnyn", "desc": "Validación de socios FCC."},
    {"página": "Repositorio GitHub (CÓDIGO)", "url": "https://github.com/fccinternationalus/TerminalX", "desc": "Almacén maestro de seguridad."},
    {"página": "Chat de Desarrollo V0", "url": "https://v0.app/chat/v0-terminal-x-911-tao-hbr75to2yWl", "desc": "Ajustes técnicos en vivo."}
]

for m in mando:
    with st.expander(f"⚙️ ENTRAR A: {m['página']}"):
        st.write(f"**Misión:** {m['desc']}")
        # Botón de seguridad reforzada
        st.link_button(f"Sincronizar {m['página']}", m['url'], use_container_width=True)

st.divider()
st.info("Nota del Centinela: Si un enlace pide login, es porque GitHub requiere re-validar su perfil federal.")
