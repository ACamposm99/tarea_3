import streamlit as st

def show_menu():
    """Muestra el menú lateral de navegación"""
    st.sidebar.title("🏢 Sistema de Gestión")
    
    # Mostrar información del usuario de forma segura
    if 'user' in st.session_state and st.session_state.user:
        if 'usuario' in st.session_state.user:
            nombre_usuario = st.session_state.user['usuario']
        else:
            nombre_usuario = "Usuario"
        st.sidebar.write(f"Usuario: **{nombre_usuario}**")
    else:
        st.sidebar.write("Usuario: **No identificado**")
    
    st.sidebar.write("---")
    
    # Opciones del menú
    menu_options = {
        "📊 Dashboard": "dashboard",
        "👥 Gestión de Clientes": "clientes", 
        "📦 Gestión de Productos": "productos",
        "💰 Gestión de Ventas": "ventas",
        "⚙️ Configuración": "config"
    }
    
    selected = st.sidebar.radio("Navegación", list(menu_options.keys()))
    
    # Botón de cerrar sesión
    st.sidebar.write("---")
    if st.sidebar.button("🚪 Cerrar Sesión", use_container_width=True):
        st.session_state.logged_in = False
        st.session_state.user = None
        st.rerun()
    
    return menu_options[selected]