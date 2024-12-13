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



# Generate results while purposes != empty
while purposes != []:
    generate_results(purposes)



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
        for grant in grants[purpose]:
            matches += [grant]
        
        if len(purposes) == 1:
            return matches

        return matches
        

         
         
        


    
    
