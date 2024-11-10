from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()  
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get response from Gemini model
def get_gemini_response(question):
    model = genai.GenerativeModel("gemini-pro") 
    chat = model.start_chat(history=[])
    response = chat.send_message(question, stream=True)
    return response

# Streamlit app setup
st.set_page_config(page_title="shashank chatbot")
st.header("Welcome to my chatbot")

# User input and response display
if "input_text" not in st.session_state:
    st.session_state.input_text = ""

input_text = st.text_input("Input:", st.session_state.input_text)

if st.button("Get Response") and input_text:
    response = get_gemini_response(input_text)
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
    

