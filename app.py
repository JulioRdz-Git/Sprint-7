import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Hola Sprint 7 🚀")
st.write("Tu entorno y Streamlit funcionan correctamente.")

df = pd.DataFrame({
    "x": [1, 2, 3, 4],
    "y": [10, 20, 30, 40]
})

fig = px.line(df, x="x", y="y", title="Gráfico de prueba")
st.plotly_chart(fig)