# app.py
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Vehículos - Dashboard", layout="wide")

# 1) Cargar datos (ajusta la ruta si tu CSV está en otra carpeta)
df = pd.read_csv("vehicles_us.csv")

# 2) Encabezado
st.header("Dashboard de anuncios de venta de coches")

# 3) Botón -> Histograma
hist_button = st.button("Construir histograma (odometer)")
if hist_button:
    st.write("Creación de un histograma para la columna **odometer**")
    fig = px.histogram(df, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# 4) Botón -> Dispersión
scatter_button = st.button("Construir dispersión (odometer vs price)")
if scatter_button:
    st.write("Gráfico de dispersión **odometer** vs **price**")
    fig2 = px.scatter(df, x="odometer", y="price", trendline="ols")
    st.plotly_chart(fig2, use_container_width=True)

# --- (Opcional) Versión con checkboxes en lugar de botones ---
st.subheader("Versión con casillas de verificación (opcional)")

if st.checkbox("Mostrar histograma (odometer)"):
    st.write("Creación de un histograma para la columna **odometer**")
    fig = px.histogram(df, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if st.checkbox("Mostrar dispersión (odometer vs price)"):
    st.write("Gráfico de dispersión **odometer** vs **price**")
    fig2 = px.scatter(df, x="odometer", y="price", trendline="ols")
    st.plotly_chart(fig2, use_container_width=True)