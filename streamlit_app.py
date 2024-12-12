import streamlit as st

pages/
    faculty.py
    student.py
    

st.title("Uni Grant Matcher")
st.write(
    "In need of funding but don't know what grant to apply for? Use the Uni Grant Matcher to find your best fit!"
)

f, s = st.columns(2)
association_f.link_button("Faculty", 
