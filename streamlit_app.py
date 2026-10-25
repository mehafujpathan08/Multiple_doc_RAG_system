import streamlit as st
from graph import graph
# import os
# st.write("DEBUG KEY:", os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="Multi-Agent AI")

st.title("🤖 Multi-Agent Task Automation System")

user_input = st.text_input("Enter your task:")

if st.button("🚀 Run Agents"):

    if user_input.strip() == "":
        st.warning("Enter a task")
    else:
        with st.spinner("Agents working... 🤖"):
            result = graph.invoke({"input": user_input})

        st.subheader("🧠 Planner Agent")
        st.write(result["plan"])

        st.subheader("🔧 Tool Agent")
        st.write(result["tool"])

        st.subheader("⚙️ Executor Agent")
        st.write(result["output"])