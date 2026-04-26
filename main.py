import streamlit as st
import random

st.set_page_config(page_title="Chemistry Cards", layout="centered")

# ---------------- VIDEO BACKGROUND FIX ----------------
st.markdown("""
<style>

/* Full black fallback */
.stApp {
    background-color: black;
}

/* Video background (fixed layering) */
video.bg {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    object-fit: cover;
    z-index: -1;
}

/* Remove white container */
.block-container {
    background: transparent !important;
}

/* TEXT */
h1, h2, h3, p {
    color: white !important;
}

/* 🔥 FORCE BUTTONS TO NOT BE WHITE */
.stButton > button {
    background-color: black !important;
    color: white !important;
    border: 2px solid white !important;
    padding: 10px;
    font-size: 16px;
}

/* hover */
.stButton > button:hover {
    background-color: #222 !important;
}

/* hide Streamlit chrome padding background */
main {
    background: transparent !important;
}

""")

# ---------------- STATE ----------------
if "state" not in st.session_state:
    st.session_state.state = "home"

if "article_state" not in st.session_state:
    st.session_state.article_state = "menu"

if "current_question" not in st.session_state:
    st.session_state.current_question = None

if "score" not in st.session_state:
    st.session_state.score = 0

if "question_count" not in st.session_state:
    st.session_state.question_count = 0

# ---------------- QUESTIONS ----------------
QUESTIONS = [
    {"q": "What is the first element?", "A": "Helium", "B": "Nitrogen", "C": "Hydrogen", "D": "Water", "correct": "C"},
    {"q": "What is H2O?", "A": "Helium", "B": "Nitrogen", "C": "Hydrogen", "D": "Water", "correct": "D"},
    {"q": "Which gas is in a balloon?", "A": "Helium", "B": "Nitrogen", "C": "Hydrogen", "D": "Water", "correct": "A"},
    {"q": "What is CO2?", "A": "Hydrogen", "B": "Carbon Dioxide", "C": "Water", "D": "Carbon Monoxide", "correct": "B"},
]

def generate_question():
    return random.choice(QUESTIONS)

# ---------------- HOME ----------------
def home():
    st.image("logo.png", width=120)
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
            st.rerun()

# ---------------- ARTICLES ----------------
def articles():
    st.title("Articles")

    if st.button("Back"):
        st.session_state.state = "home"
        st.session_state.article_state = "menu"
        st.rerun()

# ---------------- QUIZ ----------------
def quiz():
    if st.button("Exit"):
        st.session_state.state = "home"
        st.rerun()

    q = st.session_state.current_question

    st.title("Quiz")
    st.write(q["q"])

    for option in ["A", "B", "C", "D"]:
        if st.button(q[option]):
            st.session_state.current_question = generate_question()
            st.rerun()

# ---------------- ROUTER ----------------
if st.session_state.state == "home":
    home()
elif st.session_state.state == "articles":
    articles()
elif st.session_state.state == "quiz":
    quiz()