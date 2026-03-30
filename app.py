import streamlit as st

# Configuración de la página, incluyendo favicon
st.set_page_config(
    page_title="FAAAAR - Formulario de Actividades",
    page_icon="FAAAAR2025.png",  # logo para la pestaña
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo personalizado con mejoras
st.markdown("""
<style>
.stApp {
    background-color: #f4f7fb;
    font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
}

/* Encabezados centrados y color */
h1, h2, h3 {
    color: #0B3C5D;
    text-align: center;
}

/* Botones atractivos con hover y sombra */
.stButton>button {
    background-color: #1E6F9F;
    color: white;
    border-radius: 12px;
    height: 3em;
    font-size: 18px;
    font-weight: 600;
    box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
    transition: background-color 0.3s ease;
}
.stButton>button:hover {
    background-color: #145374;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #0B3C5D;
    color: white;
    padding-top: 20px;
}

/* Logo encabezado */
.logo-header {
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 120px;  /* tamaño discreto */
    padding-top: 10px;
    padding-bottom: 10px;
}

/* Logo de sidebar (opcional) */
.sidebar-logo {
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 80px;
    padding-top: 10px;
    padding-bottom: 10px;
}

/* Card para mensaje de bienvenida */
.card {
    background-color: white;
    border-radius: 12px;
    padding: 20px;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# Logo centrado como encabezado
st.image("FAAAAR2025.png", use_column_width=False, width=120, caption="", clamp=False)

# Encabezado principal
st.markdown("<h2>Formulario de Actividades - Centro de Simulación</h2>", unsafe_allow_html=True)

# Mensaje de bienvenida dentro de un card
st.markdown(
    '<div class="card"><p style="text-align: center; font-size: 18px; color: #1E6F9F;">¡Bienvenido/a! Completá los datos solicitados para organizar tu actividad.</p></div>',
    unsafe_allow_html=True
)

# Botón centrado para empezar
col1, col2, col3 = st.columns([3,1,3])
with col2:
    if st.button("Empezar ➡️"):
        st.session_state["page"] = "1_Datos_Generales"
        st.experimental_rerun()
