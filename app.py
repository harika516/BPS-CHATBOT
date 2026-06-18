import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-2.5-flash")

# App title
st.title("📚 BPS chatbot (Early access)")

# User input
question = st.text_input(
    "What would you like to learn?",
    placeholder="Your Question Here..."
)

# Explain button
if st.button("Enter"):
    if question.strip():
        prompt = f"""
        You are a friendly teacher.

        Explain this topic simply:
        {question}

        After explaining, generate 3 multiple-choice questions (MCQs).
        Provide the correct answers separately.
        """

        with st.spinner("Generating response..."):
            response = model.generate_content(prompt)

        st.write(response.text)

    else:
        st.warning("Please enter a topic to learn.")
