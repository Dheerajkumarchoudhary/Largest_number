import streamlit as st
st.write("""
# My First App
Find the Largest Number
""")

st.header('User Input Parameters')

first_number = st.number_input("Enter First Number")
second_number = st.number_input("Enter Second Number")
third_number = st.number_input("Enter Third Number")

highest = max(first_number, second_number, third_number)

st.subheader("The greatest number among these are")
st.write(highest)
