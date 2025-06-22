import streamlit as st
import pandas as pd
from utils import calculate_aps

st.set_page_config(page_title="SA APS Tracker", page_icon="🎓")
st.title("🎓 SA University Admission Tracker")
st.write("Calculate your APS score and see which degrees you qualify for.")

st.header("Step 1: Enter Your Subjects & Marks")

subjects = ['English HL', 'Mathematics', 'Physical Sciences', 'Life Orientation',
            'Life Sciences', 'Geography', 'Economics']

selected_subjects = {}
for subject in subjects:
    mark = st.number_input(f"{subject} (%)", min_value=0, max_value=100, step=1)
    if mark > 0:
        selected_subjects[subject] = mark

if selected_subjects:
    aps_score = calculate_aps(selected_subjects)
    st.success(f"✅ Your APS Score is: {aps_score}")

    st.header("Step 2: Explore Degrees You May Qualify For")
    df = pd.read_csv("data/programs.csv")

    qualified = df[df["Min_APS"] <= aps_score]
    if not qualified.empty:
        st.dataframe(qualified)
    else:
        st.warning("No qualifications matched your current APS. Try different marks.")
