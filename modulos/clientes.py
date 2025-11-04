def show_clientes():
    st.header("👥 Gestión de Clientes")
    
    # Pestañas para diferentes acciones
    tab1, tab2 = st.tabs(["📋 Ver Clientes", "➕ Agregar Cliente"])
    
    with tab1:
        ver_clientes()  # Mostrar lista de clientes
    
    with tab2:
        agregar_cliente()  # Formulario de nuevo cliente

def agregar_cliente():
    with st.form("cliente_form"):
        nombre = st.text_input("Nombre completo *")
        email = st.text_input("Email")
        telefono = st.text_input("Teléfono")
        
        if st.form_submit_button("💾 Guardar Cliente"):
            if nombre:  # Validación básica
                # Insertar en BD
                cursor.execute(
                    "INSERT INTO clientes (nombre, email, telefono) VALUES (%s, %s, %s)",
                    (nombre, email, telefono)
                )
                conn.commit()
                st.success("✅ Cliente agregado")

