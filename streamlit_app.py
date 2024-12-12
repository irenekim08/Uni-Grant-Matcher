import streamlit as st

st.title("Uni Grant Matcher")
st.write(
    "In need of funding but don't know what grant to apply for? Use the Uni Grant Matcher to find your best fit!"
)

association = st.selectbox(
    "What is the applicant's association with Uni?",
    ("Faculty", "Student"),
    index = None,
    placeholder = "Select association..."
)

st.write("Displaying grants uses for:", association)
