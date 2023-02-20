# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import pandas as pd
import altair as alt

# Definir las preguntas y constructos
preguntas_constr_1 = [
    "How often have you felt sad or down in the dumps in the past two weeks?",
    "How much have you been bothered by feeling hopeless or helpless in the past two weeks?",
    "How often have you felt like a failure or that you have let yourself or your family down in the past two weeks?",
    "How much have you been bothered by having little interest or pleasure in doing things in the past two weeks?",
    "How often have you felt down on yourself or your life in the past two weeks?"
]
preguntas_constr_2 = [
    "How motivated have you felt to make positive changes in your life in the past two weeks?",
    "How often have you taken specific steps to make positive changes in your life in the past two weeks?",
    "How much do you believe you can make positive changes in your life in the past two weeks?"
]

# Crear la aplicación Streamlit
def main():
    st.set_page_config(page_title="Test to Assess for Depression", page_icon=":pencil2:")
    st.title("Test to Assess for Depression")
    st.write("Instructions: Please carefully read each question and select the answer that best reflects your experience over the past two weeks. ")

    # Inicializar las sumas de los constructos
    suma_constr_1 = 0
    suma_constr_2 = 0

    # Crear un loop para iterar a través de las preguntas y respuestas de cada constructo
    for i, pregunta in enumerate(preguntas_constr_1):
        respuesta = st.slider(pregunta, -3, 3, value = 0)
        suma_constr_1 += respuesta
    suma_constr_1 = suma_constr_1 * -1

    for i, pregunta in enumerate(preguntas_constr_2):
        respuesta = st.slider(pregunta, -3, 3, value = 0)
        suma_constr_2 += respuesta
    if st.button("Submit"):
        # Mostrar las sumas de cada constructo
        st.write("Depressive symptons: ", suma_constr_1)
        st.write("Motivation to change: ", suma_constr_2)
    
        # Crear un dataframe con las sumas de cada constructo
        datos = pd.DataFrame({
            'Depressive symptons': ([suma_constr_1]),
            'Motivation to change': [suma_constr_2]
        })
    
        # Crear un gráfico de dispersión en dos ejes con las puntuaciones en cada constructo y ejes fijos
        grafico = alt.Chart(datos).mark_circle(
            size=100,
            color='red'
        ).encode(
        x=alt.X('Depressive symptons', axis=alt.Axis(titleFontSize=18, labelFontSize=16, values=[0], ticks=True, grid=True), scale=alt.Scale(domain=(-25, 25))),
        y=alt.Y('Motivation to change', axis=alt.Axis(titleFontSize=18, labelFontSize=16, values=[0], ticks=True, grid=True), scale=alt.Scale(domain=(-25, 25)))
        ).properties(
            width=600,
            height=500,
            title={
                "text": "Scatter plot to assess for depression",
                "fontSize": 24,
                "subtitleFontSize": 20
            }
        )
    
        # Mostrar el gráfico de dispersión
        st.write(grafico)

if __name__ == '__main__':
    main()