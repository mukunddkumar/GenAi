import streamlit as st
from openai import OpenAI

# Set the API key
api_key = "Use-your-api-key-here"
client = OpenAI(api_key=api_key)

# Custom CSS for dark theme and snowflake animation
custom_css = """
<style>
    body {
        color: #fff;
        background-color: #1e1e1e;
    }
    .stTextInput>div>div>input {
        color: #fff;
        background-color: #2e2e2e;
    }
    .stButton>button {
        color: #fff !important;
        background-color: #0078ff !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 10px 20px !important;
        font-size: 18px !important;
        cursor: pointer !important;
        transition: background-color 0.3s ease !important;
    }
    .stButton>button:hover {
        background-color: #0056b3 !important;
    }
    /* Snowflake animation */
    @keyframes snowfall {
        0% { transform: translateY(-100%); }
        100% { transform: translateY(100vh); }
    }
    .snowflake {
        position: absolute;
        top: -20px;
        left: calc(50% - 10px);
        font-size: 24px;
        animation: snowfall 10s linear infinite;
        color: #fff;
    }
</style>
"""

# Set page title and subheader
st.title("🐛 AI Bug Detective 💬🔍")
st.markdown(custom_css, unsafe_allow_html=True)

# Add a text area for user input
prompt = st.text_area("Enter your Python code:")

# Add a button for submitting code for review
if st.button("🔍 Find Bugs 🐞"):
    # Call the OpenAI API to analyze the code
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-16k-0613",
        messages=[
            {"role": "system", "content": """You are a helpful AI Assistant and Code reviewer.
            Find the Bugs and error in the program."""},
            {"role": "user", "content": prompt}
        ]
    )
    # Display the feedback
    st.subheader("Feedback:")
    st.write(response.choices[0].message.content)

    # Show snowflake animation
    st.markdown('<i class="fas fa-snowflake snowflake"></i>', unsafe_allow_html=True)
