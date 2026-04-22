word = input("What word would you like to check? ") # Correct input prompt
char_value = 0

while True:
    for char in word:
        # Compare characters to string literals (e.g., 'a')
        if char == 'a':
            char_value += 1
        elif char == 'b':
            char_value += 2
        elif char == 'c':
            char_value += 3
        elif char == 'd':
            char_value += 4
        elif char == 'e':
            char_value += 5
        elif char == 'f':
            char_value += 6
        elif char == 'g':
            char_value += 7
        elif char == 'h':
            char_value += 8
        elif char == 'i':
            char_value += 9
        elif char == 'j':
            char_value += 10
        elif char == 'k':
            char_value += 11
        elif char == 'l':
            char_value += 12
        elif char == 'm': # Added colon here
            char_value += 13
        elif char == 'n':
            char_value += 14
        elif char == 'o':
            char_value += 15
        elif char == 'p':
            char_value += 16
        elif char == 'q':
            char_value += 17
        elif char == 'r':
            char_value += 18
        elif char == 's':
            char_value += 19
        elif char == 't':
            char_value += 20
        elif char == 'u':
            char_value += 21
        elif char == 'v':
            char_value += 22
        elif char == 'w':
            char_value += 23
        elif char == 'x':
            char_value += 24
        elif char == 'y':
            char_value += 25
        elif char == 'z':
            char_value += 26
        else:
            print("Invalid") # Corrected typo

    print(char_value)
    char_value = 0
    word = input("What word would you like to check? ")  # Correct input prompt
