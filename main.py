import sqlite3
import hashlib
import sys

# =========================================================
#       RED TERMINAL X - SISTEMA OPERATIVO GLOBAL
#       ARQUITECTURA: PHELPS TUCKER GROUP
# =========================================================

def portal_soberano(patrocinante="Socio Phelps Tucker"):
    print("\n" + "═"*60)
    print("         🌐 RED TERMINAL X: EL RASCACIELOS DIGITAL 🌐")
    print("═"*60)
    print(f"📢 PATROCINIO ACTUAL: {patrocinante}")
    print("💰 Ticket de Anuncio: $5 (Puerta al Plan Platino)")
    print("═"*60)

def menu_planes_soberanos():
    print("\n" + "📊" + "═"*20 + " ESCALERA DE PODER " + "═"*20 + "📊")
    print("1. 🆓 PLAN FREE")
    print("   ↳ Exploración IA Ilimitada (Patrocinio de Terceros)")
    print("\n2. 💎 PLAN PRO (Formalización de Marketing)")
    print("   ↳ Registro FCC/IRS + Crédito Agilizado Banco Mundial")
    print("   ↳ COSTO: 6 Meses: $200 | 1 Año: $100 (OFERTA)")
    print("\n3. 🏛️ PLAN PLATINO (Alta Gerencia)")
    print("   ↳ Acceso Directo a Wall Street & Bolsa de Valores")
    print("   ↳ ENTRADA/PUJA: $400,000")
    print("-" * 60)
    print("🚀 BONO ESTRATÉGICO: 50 Anuncios en Plan Free = PRE-INSCRIPCIÓN PLATINO")
    print("═"*60)

def inicializar_infraestructura():
    try:
        conn = sqlite3.connect("terminal_x_network.db")
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios_red 
                         (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                          usuario TEXT UNIQUE, 
                          nivel TEXT DEFAULT 'FREE', 
                          ads_count INTEGER DEFAULT 0)''')
        conn.commit()
        conn.close()
    except Exception as e:
        pass

if __name__ == "__main__":
    # Cimientos de la Red
    inicializar_infraestructura()

    # Interfaz de Usuario en Render
    portal_soberano()
    menu_planes_soberanos()
    
    print("\n--- 🔐 CONTROL DE ACCESO SOBERANO ---")
    try:
        user = input("Usuario: ")
        print(f"\n📡 Conectando a {user} con la infraestructura global...")
        print("ESTADO: EN LÍNEA | RESPALDO BANCO MUNDIAL & WALL STREET")
        print("\n[✔] Sistema Operacional. Bienvenido al Rascacielos.")
    except EOFError:
        # Manejo para entornos sin input interactivo (como algunos logs de Render)
        print("\nSISTEMA ESPERANDO CONEXIÓN REMOTA...")

import streamlit as st
import sys

# --- TERMINAL X: GRAPHICAL INTERFACE CONFIGURATION ---
st.set_page_config(
    page_title="Terminal X | Phelps Tucker Group",
    page_icon="🌐",
    layout="centered"
)

def main():
    # HEADER - THE SKYSCRAPER ENTRANCE
    st.title("🌐 TERMINAL X: THE DIGITAL SKYSCRAPER")
    st.subheader("Official Operating System - Phelps Tucker Group")
    st.write("---")
    
    # SECURITY CUSTOMS (ADUANA DE SEGURIDAD)
    st.markdown("### 🛡️ SECURITY CUSTOMS & ETHICAL PROTOCOL")
    st.info("NOTICE: All users must be linked to the Artificial Intelligence Industry.")
    st.warning("STRICT PROHIBITION: Malicious, obscene, or adult-rated (X) content.")

    # USER PROFILE INPUTS
    with st.form("ai_registration_form"):
        company_name = st.text_input("📝 AI Company or Project Name:")
        ai_specialty = st.text_input("📝 AI Industry Specialty (e.g., NLP, Sales Intelligence, ML):")
        project_intent = st.text_area("📝 Brief description of your AI operations:")
        
        submit_button = st.form_submit_button("VALIDATE PROFILE")

    if submit_button:
        if not company_name or not ai_specialty or not project_intent:
            st.error("⚠️ All fields are mandatory for international validation.")
        else:
            # THE SENTINEL: PURITY FILTER
            # This filter blocks malicious or inappropriate terms automatically
            blacklist = ["porno", "xxx", "obsceno", "malware", "virus", "sex", "pornographic"]
            content_to_check = (company_name + ai_specialty + project_intent).lower()
            
            if any(term in content_to_check for term in blacklist):
                st.error("❌ CRITICAL ERROR: ETHICAL VIOLATION DETECTED.")
                st.error("🛡️ THE SENTINEL HAS TERMINATED THIS CONNECTION.")
                # Ethical block simulated by stopping execution for the user
            else:
                st.success("✅ PROFILE OFFICIALLY VALIDATED BY PHELPS TUCKER GROUP")
                st.balloons()
                st.markdown(f"### 🚀 Welcome, {company_name}!")
                st.write(f"Your project in **{ai_specialty}** is now integrated into the Terminal X Sovereign Network.")
                
                # ACCESS TO DATA (MINA DE ORO PREVIEW)
                st.write("---")
                st.markdown("#### ⛏️ GOLD MINE STATUS: ACTIVE")
                st.success("International data flows (IBRD & Latin America) are now synchronized.")

if __name__ == "__main__":
    main()

# =========================================================
# FINAL DEL DOCUMENTO SOBERANO
# =========================================================
