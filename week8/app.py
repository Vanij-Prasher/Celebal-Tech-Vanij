import streamlit as st
from chatbot import get_answer
from PIL import Image

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Loan RAG Bot",
    page_icon="📊",
    layout="wide"
)

# --- INITIALIZE SESSION STATE ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://github.com/Vanij-Prasher.png", width=120)

    st.markdown("## 👤 About Developer")
    st.markdown("""
    **Vanij Prasher**  
    🧑‍💻 Data Science Intern at Celebal Technologies  
    ⚙️ Passionate about AI, ML, LLMs and Data Science.  
    🧰 Tech Stack: Python, Streamlit, LangChain, Mistral  
    🔗 [GitHub](https://github.com/Vanij-Prasher)  
    🔗 [LinkedIn](https://linkedin.com/in/vanij-prasher)
    """)

    st.markdown("## ℹ️ About App")
    st.write("This chatbot uses **RAG (Retrieval-Augmented Generation)** with a **Hugging Face LLM (Mistral 7B)** to answer intelligent questions from a **Loan CSV dataset**.")
    st.markdown("---")
    st.caption("🚀 Built with ❤️ by Vanij Prasher")

# --- MAIN CONTENT ---
st.markdown(
    """
    <div style='text-align: center; padding: 10px 0;'>
        <h1 style='margin-bottom: 5px;'>📊 Loan Approval RAG Chatbot</h1>
        <p style='font-size: 18px; color: gray;'>Ask smart questions from the CSV-based loan dataset. Powered by Mistral 🔥</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# --- Chat Input Section ---
with st.container():
    st.markdown("### 💬 Ask your question about the loan:")
    st.text_input("Type your question here", key="user_input", placeholder="You can ask your QUESTION here...")

    if st.button("📤 Submit Question"):
        question = st.session_state.user_input

        if question:
            with st.spinner("🔍 Researching with LLM..."):
                result = get_answer(question)

            st.session_state.latest_question = question
            st.session_state.latest_answer = result
            st.session_state.chat_history.append((question, result))

            st.rerun()
        else:
            st.warning("Please enter a question.")

    # --- Show Latest Answer ---
    if (
        "latest_answer" in st.session_state
        and st.session_state.latest_answer
        and isinstance(st.session_state.latest_answer, dict)
        and "result" in st.session_state.latest_answer
    ):
        st.markdown("## 🧠 Answer")
        st.markdown(f"**Q:** {st.session_state.latest_question}")
        st.success(st.session_state.latest_answer["result"])
        st.markdown("---")

    # --- Chat Suggestions ---
    if not st.session_state.chat_history:
        st.info(
            "💡 Try asking:\n"
            "- How many approved loans for graduates?\n"
            "- What is the common loan term?\n"
            "- What’s the approval rate in urban areas?"
        )
    else:
        st.markdown("## 📜 Chat History:")
        for i, (q, a) in enumerate(reversed(st.session_state.chat_history), 1):
            st.markdown(f"**Q{i}:** {q}")
            st.markdown(f"**A{i}:** {a['result'] if isinstance(a, dict) and 'result' in a else a}")
            st.markdown("---")

# --- Footer ---
st.markdown("---")
st.markdown(
    "<div style='text-align: center; font-size: 14px; color: gray;'>Built with 🧠 Mistral + LangChain + Streamlit | © 2025 Vanij Prasher</div>",
    unsafe_allow_html=True
)