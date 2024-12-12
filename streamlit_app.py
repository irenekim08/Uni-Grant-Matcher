import streamlit as st

your_working_directory/
├── pages/
│   ├── faculty.py
│   └── student.py
└── your_homepage.py
    

st.title("Uni Grant Matcher")
st.write(
    "In need of funding but don't know what grant to apply for? Use the Uni Grant Matcher to find your best fit!"
)

f, s = st.columns(2)
association_f.link_button("Faculty", 
