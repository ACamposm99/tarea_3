def get_connection():
    try:
        return mysql.connector.connect(
            host='binv7xj8v1u2v1gssf6c-mysql.services.clever-cloud.com',
            user='uyzkixypjhm2cmxv',
            password='mS3BX9yCU0pOqzrDV2wm',
            database='binv7xj8v1u2v1gssf6c',
            port=3306
        )
    except mysql.connector.Error as e:
        st.error(f"Error de conexión: {e}")
        return None

def verify_user(username, password):
    conn = get_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Usuario WHERE usuario = %s", (username,))
        user = cursor.fetchone()
        
        if user and user['password'] == password:
            return user  # Usuario autenticado
    return None  # Autenticación fallida