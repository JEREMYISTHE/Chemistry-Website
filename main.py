import streamlit as st
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Chemistry Cards", layout="centered")

# ---------------- STATE INIT ----------------
if "state" not in st.session_state:
    st.session_state.state = "home"

if "quiz_state" not in st.session_state:
    st.session_state.quiz_state = "question"

if "current_question" not in st.session_state:
    st.session_state.current_question = None

# ---------------- STYLE ----------------
st.markdown("""
<style>
footer {visibility: hidden;}

.stApp {
    background: linear-gradient(to bottom, #0f172a, #111827);
}

h1, h2, h3, p {
    color: white;
}

div.stButton > button {
    width: 100%;
    height: 55px;
    font-size: 16px;
    border-radius: 10px;
    background-color: #a78bfa !important;
    color: black !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------- YOUR QUIZ QUESTIONS ----------------
QUESTIONS = [
    {
        "question": "What is H2O?",
        "options": ["Oxygen", "Hydrogen", "Water", "Carbon"],
        "answer": 2
    },
    {
        "question": "What is the atomic number of Carbon?",
        "options": ["6", "12", "8", "4"],
        "answer": 0
    },
    {
        "question": "Which atom is most electronegative?",
        "options": ["Oxygen", "Fluorine", "Hydrogen", "Carbon"],
        "answer": 1
    },

    # 👉 ADD YOUR ORIGINAL QUESTIONS HERE
]

def generate_question():
    return random.choice(QUESTIONS)

# ---------------- ARTICLES ----------------
ARTICLES = {
    "Bonding": """Atoms come together at certain times. They do this so that they can complete their shells.

Shells are the layers of an atom. They are what atoms want to always achieve. Any atom would love to complete their shells through other atoms. Think of atoms as people. They always want their goal. Money. To atoms, completing their shells is like winning the lottery.

Atoms can complete their shells in one way. Bonding. This happens when an atom goes to another one and they do one of 3 things.

Give, share, or take.

Giving electrons allow them to complete their shells if they are 1 or 2 more electrons than a shell. They give other atoms electrons.

Taking is when they get something from another atom. This happens a lot to atoms who are 1 or 2 electrons more than a full shell.

Finally, sharing electrons is when 2 atoms decide to both use an atom of the other. This is called covalence, while giving and taking is called ionic bonding. Polar covalent bonds are a mix of the two.

How much another atom wants to interact with other atoms is called electronegativity. The highest electronegative atom is Fluorine with an electronegativity of about 4.
"""
}

# ---------------- HOME ----------------
def home():
    col_logo, col_title = st.columns([1, 5])

    with col_logo:
        st.image("logo.png", width=80)

    with col_title:
        st.markdown("<h1>Chemistry Cards</h1>", unsafe_allow_html=True)

    st.markdown("---")

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

# ---------------- ELEMENTS ----------------
def elements():
    st.title("Elements")
    st.image("ELEMENTS.png", use_container_width=True)

    if st.button("Back"):
        st.session_state.state = "home"
        st.rerun()

# ---------------- QUIZ ----------------
def quiz():
    q = st.session_state.current_question

    if not q:
        st.session_state.current_question = generate_question()
        q = st.session_state.current_question

    st.subheader(q["question"])

    if st.session_state.quiz_state == "question":
        for i, option in enumerate(q["options"]):
            if st.button(option, key=f"opt_{i}"):
                if i == q["answer"]:
                    st.session_state.quiz_state = "correct"
                else:
                    st.session_state.quiz_state = "wrong"
                st.rerun()

    elif st.session_state.quiz_state == "correct":
        st.success("Correct")
        if st.button("Next"):
            st.session_state.current_question = generate_question()
            st.session_state.quiz_state = "question"
            st.rerun()

    elif st.session_state.quiz_state == "wrong":
        st.error("Wrong")
        if st.button("Try Again"):
            st.session_state.current_question = generate_question()
            st.session_state.quiz_state = "question"
            st.rerun()

    if st.button("Exit"):
        st.session_state.state = "home"
        st.rerun()

# ---------------- ARTICLES ----------------
def articles():
    st.title("Articles")
    st.markdown(ARTICLES["Bonding"])

    if st.button("Back"):
        st.session_state.state = "home"
        st.rerun()

# ---------------- MINI GAME ----------------
def minigame():
    st.title("Mini Game")
    st.write("Coming soon")

    if st.button("Back"):
        st.session_state.state = "home"
        st.rerun()

# ---------------- ROUTER ----------------
if st.session_state.state == "home":
    home()
elif st.session_state.state == "elements":
    elements()
elif st.session_state.state == "quiz":
    quiz()
elif st.session_state.state == "articles":
    articles()
elif st.session_state.state == "minigame":
    minigame()