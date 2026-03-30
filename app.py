import streamlit as st

# Configuración de la página, incluyendo favicon
st.set_page_config(
    page_title="FAAAAR - Formulario de Actividades",
    page_icon="logo-faaaar.png",  # logo para la pestaña
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo personalizado
st.markdown("""
<style>
.stApp {
    background-color: #f4f7fb;
    font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
}

/* Encabezados más grandes */
h1 {
    font-size: 48px;
    color: #0B3C5D;
    text-align: center;
}
h2 {
    font-size: 32px;
    color: #0B3C5D;
    text-align: center;
}

/* Botones con hover */
.stButton>button {
    background-color: #1E6F9F;
    color: white;
    border-radius: 12px;
    height: 3em;
    font-size: 25px;
    font-weight: 600;
    box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
    transition: background-color 0.3s ease;
}
.stButton>button:hover {
    background-color: #145374;
}

/* Sidebar personalizado */
section[data-testid="stSidebar"] {
    background-color: #0B3C5D;
    color: white !important;
    padding-top: 20px;
}
section[data-testid="stSidebar"] h2 {
    color: #ffffff;
}

/* Logo encabezado */
.logo-header {
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 30px;  
    padding-top: 10px;
    padding-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# Logo centrado como encabezado
st.image("FAAAAR2025.png", use_column_width=False, width=30, caption="", clamp=False)

#Título
st.markdown(
    "<h1 style='text-align: center; color: #0B3C5D; font-size: 70px;'>Formulario de Actividades - Centro de Simulación</h1>",
    unsafe_allow_html=True
)

#Bienvenida
st.markdown(
    "<p style='text-align: center; font-size: 30px; color: #1E6F9F;'>¡Bienvenido/a! Completá los datos solicitados para organizar tu actividad de manera eficiente.</p>", 
    unsafe_allow_html=True
)

# Botón centrado para empezar
col1, col2, col3 = st.columns([3,1,3])
with col2:
    if st.button("Empezar ➡️"):
        st.session_state["page"] = "1_Datos_Generales"
        st.experimental_rerun()
