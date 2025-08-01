import streamlit as st
import streamlit.components.v1 as components

# Menú lateral para seleccionar la página
page = st.sidebar.selectbox("Selecciona la página", ["Editor HTML", "Visualizador"])

# Estado compartido para guardar el código HTML entre páginas
if "html_code" not in st.session_state:
    st.session_state.html_code = ""

if page == "Editor HTML":
    st.title("Editor de Código HTML")
    # Área de texto para pegar/modificar el código HTML
    html_input = st.text_area("Pega aquí el código HTML", st.session_state.html_code, height=500)

    if st.button("Guardar"):
        st.session_state.html_code = html_input
        st.success("Código guardado correctamente")

elif page == "Visualizador":
    st.title("Visualización de la Página HTML")
    if st.session_state.html_code.strip() != "":
        # Renderiza el HTML sin mostrar el código
        components.html(st.session_state.html_code, height=800, scrolling=True)
    else:
        st.info("No hay código HTML guardado. Ve a la página 'Editor HTML' para pegar y guardar código.")




