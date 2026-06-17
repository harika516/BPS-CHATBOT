import streamlit as st
import google.generativeai as genai

# Replace with your NEW API key
genai.configure(api_key="AQ.Ab8RN6KAFX95zzqrfqEsqnIChSp7vJ0u7Jr_3_gIRl1XJl8loA")

# Initialize Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

# App title
st.title("📚 AI Learning Buddy")

# User input
question = st.text_input(
    "What would you like to learn?",
    placeholder="Your Question Here..."
)

# Explain button
if st.button("Explain"):
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