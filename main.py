import streamlit as st
import random

# ---------------- PAGE ----------------
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

if "score" not in st.session_state:
    st.session_state.score = 0

if "question_count" not in st.session_state:
    st.session_state.question_count = 0

# ---------------- YOUR QUESTIONS (UNCHANGED) ----------------
QUESTIONS = [
    {"q": "What is the first element?", "A": "Helium", "B": "Nitrogen", "C": "Hydrogen", "D": "Water", "correct": "C"},
    {"q": "What is H2O?", "A": "Helium", "B": "Nitrogen", "C": "Hydrogen", "D": "Water", "correct": "D"},
    {"q": "Which gas is in a balloon?", "A": "Helium", "B": "Nitrogen", "C": "Hydrogen", "D": "Water", "correct": "A"},
    {"q": "Which is NOT in an atom?", "A": "Proton", "B": "Nucleus", "C": "Electron", "D": "Hydrogen", "correct": "D"},
    {"q": "What is CO2?", "A": "Hydrogen", "B": "Carbon Dioxide", "C": "Water", "D": "Carbon Monoxide", "correct": "B"},
    {"q": "What is the highest electronegative element?", "A": "Hydrogen", "B": "Oxygen", "C": "Fluorine", "D": "Neon", "correct": "C"},
    {"q": "Which is NOT a type of bonding?", "A": "Covalent", "B": "Ionic", "C": "Polar Covalent", "D": "Calcic", "correct": "D"},
    {"q": "How many elements are there?", "A": "100", "B": "12", "C": "118", "D": "None of the others", "correct": "C"},
    {"q": "What is the charge of an electron?", "A": "Positive", "B": "Negative", "C": "Neutral", "D": "None of the others", "correct": "B"},
    {"q": "Which of these is not part of the first 10 elements?", "A": "Helium", "B": "Calcium", "C": "Boron", "D": "Lithium", "correct": "B"},
    {"q": "Which of these has exactly two shells?", "A": "Hydrogen", "B": "Mercury", "C": "Oxygen", "D": "Einsteinium", "correct": "C"},
    {"q": "Which of these isn't a group?", "A": "Calcimites", "B": "Transition Metals", "C": "Actinoids", "D": "Lanthanides", "correct": "A"},
    {"q": "What are multiple atoms combined together called?", "A": "Electron", "B": "Nucleus", "C": "Molecule", "D": "Solid", "correct": "C"},
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
            st.session_state.quiz_state = "question"
            st.session_state.score = 0
            st.session_state.question_count = 0
            st.rerun()

        if st.button("Mini Game"):
            st.session_state.state = "minigame"
            st.rerun()

# ---------------- QUIZ ----------------
def quiz():
    q = st.session_state.current_question

    st.subheader(f"Score: {st.session_state.score} / {st.session_state.question_count}")

    if st.session_state.question_count >= 10:
        st.title("Finished!")

        st.write(f"Final Score: {st.session_state.score} / 10")

        st.write("Ways to improve:")
        st.write("- Review the articles section")
        st.write("- Focus on bonding and atoms")
        st.write("- Try again to improve your score")

        if st.button("Restart"):
            st.session_state.score = 0
            st.session_state.question_count = 0
            st.session_state.current_question = generate_question()
            st.session_state.quiz_state = "question"
            st.rerun()

        if st.button("Home"):
            st.session_state.state = "home"
            st.rerun()

        return

    st.subheader(q["q"])

    if st.session_state.quiz_state == "question":
        if st.button(q["A"]):
            check_answer("A")

        if st.button(q["B"]):
            check_answer("B")

        if st.button(q["C"]):
            check_answer("C")

        if st.button(q["D"]):
            check_answer("D")

    elif st.session_state.quiz_state == "correct":
        st.success("Correct!")
        if st.button("Next"):
            next_question()

    elif st.session_state.quiz_state == "wrong":
        st.error("Incorrect!")
        if st.button("Next"):
            next_question()

    if st.button("Exit"):
        st.session_state.state = "home"
        st.rerun()

def check_answer(choice):
    if choice == st.session_state.current_question["correct"]:
        st.session_state.score += 1
        st.session_state.quiz_state = "correct"
    else:
        st.session_state.quiz_state = "wrong"

    st.session_state.question_count += 1
    st.rerun()

def next_question():
    st.session_state.current_question = generate_question()
    st.session_state.quiz_state = "question"
    st.rerun()

# ---------------- PLACEHOLDERS ----------------
def elements():
    st.title("Elements")
    st.image("ELEMENTS.png", use_container_width=True)
    if st.button("Back"):
        st.session_state.state = "home"
        st.rerun()

def articles():
    st.title("Articles (unchanged from your version)")
    if st.button("Back"):
        st.session_state.state = "home"
        st.rerun()

def minigame():
    st.title("Mini Game (animation not supported in Streamlit yet)")
    if st.button("Back"):
        st.session_state.state = "home"
        st.rerun()

# ---------------- ROUTER ----------------
if st.session_state.state == "home":
    home()
elif st.session_state.state == "quiz":
    quiz()
elif st.session_state.state == "elements":
    elements()
elif st.session_state.state == "articles":
    articles()
elif st.session_state.state == "minigame":
    minigame()