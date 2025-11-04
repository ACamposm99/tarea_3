def show_login():
    # Formulario de login
    with st.form("login_form"):
        username = st.text_input("Usuario")
        password = st.text_input("Contraseña", type="password")
        
        if st.form_submit_button("Iniciar Sesión"):
            user = verify_user(username, password)  # Función de BD
            
            if user:
                # Configurar sesión
                st.session_state.logged_in = True
                st.session_state.user = user
                st.success(f"Bienvenido {user['usuario']}!")
                st.rerun()  # Recargar aplicación