import streamlit as st
from big_mind_mapping import bmm
from reverse_brainstorm import rb
from role_storming import rs
from scamper import sc
from six_hats import sh
from starburtsting import sb
# Make the layout wide for better display
st.set_page_config(layout="wide")

# Define the brainstorming modes, their corresponding functions, and descriptions
modes = {
    "Big Mind Mapping": {
        "function": bmm,
        "description": "This involves creating a tree of ideas to explore the maximum amount of ideas in a very wide area. "
                       "This is perfect when you are lost and want to gather the maximum number of ideas."
    },
    "Reverse Brainstorming": {
        "function": rb,
        "description": "Instead of focusing on solutions, this technique involves identifying ways to cause a problem or "
                       "achieve the opposite effect. Perfect for spotting potential issues and coming up with innovative solutions."
    },
    "Role Storming": {
        "function": rs,
        "description": "Involves adopting the perspective of someone else to generate ideas. Great for gathering insights from different viewpoints."
    },
    "SCAMPER": {
        "function": sc,
        "description": "SCAMPER stands for Substitute, Combine, Adapt, Modify, Put to another use, Eliminate, and Reverse. "
                       "This method encourages thinking from multiple perspectives to generate diverse ideas."
    },
    "Six Thinking Hats": {
        "function": sh,
        "description": "This method, developed by Edward de Bono, looks at a problem from six different perspectives: "
                       "White (Data), Red (Emotions), Black (Risks), Yellow (Benefits), Green (Creativity), and Blue (Process management)."
    },
    "Starbursting": {
        "function": sb,
        "description": "Focuses on generating questions rather than answers using the 5 W's and 1 H (Who, What, Where, When, Why, How). "
                       "Ideal for comprehensive topic exploration."
    }
}

# App title and description
st.title("🧠 Brainstorming App")
st.write("Welcome! Choose a brainstorming mode to start generating ideas for your project.")


# Mode selection
mode_choice = st.selectbox("Select a brainstorming mode:", list(modes.keys()))

# Display the description of the selected mode
if mode_choice:
    st.write(f"**Mode selected:** {mode_choice}")
    st.write(modes[mode_choice]["description"])  # Display mode description

    # User input for idea description
    user_query = st.text_area("Describe your idea in detail to get started:",
                              "I am having a medical Instagram page talking about chronic diseases and how to deal with them. I need ideas for posts that can help me grow my page and reach more people.")

    # Button to start the brainstorming process
    if st.button("Generate Ideas"):
        # Display a loading message
        with st.spinner("Generating ideas, please wait..."):
            # Call the function for the selected mode
            result = modes[mode_choice]["function"](user_query)
        
        # Display the result in markdown format
        st.markdown(result)
