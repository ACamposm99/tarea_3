import streamlit as st
import sys
import os

# Configuración de página (debe ser primero)
st.set_page_config(
    page_title="Sistema de Gestión",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Configuración de paths para módulos
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

# Importación de módulos
from modulos.login import show_login
from modulos.menu import show_menu
from modulos.clientes import show_clientes
from modulos.productos import show_productos
from modulos.ventas import show_ventas

def main():
    # Inicialización de estado de sesión
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'user' not in st.session_state:
        st.session_state.user = None
    
    # Lógica de autenticación
    if not st.session_state.logged_in:
        show_login()
    else:
        # Navegación entre módulos
        selected_section = show_menu()
        
        if selected_section == "dashboard":
            show_dashboard()
        elif selected_section == "clientes":
            show_clientes()
        # ... más secciones

if __name__ == "__main__":
    main()