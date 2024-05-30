import random as rd
print("(Welcome to hungman game)")
print("Guess the word")
print("-----------------------------------------------Instruction-------------------------------------------------")
print("Of course! Here you go:")

print("1. Guess letters to reveal a hidden word while avoiding incorrect guesses that lead to the drawing of a "
      "hangman figure, aiming to uncover the word before the hangman is fully drawn.")
print("2. The game starts with a blank display representing the letters of the word as underscores, and players make "
      "guesses one letter at a time.")
print("3. Correct guesses replace underscores with the guessed letter in their correct positions within the word, "
      "while incorrect guesses result in parts of the hangman being drawn.")
print("4. The hangman drawing progresses with each incorrect guess, typically depicting the gallows, head, body, "
      "arms, and legs.")
print("5. The game ends in victory if the word is fully revealed before the hangman is drawn, but ends in defeat if "
      "the hangman is completed before the word is guessed correctly.")
print("-------------------------------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------------------------------")

print("-------------------------------------------------------------------------------------------------------------")
print("Lets guess the word")


def display_hangman(tries):
    stages = [
        """
           ------
           |    |
           O    |
          /|\   |
          / \   |
                |
        ---------
        """,
        """
           ------
           |    |
           O    |
          /|\   |
          /     |
                |
        ---------
        """,
        """
           ------
           |    |
           O    |
          /|\   |
                |
                |
        ---------
        """,
        """
           ------
           |    |
           O    |
          /|\   |
                |
                |
        ---------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        ---------
        """,
        """
           -----
           |    |
           O    |
                |
                |
                |
        ---------
        """,
        """
           -----
           |    |
                |
                |
                |
                |
        ---------
        """
    ]
    return stages[tries]

lives = 6
word= [
    "karachi",
    "lahore",
    "islamabad",
    "rawalpindi",
    "faisalabad",
    "multan",
    "peshawar",
    "quetta",
    "muree",
    "sialkot"
]


g_word = rd.choice(word)
display = []
for letter in g_word:
    display += "_"
print(display)
game_over = False
while not game_over:
    g_letter = input("\nEnter your guessed letter: ").lower()
    for position in range(len(g_word)):
        letter = g_word[position]
        if letter == g_letter:  # its checks the guess letter is in the word
            print("great")
            display[position] = g_letter  # it displays the letter with the blank space '_'
    print(display)
    if g_letter not in g_word:
        lives -= 1
        print(f"\nThe remaining lives is {lives}")
        if lives == 0:
            print("\nYou lose the game")
            print("All the lives is exhausted")
            game_over = True
    print(display_hangman(lives))
    if "_" not in display:
        print("\nYou won the game")
        game_over = True

print("Thank u for palying this game")