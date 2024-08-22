import streamlit as st

st.set_page_config(
    page_title="Heart-disease",
    page_icon="🫀",
)

st.title("Heart disease prediction model 🫀")

st.sidebar.success("Select a demo above.")

st.markdown(
    """### Introduction
The human heart is a muscular organ responsible for pumping blood throughout the body, supplying oxygen and nutrients to tissues, and removing carbon dioxide and other wastes. It's a central component of the circulatory system and plays a crucial role in maintaining life.""")

st.image("heart.jpg", width=400)
"""### How the Heart Works
The heart functions as a dual pump, managing two main circulatory routes: pulmonary circulation and systemic circulation."""

("""**Pulmonary Circulation:**
The right side of the heart pumps deoxygenated blood to the lungs, where it receives oxygen and expels carbon dioxide.

**Systemic Circulation:** The left side of the heart pumps oxygen-rich blood to the rest of the body, supplying tissues and organs with the oxygen needed for energy production.
Each heartbeat is part of a cycle that includes:

**Diastole:** The heart muscle relaxes, allowing the chambers to fill with blood.Blood flows into the atria from the veins (right atrium from the body, left atrium from the lungs).  

**Systole:** The heart muscle contracts, pushing blood out of the chambers to the lungs and the rest of the body.""")  
("""### Types of Heart Disease""")
st.write(" ***Coronary Artery Disease (CAD):***") 
("""The most common type, characterized by the buildup of plaque in the coronary arteries, leading to reduced blood flow to the heart muscle.""")  
  
st.write(" ***Heart Attacks:***")  
("Occur when the plaque rupture causes a blockage, resulting in myocardial infarction (death of heart tissue).")  

st.write("**Heart Failure:**")  
("""When the heart is unable to pump enough blood to meet the body’s needs.""")    
st.write("**Arrhythmia:**")  
("""Abnormal heart rhythms or beats.""")    
st.write("**Congenital Heart Disease:**")  
("""Present at birth, affecting the structure of the heart or its blood vessels.  
""")

("""### Causes and Risk Factors""")
st.write("**Lifestyle:** High blood pressure, high cholesterol, smoking, physical inactivity, and obesity.")  
st.write("**Genetics:** Family history of early heart disease.")  
st.write("**Age:** Risk increases with age")  
st.write("**Sex:** Men have a greater risk of heart attack before age 50, while women have a higher risk after menopause.")
st.write("**Other medical conditions:** Diabetes, high blood pressure, and kidney disease.")
("""### Symptoms""")
st.write("**Chest pain or discomfort:** Typically described as pressure, tightness, or heaviness.")
st.write("**Shortness of breath:** Difficulty breathing or feeling winded.")
st.write("**Fatigue:** Feeling unusually tired or weak.")  
st.write("**Pain or discomfort in the arms, back, neck, jaw, or stomach:** Radiating pain from the chest.")  
("""### Diagnosis and Treatment""")
st.write("**Medical history and physical examination:** Identifying risk factors and symptoms.")
st.write("**Imaging tests:** Echocardiogram, stress test, or coronary angiogram to visualize the heart and blood vessels.")
st.write("**Lifestyle changes:** Quitting smoking, exercising regularly, and managing blood pressure and cholesterol.")
st.write("**Medications:** Statins, beta blockers, and blood thinners to manage symptoms and prevent complications.")
st.write("**Surgery:** Angioplasty, bypass grafting, or heart transplantation in severe cases.")
("""### Prevention""")
st.write("**Maintain a healthy lifestyle:** Eat a balanced diet, exercise regularly, and manage stress.")
st.write("**Get regular check-ups:** Monitor blood pressure, cholesterol, and blood sugar levels.")
st.write("**Quit smoking:** Reduce the risk of cardiovascular disease.")
