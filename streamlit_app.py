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
                  "Classroom Supplies", "Startup (New program)", "Professional Membership"]
    purposes_f = st.pills("Select all purposes for grant", list_purposes_f, selection_mode = "multi")

    faculty_grants = {"Uni High Faculty Classroom Needs & Projects Request": "Classroom Supplies"
                "Ang Current Use Fund (Professional Development Funding)": ["Special Opportunity (Non-Uni)", "Conference"]
                "Frankel Fund For Learning Innovation": "Research",
                "Innovations in Technology (Professional Development Funding)": ["Research", "Activity", "Project Supplies"],
                "Uni Endowment Fund (Professional Development Funding)": ["Special Opportunity (Non-Uni)", "Project Supplies", "Startup (New program)", "Professional Membership"],
                "Teaching Excellence (Makino Awards)": ["Research/Publication", "Activity", "Travel/Housing/Food", "Project Supplies", "Startup (New program)"]}


                                                        
    
if association == "Student":
    list_purposes_s = ["Scholarship/Special Opportunity (Non-Uni)", "Conference", "Research", 
                  "Activity", "Travel/Housing/Food", "Supplies", "Study Abroad", "AP/ACT Prep",
                  "Startup (New program)", "Camps (academic, arts, athletics)"]
    purposes_s = st.pills("Select all purposes for grant", list_purposes_s, selection_mode = "multi")    

    student_grants = {"Barbara Lazarus Memorial Fund": ["Conference", "Research", "Activity", "Travel/Housing/Food", "Supplies"],
                "Boren Scholarship": ["Scholarship/Special Opportunity", "Travel/Housing/Food", "Supplies", "Study Abroad", "AP/ACT Prep", "Camps (academic, arts, athletics)"],
                "Eastern Illini Electric Cooperative": "Scholarship/Special Opportunity",
                "Makino Awards": ["Activity", "Travel/Housing/Food", "Supplies"],
                "The Illinois Odd Fellow-Rebekah Scholarship Program": "Scholarship/Special Opportunity",
                "Frankel Fund For Learning Innovation": "Research",
                "McNevin Scholarship": ["Study Abroad", "AP/ACT Prep", "Camps(academic, arts, athletics)"],
                "Martin Luther King Scholarship": "Scholarship/Special Opportunity"}

# Generate results
