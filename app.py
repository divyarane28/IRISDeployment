import streamlit as st
import pickle
import numpy as np


#Load model
with open("model.pkl") as f:
    model=pickle.load(f)

# Streamlit UI
st.title("Iris flower classifier")
st.write("Enter the features below : ")

# Input features
s1=st.number_input("Sepal length : ",min_value=4.3,max_value=7.9)
sw=st.number_input("Sepal width : ",min_value=2,max_value=4.4)
p1=st.number_input("Petal length : ",min_value=1,max_value=6.9)
pw=st.number_input("Petal width : ",min_value=0.1,max_value=2.5)

# button predict
if st.button("Predict"):
    pred=model.predict([[s1,sw,p1,pw]])
    classes=["Setosa","Versicolor","Virginica"]
    st.write(f"Prediction : ",{classes[prediction[0]]})
