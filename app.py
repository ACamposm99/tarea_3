import streamlit as st
import sys
import os

# Configurar paths para importaciones
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.extend([
    current_dir,
    os.path.join(current_dir, 'modulos'),
    os.path.join(current_dir, 'config')
])

# CONFIGURACIÓN DE PÁGINA (DEBE SER PRIMERO)
st.set_page_config(
    page_title="Sistema de Gestión",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Importar módulos
try:
    from modulos.login import show_login
    from modulos.menu import show_menu
    from modulos.clientes import show_clientes
    from modulos.productos import show_productos
    from modulos.ventas import show_ventas
except ImportError as e:
    st.error(f"Error de importación: {e}")
    st.stop()

def show_dashboard():
    """Muestra el dashboard principal"""
    st.title("📊 Dashboard Principal")
    
    try:
        from config.conexion import get_connection
        conn = get_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT COUNT(*) FROM clientes")
                total_clientes = cursor.fetchone()[0]
                
                cursor.execute("SELECT COUNT(*) FROM productos")
                total_productos = cursor.fetchone()[0]
                
                cursor.execute("SELECT SUM(total) FROM ventas")
                total_ventas = cursor.fetchone()[0] or 0
                
                cursor.execute("SELECT COUNT(*) FROM ventas")
                numero_ventas = cursor.fetchone()[0]
                
                # Mostrar métricas
                col1, col2, col3, col4 = st.columns(4)
                with col1: st.metric("👥 Total Clientes", total_clientes)
                with col2: st.metric("📦 Total Productos", total_productos)
                with col3: st.metric("💰 Total Ventas", f"${total_ventas:,.2f}")
                with col4: st.metric("🛒 N° de Ventas", numero_ventas)
                    
            except Exception as e:
                st.error(f"❌ Error cargando dashboard: {e}")
            finally:
                cursor.close()
                conn.close()
        else:
            st.warning("⚠️ No se pudo conectar a la base de datos")
                
    except Exception as e:
        st.error(f"❌ Error con la conexión: {e}")
    
    st.write("---")
    st.subheader("Bienvenido al Sistema de Gestión")
    st.write("""
    Utilice el menú lateral para navegar entre las diferentes secciones:
    - **👥 Gestión de Clientes**: Administre clientes
    - **📦 Gestión de Productos**: Controle inventario  
    - **💰 Gestión de Ventas**: Registre ventas
    """)

def show_config():
    """Muestra la configuración del sistema"""
    st.title("⚙️ Configuración del Sistema")
    if 'user' in st.session_state and st.session_state.user:
        st.info(f"**Usuario conectado:** {st.session_state.user['usuario']}")
    else:
        st.info("**Usuario conectado:** No disponible")
    st.info("**Base de datos:** Clever Cloud MySQL")

def main():
    """Función principal de la aplicación"""
    # Inicializar estado de sesión
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'user' not in st.session_state:
        st.session_state.user = None
    
    # Mostrar login si no está autenticado
    if not st.session_state.logged_in:
        show_login()
    else:
        # Mostrar menú y contenido principal
        selected_section = show_menu()
        if selected_section == "dashboard":
            show_dashboard()
        elif selected_section == "clientes":
            show_clientes()
        elif selected_section == "productos":
            show_productos()
        elif selected_section == "ventas":
            show_ventas()
        elif selected_section == "config":
            show_config()

if __name__ == "__main__":
    main()