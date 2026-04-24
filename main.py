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

# ---------------- QUIZ (UNCHANGED STRUCTURE) ----------------
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
    }
]

def generate_question():
    return random.choice(QUESTIONS)

# ---------------- ARTICLES (YOUR ORIGINAL CONTENT) ----------------
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

PH is measured from 0 - 14, with 0 being acidic and 14 being a base. 7 is the neutral. Water is a 7 on the PH scale, lemon is a 2 and soap is a 12, meaning it is a base

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
            st.session_state.quiz_state = "question"
            st.rerun()

        if st.button("Mini Game"):
            st.session_state.state = "minigame"
            st.rerun()

# ---------------- ELEMENTS ----------------
def elements():
    st.title("Elements")

    st.image("ELEMENTS.png", use_container_width=True)

    if st.button("Back"):
        st.session_state.state = "home"
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
    q = st.session_state.current_question

    st.subheader(q["question"])

    if st.session_state.quiz_state == "question":
        for i, option in enumerate(q["options"]):
            if st.button(option):
                if i == q["answer"]:
                    st.session_state.quiz_state = "correct"
                else:
                    st.session_state.quiz_state = "wrong"
                st.rerun()

    elif st.session_state.quiz_state == "correct":
        st.success("Correct!")
        if st.button("Next"):
            st.session_state.current_question = generate_question()
            st.session_state.quiz_state = "question"
            st.rerun()

    elif st.session_state.quiz_state == "wrong":
        st.error("Wrong!")
        if st.button("Try Again"):
            st.session_state.current_question = generate_question()
            st.session_state.quiz_state = "question"
            st.rerun()

    if st.button("Exit"):
        st.session_state.state = "home"
        st.rerun()

# ---------------- MINI GAME ----------------
def minigame():
    st.title("Mini Game")

    if st.button("Back"):
        st.session_state.state = "home"
        st.rerun()

# ---------------- ROUTER ----------------
if st.session_state.state == "home":
    home()
elif st.session_state.state == "elements":
    elements()
elif st.session_state.state == "articles":
    articles()
elif st.session_state.state == "quiz":
    quiz()
elif st.session_state.state == "minigame":
    minigame()