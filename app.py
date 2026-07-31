import streamlit as st
import pandas as pd
import pickle


with open("decision_tree_model.pkl", "rb") as file:
    model = pickle.load(file)

st.set_page_config(
    page_title="Student Placement Prediction",
    page_icon="🎓"
)
st.sidebar.title("📊 Model Information")

st.sidebar.markdown("---")

st.sidebar.write("**Algorithm:** Decision Tree Classifier")
st.sidebar.write("**Dataset:** Student Placement Dataset")
st.sidebar.write("**Accuracy:** 95.00%")

st.sidebar.markdown("---")

st.sidebar.info("Developed by Umme Ahmad")
st.markdown(
    "<h2 style='text-align:center; white-space: nowrap;'>🎓 Student Placement Prediction System</h2>",
    unsafe_allow_html=True
)
st.write("Enter the student's details below.")

study_hours = st.number_input("Study Hours", min_value=0.0, max_value=24.0, value=5.0)
internet_usage = st.number_input("Internet Usage (hours/day)", min_value=0.0, max_value=24.0, value=4.0)
assignments_completed = st.number_input("Assignments Completed", min_value=0, value=10)
previous_score = st.number_input("Previous Score", min_value=0.0, max_value=100.0, value=70.0)
exam_score = st.number_input("Exam Score", min_value=0.0, max_value=100.0, value=75.0)

if st.button("Predict Placement"):

    input_data = pd.DataFrame({
        "study_hours": [study_hours],
        "internet_usage": [internet_usage],
        "assignments_completed": [assignments_completed],
        "previous_score": [previous_score],
        "exam_score": [exam_score]
    })

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("🎉 Student is likely to be Placed.")
    else:
        st.error("❌ Student is not likely to be Placed.")
