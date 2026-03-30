import streamlit as st

st.header("Datos Generales")

st.session_state.nombre = st.text_input("Nombre y apellido")
st.session_state.email = st.text_input("Email")
st.session_state.actividad = st.text_input("Nombre de la actividad")
st.session_state.fecha = st.date_input("Fecha")
st.session_state.cupo = st.number_input("Cupo", min_value=1)
