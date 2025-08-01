import streamlit as st
import google.generativeai as genai
st.title("Own Chat APP-Gemini")
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
with st.form("Gemini"):
    text = st.text_area("Enter Your Prompt")
    submitted = st.form_submit_button("Submit")

def generate_response(input_text):
    model = genai.GenerativeModel("gemini-pro")
    response = model.invoke(input_text)
    return response.content

if "chat_history" not in st.session_state:
    st.session_state['chat_history'] = []



if submitted and text :
    response = generate_response(text)
    st.session_state['chat_history'].append({'user': text, 'assistant': response})
    st.write(response)

st.write('## Chat History')
for chat in reversed(st.session_state['chat_history']):
       st.write(f"**:adult: User**: {chat['user']}")
       st.write(f"**:brain: Assistant**: {chat['assistant']}")
       st.write("---")