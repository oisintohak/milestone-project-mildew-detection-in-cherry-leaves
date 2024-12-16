import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n"
        f"* Powdery mildew is a fungal disease that affects many plant species. \n"
        f"* The client's company is concerned about supplying the market with a compromised quality product that contains the disease. \n\n"
        f"**Project Dataset**\n"
        f"* The available dataset contains more than 4000 images of cherry leaves from the client's crop fields")

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/oisintohak/milestone-project-mildew-detection-in-cherry-leaves/blob/main/README.md).")
    

    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew. \n"
        f"* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew. "
        )
