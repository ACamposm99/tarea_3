import mysql.connector
import streamlit as st

def get_connection():
    """Establece conexión con la base de datos en Clever Cloud"""
    try:
        connection = mysql.connector.connect(
            host='binv7xj8v1u2v1gssf6c-mysql.services.clever-cloud.com',
            user='uyzkixypjhm2cmxv',
            password='mS3BX9yCU0pOqzrDV2wm',
            database='binv7xj8v1u2v1gssf6c',
            port=3306
        )
        return connection
    except mysql.connector.Error as e:
        st.error(f"Error conectando a la base de datos: {e}")
        return None

def verify_user(username, password):
    """Verifica las credenciales del usuario en la base de datos"""
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM Usuario WHERE usuario = %s", (username,))
            user = cursor.fetchone()
            
            if user:
                # Verificación simple de contraseña
                if user.get('password') == password:
                    return user
            return None
        except mysql.connector.Error as e:
            st.error(f"Error verificando usuario: {e}")
            return None
        finally:
            cursor.close()
            conn.close()
    return None