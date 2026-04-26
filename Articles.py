import streamlit as st
import random

# ---------------- PAGE ----------------
st.set_page_config(page_title="Chemistry Cards", layout="centered")

# ---------------- BACKGROUND (VIDEO + FIXED UI) ----------------
st.markdown("""
<style>

/* Background video */
video.bg {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    object-fit: cover;
    z-index: -1;
}

/* Remove Streamlit white box */
.block-container {
    background: transparent !important;
}

/* Global background fallback */
.stApp {
    background-color: black;
}

/* TEXT */
h1, h2, h3, p {
    color: white !important;
}

/* BUTTONS (FORCED BLACK) */
.stButton > button {
    background-color: black !important;
    color: white !important;
    border: 2px solid white !important;
    padding: 10px;
    font-size: 16px;
}

.stButton > button:hover {
    background-color: #222 !important;
}

</style>

<video autoplay loop muted class="bg">
    <source src="background.mp4" type="video/mp4">
</video>
""", unsafe_allow_html=True)

# ---------------- STATE ----------------
if "state" not in st.session_state:
    st.session_state.state = "home"

if "article_state" not in st.session_state:
    st.session_state.article_state = "menu"

if "question_index" not in st.session_state:
    st.session_state.question_index = 0

if "score" not in st.session_state:
    st.session_state.score = 0

# ---------------- QUESTIONS (YOUR ORIGINAL SET KEPT) ----------------
QUESTIONS = [
    {"q": "What is the first element?", "A": "Helium", "B": "Nitrogen", "C": "Hydrogen", "D": "Water", "correct": "C"},
    {"q": "What is H2O?", "A": "Helium", "B": "Nitrogen", "C": "Hydrogen", "D": "Water", "correct": "D"},
    {"q": "Which gas is in a balloon?", "A": "Helium", "B": "Nitrogen", "C": "Hydrogen", "D": "Water", "correct": "A"},
    {"q": "What is CO2?", "A": "Hydrogen", "B": "Carbon Dioxide", "C": "Water", "D": "Carbon Monoxide", "correct": "B"},
    {"q": "What is the charge of an electron?", "A": "Positive", "B": "Negative", "C": "Neutral", "D": "None", "correct": "B"},
    {"q": "How many elements are there?", "A": "100", "B": "118", "C": "12", "D": "None", "correct": "B"},
    {"q": "What is bonding?", "A": "Atoms joining", "B": "Breaking", "C": "Heating", "D": "Freezing", "correct": "A"},
    {"q": "What is oxygen?", "A": "O", "B": "H", "C": "C", "D": "Na", "correct": "A"},
    {"q": "What is water made of?", "A": "CO2", "B": "H2O", "C": "O2", "D": "NaCl", "correct": "B"},
    {"q": "Which is a noble gas?", "A": "Oxygen", "B": "Helium", "C": "Hydrogen", "D": "Sodium", "correct": "B"},
]

def next_question():
    st.session_state.question_index = (st.session_state.question_index + 1) % len(QUESTIONS)

q = QUESTIONS[st.session_state.question_index]

# ---------------- ARTICLES (UNCHANGED CONTENT) ----------------
ARTICLES = {
"a1": """Atoms come together at certain times. They do this so that they can complete their shells.

Shells are the layers of an atom. They are what atoms want to always achieve. Any atom would love to complete their shells through other atoms. Think of atoms as people. They always want their goal. Money. To atoms, completing their shells is like winning the lottery.

Atoms can complete their shells in one way. Bonding. This happens when an atom goes to another one and they do one of 3 things.

Give, share, or take.

Giving electrons allow them to complete their shells if they are 1 or 2 more electrons than a shell. They give other atoms electrons.

Taking is when they get something from another atom. This happens a lot to atoms who are 1 or 2 electrons more than a full shell.

Finally, sharing electrons is when 2 atoms decide to both use an atom of the other. This is called covalence, while giving and taking is called ionic bonding. Polar covalent bonds are a mix of the two.

Electronegativity is how much atoms attract electrons. Fluorine is highest.""",

"a2": """Atoms make up everything. From your hair to water to air.

Atoms are extremely small and made of electrons, protons, and neutrons.

Protons are positive, electrons are negative, neutrons are neutral.

They form a nucleus in the center.

Atoms combine to form molecules like water (H2O).""",

"a3": """Matter is anything that takes up space.

It exists as solid, liquid, or gas.

Solids are tightly packed.

Liquids flow but stay in a container.

Gases move freely.

Temperature affects movement of particles.""",

"a4": """The pH scale measures acidity.

It goes from 0 to 14.

0 is acidic, 14 is basic, 7 is neutral.

Lemon is acidic, water is neutral, soap is basic.

Acids release hydrogen ions, bases absorb them."""
}

# ---------------- HOME ----------------
def home():
    st.image("logo.png", width=120)
    st.title("Chemistry Cards")

    if st.button("Elements"):
        st.session_state.state = "elements"

    if st.button("Articles"):
        st.session_state.state = "articles"

    if st.button("Quiz"):
        st.session_state.state = "quiz"

    if st.button("Minigame"):
        st.session_state.state = "minigame"

# ---------------- ARTICLES ----------------
def articles():
    st.title("Articles")

    if st.session_state.article_state == "menu":
        if st.button("Bonding"):
            st.session_state.article_state = "a1"
        if st.button("Atoms"):
            st.session_state.article_state = "a2"
        if st.button("States of Matter"):
            st.session_state.article_state = "a3"
        if st.button("pH Scale"):
            st.session_state.article_state = "a4"
    else:
        st.write(ARTICLES[st.session_state.article_state])
        if st.button("Back"):
            st.session_state.article_state = "menu"

    if st.button("Exit"):
        st.session_state.state = "home"

# ---------------- QUIZ ----------------
def quiz():
    st.title("Quiz")

    st.write(q["q"])

    for opt in ["A", "B", "C", "D"]:
        if st.button(q[opt]):
            if opt == q["correct"]:
                st.session_state.score += 1
            next_question()

    st.write(f"Score: {st.session_state.score}")

    if st.button("Exit"):
        st.session_state.state = "home"

# ---------------- ELEMENTS ----------------
def elements():
    st.title("Elements Table")
    st.write("Placeholder for periodic table")

    if st.button("Exit"):
        st.session_state.state = "home"

# ---------------- MINIGAME ----------------
def minigame():
    st.title("Minigame")
    st.write("Placeholder for animation game")

    if st.button("Exit"):
        st.session_state.state = "home"

# ---------------- ROUTER ----------------
if st.session_state.state == "home":
    home()
elif st.session_state.state == "articles":
    articles()
elif st.session_state.state == "quiz":
    quiz()
elif st.session_state.state == "elements":
    elements()
elif st.session_state.state == "minigame":
    minigame()