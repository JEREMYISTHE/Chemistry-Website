import streamlit as st
import random

# ---------------- PAGE ----------------
st.set_page_config(page_title="Chemistry Cards", layout="centered")

# ---------------- VIDEO BACKGROUND ----------------
st.markdown("""
<style>

/* App base */
.stApp {
    background-color: black;
}

/* Video background */
video.bg {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    z-index: -1;
}

/* Ensure UI stays above video */
.block-container {
    background: transparent !important;
}

/* Titles */
h1, h2, h3, h4, h5, h6 {
    color: white !important;
}

/* Text */
p {
    color: white;
}

/* Buttons */
.stButton > button {
    background-color: white;
    color: black;
    border: 2px solid black;
    padding: 10px;
    font-size: 16px;
}

.stButton > button:hover {
    background-color: #f0f0f0;
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

# ---------------- ARTICLES ----------------
ARTICLES = {
"a1": """Atoms come together at certain times. They do this so that they can complete their shells.

Shells are the layers of an atom. They are what atoms want to always achieve. Any atom would love to complete their shells through other atoms. Think of atoms as people. They always want their goal. Money. To atoms, completing their shells is like winning the lottery.

Atoms can complete their shells in one way. Bonding. This happens when an atom goes to another one and they do one of 3 things.

Give, share, or take.

Giving electrons allow them to complete their shells if they are 1 or 2 more electrons than a shell. They give other atoms electrons.

Taking is when they get something from another atom. This happens a lot to atoms who are 1 or 2 electrons more than a full shell.

Finally, sharing electrons is when 2 atoms decide to both use an atom of the other. This is called covalence, while giving and taking is called ionic bonding. Polar covalent bonds are a mix of the two.

How much another atom wants to interact with other atoms is called electronegativity. The highest electronegative atom is Fluorine with an electronegativity of about 4.""",

"a2": """Atoms make up everything. Yes. Everything. From your hair, to your water, to your waste, atoms make them up.

You might be wondering, why don't I see atoms? It is because atoms are so small, you can only see them with a microscope. In fact, the width of a single strand of hair is about a million times the size of a carbon atom.

Atoms are made of even smaller things called electrons, protons, and neutrons. An electron gives a negative charge, a proton releases a positive charge, and the neutrons provide a neutral charge. The neutrons and protons meet in the middle, making the nucleus. The protons in the nucleus make sure the electrons stay in the atom.

How do atoms make up everything? Well, they form and work together to make different things. For example, hydrogen and oxygen combine to create water. Any 2 atoms combined are called molecules. You can see the article, Bonding to see how atoms create different chemicals and substances that make up our world.""",

"a3": """Everything is matter. Water, ice, and oxygen is all matter. Matter is anything that takes up space. Matter comes in 3 ways.

Liquid, solid, and gas.

Liquids are anything that may still move, but will fill up a container. Think about a glass cup. The water will go in it, but not leave.

Solids are solid. They may be touched and felt if still. They would be the glass in a glass cup filled with water.

Finally, gases are not able to be felt. They try to be as free as they can and always try to move.

Each state of matter is made up in a different way. In a solid, molecules are very compact and together.

In a liquid, they are free, but don't move to much, and in a gas, they move around randomly and quickly.

When atoms get cold, they move slower and condense into liquids and solids. When they get hotter, they move faster, which provides the opposite affect, making liquids and gases.""",

"a4": """The PH scale is an important scale used to measure how acidic something is. It is involved with acids and bases and everything has a PH level. Water, Soda, Lemons, they all can be measured in PH.

PH is measured from 0 - 14, with 0 being acidic and 14 being a base. 7 is the neutral. Water is a 7 on the PH scale, lemon is a 2 and soap is a 12, meaning it is a base.

The differences between acids and bases is that acids taste sour while bases taste bitter. Also, chemically, acids release hydrogen ions while bases usually pick up the ions released.

Common examples of acids include lemons, vinegar, and battery acid. Common examples of bases are soap, bleach and baking soda."""
}

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
            st.session_state.score = 0
            st.session_state.question_count = 0
            st.rerun()
        if st.button("Mini Game"):
            st.session_state.state = "minigame"
            st.rerun()

# ---------------- ARTICLES ----------------
def articles():
    st.title("Articles")

    if st.session_state.article_state == "menu":
        if st.button("Bonding"):
            st.session_state.article_state = "a1"
            st.rerun()
        if st.button("Atoms"):
            st.session_state.article_state = "a2"
            st.rerun()
        if st.button("States of Matter"):
            st.session_state.article_state = "a3"
            st.rerun()
        if st.button("PH Scale"):
            st.session_state.article_state = "a4"
            st.rerun()
    else:
        st.markdown(ARTICLES[st.session_state.article_state])
        if st.button("Back"):
            st.session_state.article_state = "menu"
            st.rerun()

    if st.button("Exit"):
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
    st.write(f"Score: {st.session_state.score} / {st.session_state.question_count}")
    st.subheader(q["q"])

    for option in ["A", "B", "C", "D"]:
        if st.button(q[option]):
            if option == q["correct"]:
                st.session_state.score += 1
            st.session_state.question_count += 1
            st.session_state.current_question = generate_question()
            st.rerun()

# ---------------- ROUTER ----------------
if st.session_state.state == "home":
    home()
elif st.session_state.state == "articles":
    articles()
elif st.session_state.state == "quiz":
    quiz()