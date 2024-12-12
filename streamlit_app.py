import streamlit as st

st.title("Uni Grant Matcher")
st.write(
    "In need of funding but don't know what grant to apply for? Use the Uni Grant Matcher to find your best fit!"
)

# Selectbox to select association
association = st.selectbox(
    "What is the applicant's association with Uni?",
    ("Faculty", "Student"),
    index = None,
    placeholder = "Select association...")

st.write("Displaying grant uses for:", association)

# Pill buttons for each association
if association == "Faculty":
    list_purposes_f = ["Special Opportunity (Non-Uni)", "Conference", "Research/Publication", 
                  "Activity", "Travel/Housing/Food", "Insurance", "Project Supplies", 
                  "Startup (New program)", "Professional Membership"]
    purposes_f = st.pills("Select all purposes for grant", list_purposes_f, selection_mode = "multi")
    
    
if association == "Student":
    list_purposes_s = ["Scholarship/Special Opportunity (Non-Uni)", "Conference", "Research", 
                  "Activity", "Travel/Housing/Food", "Supplies", "Study Abroad", "AP/ACT Prep",
                  "Startup (New program)", "Camps (academic, arts, athletics)"]
    purposes_s = st.pills("Select all purposes for grant", list_purposes_f, selection_mode = "multi")    
