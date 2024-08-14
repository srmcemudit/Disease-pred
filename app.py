import streamlit as st
import pickle

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)
    
age = st.number_input(
    "Enter your age", value=None , placeholder= "age" , key="age",
)

gender = st.selectbox(
    "gender",
    ("male", "female"),
    index=None , placeholder= "gender" , 
)
gender = 0 if gender == "male" else 1


blood = st.number_input(
    "Blood pressure at rest in mm hg", value=None , placeholder="Enter blood pressure" ,key="blood",
)

chol = st.number_input(
    "Serum cholesterol in mg/dl", value=None , placeholder="Enter cholestrol" ,key="chol",
)

ofbs = ["Above 120 mg/dl", "Below 120 mg/dl"]
fbs = st.selectbox(
    "Fasting blood sugar level",
    ofbs,
    index=None,
)
pfbs = 1 if fbs == 'Above 120 mg/dl' else 0

Thalach = st.number_input(
   "Enter Thalach value" , value=None , key="Thalach" , placeholder="Maximum heart rate achieved during a stress test" ,
)
exang = st.selectbox(
    "Exercise-induced angina",
    ("Yes", "No"),
    index=None , placeholder="chest pain during exercise" , key="exang" ,
)
exang = 1 if exang == 'Yes' else 0


oldpeak = st.number_input(
   "Enter oldpeak value" , value=None , key="oldpeak" , placeholder="Enter old peak value in mm" ,
)
slope = st.selectbox(
    "Slope of the peak exercise ST segment:",
    ("Upslopping", "Flat", "Downsloping"),
    index=None , placeholder="Enter slope value" , key="slope" ,
)
if slope == "Upslopping":
    slope = 0
elif slope == "Flat":
    slope = 1
else:
    slope = 2

ca = st.selectbox(
    "Number of major vessels (0-4) colored by fluoroscopy:",
    ("0", "1", "2" , "3" , "4" ),
    index=None , placeholder="Enter slope value" , key="ca" ,
)
cp1 = st.selectbox(
    "Chest pain:",
    ("Typical angina", "Atypical angina", "Non-anginal pain" , "Asymptomatic" ),
    index=None , placeholder="Chest Pain Type :" , key="cp" ,
)
def angina_classification(cp):
    if cp == "Typical angina":
        return "0", "0", "0"
    elif cp == "Atypical angina":
        return "1", "0", "0"
    elif cp == "Non-anginal pain":
        return "0", "1", "0"
    elif cp == "Asymptomatic":
        return "0", "0", "1"
    else:
        return "Invalid input"
chest = angina_classification(cp1)

ecg1 = st.selectbox(
    "Resting electrocardiographic results :",
    ("Normal", "Having ST-T wave abnormality", "Showing probable or definite left ventricular hypertrophy"),
    index=None , placeholder="Select ecg results" , key="ecg" ,
)
def elec(ecg):
    if ecg == "Normal":
        return "0", "0"
    elif ecg == "Having ST-T wave abnormality":
        return "1", "0"
    elif ecg == "Showing probable or definite left ventricular hypertrophy":
        return "0", "1"
    else:
        return "Invalid input"
electro = elec(ecg1)

thal_stress = st.selectbox(
    "Thalium stress test result:",
    ("Normal", "Fixed defect", "Reversible defect" , "Not described" ),
    index=None , placeholder="Chest Pain Type :" , key="thal" ,
)

def thala(thal):
    if thal == "Normal":
        return "0", "0", "0"
    elif thal == "Fixed defect":
        return "1", "0", "0"
    elif thal == "Reversible defect":
        return "0", "1", "0"
    elif thal == "Not described":
        return "0", "0", "1"
    else:
        return "Invalid input"
thalium = thala(thal_stress)
    
l = model.predict([[age,gender,blood,chol,pfbs,Thalach,exang,oldpeak,slope,ca,chest[0],chest[1],chest[2],electro[0],electro[1],thalium[0],thalium[1],thalium[2]]])
if l == 1:
    st.write("you are affected")
else:
    st.write("you are not affected")