from time import sleep
from turtle import setx
import streamlit as st
import json

def reverseList(item):
    return list(reversed(item))

with open('columns.json') as json_file:
    data = json.load(json_file)

header = st.container()

with header:
    st.title("HELLLO")

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
                        options = reverseList(data['Smoking']))

    alcohol = st.radio(label = 'Do you drink alcohol?', 
                        options = reverseList(data['AlcoholDrinking']))

    stroke  = st.radio(label = 'Have you ever had a stroke?', 
                        options = reverseList(data['Stroke']))

    walk    = st.radio(label = 'Do you have difficulty walking or climbing the stairs?', 
                        options = reverseList(data['DiffWalking']))

    sex     = st.radio(label = 'What is your biological sex?', 
                        options = reverseList(data['Sex']))

    age     = st.selectbox(label = "What is your age?",
                        options = data['AgeCategory'])

    race    = st.selectbox(label = "What is your age?",
                        options = data['Race'])

    diabetic= st.selectbox(label = "Are you or have been close to being diabetic",
                        options = data['Diabetic'])

    active  = st.radio(label = 'Are you physically active', 
                        options = reverseList(data['PhysicalActivity']))

    health  = st.selectbox(label = 'What would you say your general health is like?', 
                        options = reverseList(data['GenHealth']))

    sleep   = st.slider(label = 'On average, how many hours of sleep do you get on a daily basis?',
                        min_value = 0.0,
                        max_value = 24.0,
                        value = 20.0,
                        step = 0.5)

    asthma  = st.radio(label = 'Do you have/had asthma?', 
                        options = reverseList(data['Asthma']))

    kidney  = st.radio(label = 'Do you have/had kidney cancer?', 
                        options = reverseList(data['KidneyDisease']))

    skin    = st.radio(label = 'Do you have/had skin cancer?', 
                        options = reverseList(data['SkinCancer']))

    sel_col, disp_col = st.columns(2)

