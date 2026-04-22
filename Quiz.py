import pygame
import random
from Settings import *
import time

# ---------------- BUTTONS ----------------
A_button = pygame.Rect(100, 200, 250, 70)
B_button = pygame.Rect(380, 200, 250, 70)
C_button = pygame.Rect(100, 350, 250, 70)
D_button = pygame.Rect(380, 350, 250, 70)

X_button = pygame.Rect(15, 10, 30, 28)
Next_button = pygame.Rect(550, 250, 100, 40)

minigame_space = pygame.Rect(100, 350, 250, 70)
X = 100
Y = 400
frames = 0

# ---------------- ASSETS ----------------
basketball = pygame.image.load("basketball.png")
hoop = pygame.image.load("hoop.png")

BLACK = (0, 0, 0)

# ---------------- STATE ----------------
win_streak = 0
state = "question"

# ---------------- QUESTIONS ----------------
def generate_question():
    questions = [
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
    return random.choice(questions)

current = generate_question()

# ---------------- DRAW ----------------
def draw():
    # X button always visible
    pygame.draw.rect(screen, WHITE, X_button)
    screen.blit(X_Button, (20, 15))

    if state == "question":
        pygame.draw.rect(screen, RED, A_button)
        pygame.draw.rect(screen, BLUE, B_button)
        pygame.draw.rect(screen, YELLOW, C_button)
        pygame.draw.rect(screen, GREEN, D_button)

        screen.blit(question_font.render(str(win_streak), True, BLACK), (575, 10))
        screen.blit(flame, (625, 10))

        screen.blit(question_font.render(current["q"], True, BLACK), (100, 100))

        screen.blit(font.render(current["A"], True, BLACK), (130, 230))
        screen.blit(font.render(current["B"], True, BLACK), (405, 230))
        screen.blit(font.render(current["C"], True, BLACK), (130, 380))
        screen.blit(font.render(current["D"], True, BLACK), (405, 380))

    elif state == "correct":
        screen.blit(question_font.render("Correct! You may move on!", True, GREEN), (150, 150))
        pygame.draw.rect(screen, GREEN, Next_button)
        screen.blit(font.render("Next", True, WHITE), (565, 265))

    elif state == "wrong":
        screen.blit(question_font.render("Incorrect! Try the next one!", True, RED), (150, 150))
        pygame.draw.rect(screen, RED, Next_button)
        screen.blit(font.render("Next", True, WHITE), (565, 265))

    elif state == "randomizing":
        randomizer = random.randint(1, 2)
        if randomizer == 1:
            right_basketball()
        else:
            print("Wrong")

    elif state == "minigame_right_1":
        global frames
        global X
        global Y
        if frames == 20:
            minigame_right_2()
        else:
            X += 4
            Y -= 10
            screen.blit(basketball, (X, Y))
            screen.blit(hoop, (300, 200))
            frames += 1
    elif state == "minigame_right_2":
        if frames == 40:
            minigame_right_3()
        else:
            X += 6
            Y -= 8
            screen.blit(basketball, (X, Y))
            screen.blit(hoop, (300, 200))
            frames += 1
    elif state == "minigame_right_3":
        if frames == 50:
            minigame_right_4()
        else:
            X += 5
            Y -= 3
            screen.blit(basketball, (X, Y))
            screen.blit(hoop, (300, 200))
            frames += 1
    elif state == "minigame_right_4":
        if frames == 55:
            minigame_right_5()
        else:
            X += 7
            Y += 3
            screen.blit(basketball, (X, Y))
            screen.blit(hoop, (300, 200))
            frames += 1

    elif state == "minigame_right_5":
        if frames == 70:
            minigame_right_6()
        else:
            X += 7
            Y += 5
            screen.blit(basketball, (X, Y))
            screen.blit(hoop, (300, 200))
            frames += 1

    elif state == "minigame_right_6":
        if frames == 100:
            question()
            draw()
            frames = 0
            X = 100
            Y = 400
        else:
            X += 4
            Y += 10
            screen.blit(basketball, (X, Y))
            screen.blit(hoop, (300, 200))
            frames += 1


# ---------------- MINIGAME ----------------
def minigame_run():

    global state
    state = "minigame"


# OPTIONAL helpers (not required but safe)
def right_basketball():
    screen.blit(basketball, (X, Y))
    screen.blit(hoop, (300, 200))
    global state
    state = "minigame_right_1"

def minigame_right_2():
    screen.blit(basketball, (X, Y))
    screen.blit(hoop, (300, 200))
    global state
    state = "minigame_right_2"

def minigame_right_3():
    screen.blit(basketball, (X, Y))
    screen.blit(hoop, (300, 200))
    global state
    state = "minigame_right_3"

def minigame_right_4():
    screen.blit(basketball, (X, Y))
    screen.blit(hoop, (300, 200))
    global state
    state = "minigame_right_4"

def minigame_right_5():
    screen.blit(basketball, (X, Y))
    screen.blit(hoop, (300, 200))
    global state
    state = "minigame_right_5"

def minigame_right_6():
    screen.blit(basketball, (X, Y))
    screen.blit(hoop, (300, 200))
    global state
    state = "minigame_right_6"


def score():
    screen.blit(basketball, (X, Y))
    screen.blit(hoop, (300, 200))
    global state
    state = "score"

def question():
    global state
    state = "question"

def wrong_basketball():
    print("Wrong")