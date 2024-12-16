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




purposes = []


# Faculty pill buttons
if association == "Faculty":
    
    # Dictionary containing all grants with their corresponding purposes
    grants = {"Classroom Supplies": "Uni High Faculty Classroom Needs & Projects Request",
              "Special Opportunity (Non-Uni)": ["Ang Current Use Fund (Professional Development Funding)", "Uni Endowment Fund (Professional Development Funding)"],
              "Conference": "Ang Current Use Fund (Professional Development Funding)",
              "Research/Publication": ["Frankel Fund For Learning Innovation", "Innovations in Learning (Professional Development Funding)", "Teaching Excellence (Makino Awards)"],
              "Activity": ["Innovations in Learning (Professional Development Funding)", "Teaching Excellence (Makino Awards)"],
              "Project Supplies": ["Innovations in Technology (Professional Development Funding)", "Uni Endowment Fund (Professional Development Funding)", "Teaching Excellence (Makino Awards)"],
              "Startup (New program)": ["Uni Endowment Fund (Professional Development Funding)", "Teaching Excellence (Makino Awards)"],
              "Professional Membership": "Uni Endowment Fund (Professional Development Funding)",
              "Travel/Housing/Food": "Teaching Excellence (Makino Awards)"}

    purposes = st.pills("Select all purposes for grant", grants.keys(), selection_mode = "multi")




                                                        
# Student pill buttons    
if association == "Student":  

    # Dictionary containing all grants with their corresponding purposes
    grants = {"Conference": "Barbara Lazarus Memorial Fund",
              "Research": ["Barbara Lazarus Memorial Fund", "Frankel Fund For Learning Innovation"],
              "Activity": ["Barbara Lazarus Memorial Fund", "Makino Awards"],
              "Travel/Housing/Food": ["Barbara Lazarus Memorial Fund", "Boren Scholarship", "Makino Awards"],
              "Supplies": ["Barbara Lazarus Memorial Fund", "Boren Scholarship", "Makino Awards"],
              "Scholarship/Special Opportunity": ["Boren Scholarship", "Eastern Illini Electric Cooperative", "The Illinois Odd Fellow-Rebekah Scholarship Program", "Martin Luther King Scholarship"],
              "Study Abroad": ["Boren Scholarship", "McNevin Scholarship"],
              "AP/ACT Prep": ["Boren Scholarship", "McNevin Scholarship"],
              "Camps (academic, arts, athletics)": ["Boren Scholarship", "McNevin Scholarship"]}

    purposes = st.pills("Select all purposes for grant", grants.keys(), selection_mode = "multi")  




def generate_results(purposes: list) -> list:
    """
    Generates results of suitable grant(s) based off of user's chosen purposes.

    Args:
            purposes(list):        List containing strings of chosen purpose options.
    
    Returns:
            matches(list):         List containing string titles of matched grants.
    """
    matches = []
    
    for purpose in purposes:
        # One grant
        if len(grants[purpose].values()) == 1:
            return grants[purpose]
        # Multiple grants
        for grant in grants[purpose]:
            matches += [grant]

        return matches



st.write(f"Check out:")

grant_links = {"Barbara Lazarus Memorial Fund": "https://www.uni.illinois.edu/sites/default/files/2024-09/Barbara%20Lazarus%20Memorial%20Fund.pdf",
                "Boren Scholarship": "https://www.uni.illinois.edu/sites/default/files/2022-11/Boren_Scholarship.docx",
                "Eastern Illini Electric Cooperative": "https://eiec.org/youth-washington-program",
                "Makino Awards": "https://www.uni.illinois.edu/sites/default/files/2022-11/MAKINO%20AWARD_Enhancing%20Student%20Life.doc",
                "The Illinois Odd Fellow-Rebekah Scholarship Program": "https://ioof-il.org/programs/scholarship-program.html",
                "Frankel Fund For Learning Innovation": "https://www.uni.illinois.edu/sites/default/files/2023-04/Frankel_Fund_for_Learning_Innovation_Application_Revised_4-4-23.docx",
                "McNevin Scholarship": "https://www.uni.illinois.edu/sites/default/files/2024-08/McNevin_Scholarship_Description_and_application_2024.pdf",
                "Martin Luther King Scholarship": "https://www.collegesuccessfoundation.org/scholarship/martin-luther-king-jr-scholarship/#about",
                "Uni High Faculty Classroom Needs & Projects Request": "https://surveys.illinois.edu/sec/1092747534?referrer=",
                "Ang Current Use Fund (Professional Development Funding)": "https://forms.illinois.edu/sec/4072389?referrer=https://shibboleth.illinois.edu/",
                "Innovations in Learning (Professional Development Funding)": "https://forms.illinois.edu/sec/4072389?referrer=https://shibboleth.illinois.edu/",
                "Uni Endowment Fund (Professional Development Funding)": "https://forms.illinois.edu/sec/4072389",
                "Teaching Excellence (Makino Awards)": "https://www.uni.illinois.edu/sites/default/files/2022-11/Makino_Award_Teaching_Excellence.doc"}



# Run generate_results only if there are purposes selected
if purposes != []:
    for grant in generate_results(purposes):
        st.link_button(f"Apply for {grant}", grant_links[grant])

st.write("For more information on grants and funds at Uni, visit the Uni High website.")         
         
        
# GENERATING KEY ERROR TYPE B FOR CONFERENCE AND RESEARCH
# CHECK CACHING & REBOOTING

    
    
