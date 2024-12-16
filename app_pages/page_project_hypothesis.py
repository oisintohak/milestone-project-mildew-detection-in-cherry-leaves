import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"* We suspect that leaves infected with powdery mildew have white/grey powdery patches that can differentiate them from a healthy leaf \n"
        f"* An Image Montage shows that infected leaves have these white/grey powdery patches. "
        f"Average Image, Variability Image and Difference between Averages studies did not reveal "
        f"any clear pattern to differentiate one from another."

    )
