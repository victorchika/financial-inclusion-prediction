# Save this as a separate Python file, e.g., app.py
import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title('Financial Inclusion Prediction')

# Input fields for user to enter feature values
country = st.selectbox('Country', [0, 1, 2, 3])
year = st.selectbox('Year', [2016, 2017, 2018])
location_type = st.selectbox('Location Type', [0, 1])
cellphone_access = st.selectbox('Cellphone Access', [0, 1])
household_size = st.number_input('Household Size', min_value=1, max_value=21, step=1)
age_of_respondent = st.number_input('Age of Respondent', min_value=16, max_value=100, step=1)
gender_of_respondent = st.selectbox('Gender of Respondent', [0, 1])
relationship_with_head = st.selectbox('Relationship with Head', [0, 1, 2, 3, 4, 5])
marital_status = st.selectbox('Marital Status', [0, 1, 2, 3, 4])
education_level = st.selectbox('Education Level', [0, 1, 2, 3, 4, 5])
job_type = st.selectbox('Job Type', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Prediction
if st.button('Predict'):
    features = np.array([[country, year, location_type, cellphone_access, household_size,
                          age_of_respondent, gender_of_respondent, relationship_with_head,
                          marital_status, education_level, job_type]])
    prediction = model.predict(features)
    st.write('Prediction:', 'Has a bank account' if prediction == 1 else 'Does not have a bank account')