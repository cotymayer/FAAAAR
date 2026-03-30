import streamlit as st

st.set_page_config(
    page_title="FAAAAR - Solicitud",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo 
st.markdown("""
<style>
.stApp {
    background-color: #f4f7fb;
    font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
}

h1, h2, h3 {
    color: #0B3C5D;
}

.stButton>button {
    background-color: #1E6F9F;
    color: white;
    border-radius: 8px;
    height: 3em;
    font-size: 18px;
    font-weight: 600;
}

section[data-testid="stSidebar"] {
    background-color: #0B3C5D;
    color: white;
}

.logo {
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 300px;
    padding-top: 20px;
    padding-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# Logo grande centrado
st.image("FAAAAR2025.png", use_column_width=False, width=300, caption="")

# Encabezado
st.markdown("<h2 style='text-align: center; color: #0B3C5D;'>Formulario de Actividades - Centro de Simulación</h2>", unsafe_allow_html=True)

# Mensaje breve casual
st.markdown("<p style='text-align: center; font-size: 18px; color: #1E6F9F;'>Bienvenido! Por favor, completá con los datos requeridos para el armado de la actividad.</p>", unsafe_allow_html=True)

# Botón centrado para empezar con ícono flecha
col1, col2, col3 = st.columns([3,1,3])
with col2:
    if st.button("Empezar ➡️"):
        # Cambiar página automáticamente no está disponible nativo,
        # pero podemos guardar un flag en session_state para que el menú lateral empiece en la página 1.
        st.session_state["page"] = "1_Datos_Generales"
        st.experimental_rerun()
