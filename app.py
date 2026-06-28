import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import streamlit as st
from utils.llm_client import GeminiClient
from utils.mcp_helper import build_mcp_prompt


def main():
    st.set_page_config(
        page_title="MCP Generator / AI Tutor",
        page_icon="📝",
        layout="centered"
    )

    st.title("📝 AI MCP Generator & Tutor")
    st.write("Generate **15 MCP Question** based on a topic and difficulty level.")

    topic = st.text_input(
        "Enter Topic:",
        placeholder= "e.g. Python Lists, ML Algorithms, Docker, Git, MLOps etc."
    )

    level = st.selectbox(
        "Select Difficulty Level:",
        options=["Easy", "Medium", "Hard"],
        index=0
    )

    if st.button("Generate Questions"):
        if not topic.strip():
            st.warning("Please enter a topic")
            return
        
        with st.spinner("Generating MCQs..."):
            try:
                prompt = build_mcp_prompt(topic, level)
                client = GeminiClient()
                response = client.ask(prompt)

                st.markdown("---")
                st.subheader("📘 Generated MCQs")
                st.markdown(response)
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")


if __name__=="__main__":
    main()