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
    "Question 1- How often have you felt sad or down in the dumps in the past two weeks?",
    "Question 2- How much have you been bothered by feeling hopeless or helpless in the past two weeks?",
    "Question 3- How often have you felt like a failure or that you have let yourself or your family down in the past two weeks?",
    "Question 4- How much have you been bothered by having little interest or pleasure in doing things in the past two weeks?",
    "Question 5- How often have you felt down on yourself or your life in the past two weeks?"
]
preguntas_constr_2 = [
    "Question 6- How motivated have you felt to make positive changes in your life in the past two weeks?",
    "Question 7- How often have you taken specific steps to make positive changes in your life in the past two weeks?",
    "Question 8- How much do you believe you can make positive changes in your life in the past two weeks?"
]

# Crear la aplicación Streamlit
def main():
    st.set_page_config(page_title="Test to Assess for Depression", page_icon=":pencil2:")
    st.title("Test to Assess for Depression")
    st.write("Instructions: Please carefully read each question and select the answer that best reflects your experience over the past two weeks. ")

    st.markdown("<style>.css-1s80s3i {{margin-bottom: 20px;}}</style>", unsafe_allow_html=True)


    # Inicializar las sumas de los constructos
    suma_constr_1 = 0
    suma_constr_2 = 0
    
    # Define the mapping from text options to numerical values
    option_values = {
    'Not at all': -3,
    'Several days a week': -2,
    'Half the days': -1,
    'Most days': 1,
    'Every day': 2,
    'All the time': 3
    }
    
    # Crear un loop para iterar a través de las preguntas y respuestas de cada constructo
    for i, pregunta in enumerate(preguntas_constr_1):
        
        # Use markdown to display the question in a bigger font
        st.markdown("<p style='font-size: 20px'>{}</p>".format(pregunta), unsafe_allow_html=True)
        
        # Use select_slider with text options, and then convert the response to a number using the mapping
        respuesta = st.select_slider(" ", options=list(option_values.keys()), key=f"constr_1_{i}")
        respuesta_num = option_values[respuesta]

        # Add margin to the select_slider element
        st.markdown("<style>.css-1s80s3i {{margin-bottom: 20px;}}</style>", unsafe_allow_html=True)

        suma_constr_1 += respuesta_num
        suma_constr_1 = suma_constr_1 * -1

    for i, pregunta in enumerate(preguntas_constr_2):
        st.markdown("<p style='font-size: 20px'>{}</p>".format(pregunta), unsafe_allow_html=True)
                
        respuesta = st.select_slider(" ", options=list(option_values.keys()), key=f"constr_2_{i}")
        respuesta_num = option_values[respuesta]
        
        # Add margin to the select_slider element
        st.markdown("<style>.css-1s80s3i {{margin-bottom: 20px;}}</style>", unsafe_allow_html=True)

        suma_constr_2 += respuesta_num
        suma_constr_2 = suma_constr_2
        
    if st.button("Submit"):
        # Mostrar las sumas de cada constructo
        # st.write("Depressive symptons: ", suma_constr_1)
        # st.write("Motivation to change: ", suma_constr_2)
    
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
        x=alt.X('Depressive symptons', axis=alt.Axis(titleFontSize=18, labelFontSize=16, values=[0], ticks=True, grid=True), scale=alt.Scale(domain=(-10, 10))),
        y=alt.Y('Motivation to change', axis=alt.Axis(titleFontSize=18, labelFontSize=16, values=[0], ticks=True, grid=True), scale=alt.Scale(domain=(-10, 10)))
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
