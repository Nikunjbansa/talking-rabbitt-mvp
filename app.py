import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Talking Rabbitt AI - Conversational Analytics")

uploaded_file = st.file_uploader("Upload Sales CSV")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df)

    question = st.text_input("Ask a question about your data")

    if question:
        if "highest revenue" in question.lower():

            result = df.groupby("Region")["Revenue"].sum()

            top_region = result.idxmax()

            st.write("Region with highest revenue:", top_region)

            st.bar_chart(result)
