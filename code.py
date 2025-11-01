import os
import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model=genai.GenerativeModel('gemini-2.0-flash')

# UI
st.title("💡 Code Generation & Explanation with Gemini 2.0")
user_input = st.text_area("📝 Enter your programming task or code snippet:")

if st.button("🚀 Generate Code / Explain"):
    prompt = f"""
    You are a helpful programming assistant who can generate code snippets and explain code.
    If the input is a task, generate code with brief comments.
    If the input is a code snippet, explain it in simple terms.
    
    Input: {user_input}
    """
    response = model.generate_content(prompt)
    st.success(response.text)
   
