import streamlit as st
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Chemistry Cards", layout="centered")

# ---------------- STATE ----------------
if "state" not in st.session_state:
    st.session_state.state = "home"

if "article_state" not in st.session_state:
    st.session_state.article_state = "menu"

if "quiz_state" not in st.session_state:
    st.session_state.quiz_state = "question"

if "current_question" not in st.session_state:
    st.session_state.current_question = None

# ---------------- STYLE ----------------
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(to bottom, #0f172a, #111827);
}

/* Text */
h1, h2, h3, p {
    color: white;
}

/* Buttons */
div.stButton > button {
    width: 100%;
    height: 55px;
    font-size: 16px;
    border-radius: 10px;
    background-color: black !important;
    color: white !important;
    border: 1px solid white;
}

/* IMPORTANT: push content above bottom bar */
.block-container {
    padding-bottom: 120px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- QUIZ ----------------
QUESTIONS = [
    {"question": "What is H2O?", "options": ["Oxygen", "Hydrogen", "Water", "Carbon"], "answer": 2},
    {"question": "Atomic number of Carbon?", "options": ["6", "12", "8", "4"], "answer": 0},
    {"question": "Most electronegative atom?", "options": ["Oxygen", "Fluorine", "Hydrogen", "Carbon"], "answer": 1}
]

def generate_question():
    return random.choice(QUESTIONS)

# ---------------- BOTTOM COVER (REAL STREAMLIT SAFE VERSION) ----------------
st.markdown("""
<div style="
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 90px;
    background-color: #111827;
    z-index: 999999;
">
</div>
""", unsafe_allow_html=True)

# ---------------- HOME ----------------
def home():
    st.title("Chemistry Cards")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Elements"):
            st.session_state.state = "elements"
            st.rerun()

        if st.button("Articles"):
            st.session_state.state = "articles"
            st.rerun()

    with col2:
        if st.button("Quiz"):
            st.session_state.state = "quiz"
            st.session_state.current_question = generate_question()
            st.session_state.quiz_state = "question"
            st.rerun()

        if st.button("Mini Game"):
            st.session_state.state = "minigame"
            st.session_state.current_question = generate_question()
            st.session_state.quiz_state = "question"
            st.rerun()

# ---------------- ROUTER ----------------
if st.session_state.state == "home":
    home()