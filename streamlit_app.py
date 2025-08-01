import streamlit as st
import google.generativeai as genai

st.title("Own Chat APP - Gemini")

# Configure API key from Streamlit secrets
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Initialize the Gemini model once
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_response(input_text):
    response = model.generate_content(input_text)
    return response.text  # This gives you the actual string output

# Set up session state for history
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Form for prompt input
with st.form("Gemini"):
    text = st.text_area("Enter Your Prompt")
    submitted = st.form_submit_button("Submit")

# On submit, generate and store response
if submitted and text:
    response = generate_response(text)
    st.session_state["chat_history"].append({"user": text, "assistant": response})
    st.write(response)

# Show chat history
st.write("## Chat History")
for chat in reversed(st.session_state["chat_history"]):
    st.write(f"**👤 User**: {chat['user']}")
    st.write(f"**🧠 Assistant**: {chat['assistant']}")
    st.write("---")
