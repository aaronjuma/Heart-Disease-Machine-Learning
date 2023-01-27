from time import sleep
from turtle import setx
import streamlit as st
import json
import Utils

with open('dataset/columns.json') as json_file:
    data = json.load(json_file)

header = st.container()

with header:
    st.title("Heart Disease Predictor")

    # TODO: Weight and Height BMI CALCUALTIONS UNDER

    status = st.radio(label = 'Select your height/weight format: ',
                        options = ['kgs/cms', 'lbs/inches'])

    if status == 'kgs/cms':
        weight = st.number_input(label = "Enter your weight (in kgs)",
                                    value = 80,
                                    min_value = 25,
                                    max_value = 700,
                                    step = 5)
    
        height = st.number_input(label = "Enter your height (in cm)",
                                    value = 150,
                                    min_value = 90,
                                    max_value = 250,
                                    step = 5)
    else:
        weight = st.number_input(label = "Enter your weight (in lbs)",
                                    value = 120,
                                    min_value = 60,
                                    max_value = 1000,
                                    step = 5)
    
        height = st.number_input(label = "Enter your height (in inches)",
                                    value = 60,
                                    min_value = 36,
                                    max_value = 96,
                                    step = 1)




    smoke   = st.radio(label = 'Have you smoked at least 100 cigarettes in your entire life?', 
                        options = data['Smoking'])
    
    alcohol = st.radio(label = 'Do you drink alcohol?', 
                        options = data['AlcoholDrinking'])

    stroke  = st.radio(label = 'Have you ever had a stroke?', 
                        options = data['Stroke'])

    physical= st.slider(label = 'Rate your ',
                        min_value = 0,
                        max_value = 24,
                        value = 20,
                        step = 0)

    walk    = st.radio(label = 'Do you have difficulty walking or climbing the stairs?', 
                        options = data['DiffWalking'])

    sex     = st.radio(label = 'What is your biological sex?', 
                        options = data['Sex'])

    age     = st.selectbox(label = "What is your age?",
                        options = data['AgeCategory'])

    race    = st.selectbox(label = "What is your age?",
                        options = data['Race'])

    diabetic= st.selectbox(label = "Are you or have been close to being diabetic",
                        options = data['Diabetic'])

    active  = st.radio(label = 'Are you physically active', 
                        options = data['PhysicalActivity'])

    health  = st.selectbox(label = 'What would you say your general health is like?', 
                        options = data['GenHealth'])

    sleep   = st.number_input(label = 'On average, how many hours of sleep do you get on a daily basis?',
                        min_value = 0,
                        max_value = 24,
                        value = 20,
                        step = 0)

    asthma  = st.radio(label = 'Do you have/had asthma?', 
                        options = data['Asthma'])

    kidney  = st.radio(label = 'Do you have/had kidney cancer?', 
                        options = data['KidneyDisease'])

    skin    = st.radio(label = 'Do you have/had skin cancer?', 
                        options = data['SkinCancer'])

    

