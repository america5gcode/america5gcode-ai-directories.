import sqlite3
import hashlib

if __name__ == "__main__":
    conn = sqlite3.connect("terminal_x_network.db")
    conn.execute('''CREATE TABLE IF NOT EXISTS usuarios_red 
                   (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    usuario TEXT UNIQUE, password TEXT)''')
    conn.close()

    print("\n--- 🔐 REGISTRO GENERAL: TERMINAL X ---")
    user = input("Nombre de Usuario: ")
    pw = input("Contraseña: ")
    pw_hash = hashlib.sha256(pw.encode()).hexdigest()
    
    try:
        conn = sqlite3.connect("terminal_x_network.db")
        conn.execute("INSERT INTO usuarios_red (usuario, password) VALUES (?, ?)", (user, pw_hash))
        conn.commit()
        conn.close()
        print(f"🚀 REGISTRO EXITOSO: Bienvenido a la Red, {user}.")
    except:
        print(f"🔑 ACCESO: Bienvenido de nuevo, {user}.")

    print("\n🏆 SISTEMA OPERATIVO Y SOBERANO
