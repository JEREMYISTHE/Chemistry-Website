import pygame
from Settings import *

article_1_button = pygame.Rect(50, 50, 150, 50)
article_2_button = pygame.Rect(250, 50, 150, 50)
article_3_button = pygame.Rect(450, 50, 150, 50)
article_4_button = pygame.Rect(50, 200, 150, 50)
X_button = pygame.Rect(15, 10, 30, 28)

state = "menu"

# --- ARTICLE 1 ---
a1_l1 = font.render("Atoms come together at certain times. They do this so that they can complete their shells.", True, BLACK)
a1_l2 = font.render("Shells are the layers of an atom. They are what atoms want to always achieve. Any atom would love to complete their shells", True, BLACK)
a1_l3 = font.render("complete their shells through other atoms. Think of atoms as people. They always want their goal. Money. To atoms, completing", True, BLACK)
a1_l4 = font.render("their shells is like winning the lottery.", True, BLACK)
a1_l5 = font.render("Atoms can complete their shells in one way. Bonding. This happens when an atom goes to another one and they do one of 3 things.", True, BLACK)
a1_l6 = font.render("Give, share, or take.", True, BLACK)
a1_l7 = font.render("Giving electrons allow them to complete their shells if they are 1 or 2 more electrons than a shell. They give other atoms electrons.", True, BLACK)
a1_l8 = font.render("Taking is when they get something from another atom. This happens a lot to atoms who are 1 or 2 electrons more than a full shell.", True, BLACK)
a1_l9 = font.render("Finally, sharing electrons is when 2 atoms decide to both use an atom of the other. This is called covalence,", True, BLACK)
a1_l10 = font.render("while giving and taking is called ionic bonding. Polar covalent bonds are a mix of the two.", True, BLACK)
a1_l11 = font.render("How much another atom wants to interact with other atoms is called electronegativity. The highest electronegative atom is ", True, BLACK)
a1_l12 = font.render("Fluorine with an electronegativity of about 4.", True, BLACK)

# --- ARTICLE 2 ---
a2_l1 = font.render("Atoms make up everything. Yes. Everything. From your hair, to your water, to your waste, atoms make them up.", True, BLACK)
a2_l2 = font.render("You might be wondering, why don't I see atoms? It is because atoms are so small, you can only see them with a microscope. In", True, BLACK)
a2_l3 = font.render("fact, the width of a single strand of hair is about a million times the size of a carbon atom.", True, BLACK)
a2_l4 = font.render("Atoms are made of even smaller things called electrons, protons, and neutrons. An electron gives a negative", True, BLACK)
a2_l5 = font.render("charge, a proton releases a positive charge, and the neutrons provide a neutral charge. The neutrons and protons meet", True, BLACK)
a2_l6 = font.render("in the middle, making the nucleus. The protons in the nucleus make sure the electrons stay in the atom.", True, BLACK)
a2_l7 = font.render("How do atoms make up everything? Well, they form and work together to make different things. For example, hydrogen and oxygen", True, BLACK)
a2_l8 = font.render("combine to create water. Any 2 atoms combined are called molecules. You can see the article, Bonding to see how atoms create", True, BLACK)
a2_l9 = font.render("different chemicals and substances that make up our world.", True, BLACK)

# --- ARTICLE 3 ---
a3_l1 = font.render("Everything is matter. Water, ice, and oxygen is all matter. Matter is anything that takes up space. Matter comes in 3 ways.", True, BLACK)
a3_l2 = font.render("Liquid, solid, and gas.", True, BLACK)
a3_l3 = font.render("Liquids are anything that may still move, but will fill up a container. Think about a glass cup. The water will go in it, but not leave.", True, BLACK)
a3_l4 = font.render("Solids are solid. They may be touched and felt if still. They would be the glass in a glass cup filled with water.", True, BLACK)
a3_l5 = font.render("Finally, gases are not able to be felt. They try to be as free as they can and always try to move.", True, BLACK)
a3_l6 = font.render("Each state of matter is made up in a different way. In a solid, molecules are very compact and together.", True, BLACK)
a3_l7 = font.render("In a liquid, they are free, but don't move to much, and in a gas, they move around randomly and quickly.", True, BLACK)
a3_l8 = font.render("When atoms get cold, they move slower and condense into liquids and solids. When they get hotter, they move faster, which provides", True, BLACK)
a3_l9 = font.render("the opposite affect, making liquids and gases.", True, BLACK)

a4_l1 = font.render("The PH scale is an important scale used to measure how acidic something is. It is involved with acids and bases and everything has", True, BLACK)
a4_l2 = font.render("a PH level. Water, Soda, Lemons, they all can be measured in PH.", True, BLACK)
a4_l3 = font.render("PH is measured from 0 - 14, with 0 being acidic and 14 being a base. 7 is the neutral. Water is a 7 on the PH scale, lemon is a 2 and", True, BLACK)
a4_l4 = font.render("soap is a 12, meaning it is a base", True, BLACK)
a4_l5 = font.render("The differences between acids and bases is that acids taste sour while bases taste bitter. Also, chemically, acids release hydrogen", True, BLACK)
a4_l6 = font.render("ions while bases usually pick up the ions released.", True, BLACK)
a4_l7 = font.render("Common examples of acids include lemons, vinegar, and battery acid. Common examples of bases are soap, bleach and baking", True, BLACK)
a4_l8 = font.render("soda.", True, BLACK)


def draw():
    # DRAW X BUTTON ON EVERY SCREEN
    pygame.draw.rect(screen, WHITE, X_button)
    screen.blit(X_Button, (20, 15))

    if state == "menu":
        pygame.draw.rect(screen, GREEN, article_1_button)
        pygame.draw.rect(screen, GREEN, article_2_button)
        pygame.draw.rect(screen, GREEN, article_3_button)
        pygame.draw.rect(screen, GREEN, article_4_button)

        screen.blit(font.render("Bonding", True, BLACK), (90,75))
        screen.blit(font.render("Atoms", True, BLACK), (300,75))
        screen.blit(font.render("States of Matter", True, BLACK), (470,75))
        screen.blit(font.render("PH Scale", True, BLACK), (90,225))

    elif state == "a1":
        screen.blit(a1_l1, (25, 100))
        screen.blit(a1_l2, (25, 150))
        screen.blit(a1_l3, (25, 175))
        screen.blit(a1_l4, (25, 200))
        screen.blit(a1_l5, (25, 250))
        screen.blit(a1_l6, (25, 275))
        screen.blit(a1_l7, (25, 325))
        screen.blit(a1_l8, (25, 350))
        screen.blit(a1_l9, (25, 375))
        screen.blit(a1_l10, (25, 400))
        screen.blit(a1_l11, (25, 425))
        screen.blit(a1_l12, (25, 450))

    elif state == "a2":
        screen.blit(a2_l1, (25, 100))
        screen.blit(a2_l2, (25, 150))
        screen.blit(a2_l3, (25, 175))
        screen.blit(a2_l4, (25, 225))
        screen.blit(a2_l5, (25, 250))
        screen.blit(a2_l6, (25, 275))
        screen.blit(a2_l7, (25, 325))
        screen.blit(a2_l8, (25, 350))
        screen.blit(a2_l9, (25, 375))

    elif state == "a3":
        screen.blit(a3_l1, (25, 100))
        screen.blit(a3_l2, (25, 115))
        screen.blit(a3_l3, (25, 150))
        screen.blit(a3_l4, (25, 165))
        screen.blit(a3_l5, (25, 200))
        screen.blit(a3_l6, (25, 235))
        screen.blit(a3_l7, (25, 270))
        screen.blit(a3_l8, (25, 305))
        screen.blit(a3_l9, (25, 320))

    elif state == "a4":
        screen.blit(a4_l1, (25, 100))
        screen.blit(a4_l2, (25, 115))
        screen.blit(a4_l3, (25, 150))
        screen.blit(a4_l4, (25, 165))
        screen.blit(a4_l5, (25, 200))
        screen.blit(a4_l6, (25, 215))
        screen.blit(a4_l7, (25, 240))
        screen.blit(a4_l8, (25, 255))
