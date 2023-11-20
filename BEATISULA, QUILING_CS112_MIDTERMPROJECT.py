# Importing necessary modules
import turtle
import random

# ASCII art representations for the stages of the hangman
stages = [''' 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Initializing the turtle screen
screen = turtle.Screen()
screen.title("Hangman Turtle Game")
screen.bgcolor("white")
screen.setup(width=600, height=600)

# Turtle for displaying the welcome message
welcome_turtle = turtle.Turtle()
welcome_turtle.hideturtle()
welcome_turtle.penup()
welcome_turtle.goto(0, 200)
welcome_turtle.write("Welcome to Hangman!", align="center", font=("Courier New", 24, "normal"))

# Turtle for displaying the hangman art
hangman_turtle = turtle.Turtle()
hangman_turtle.hideturtle()
hangman_turtle.penup()
hangman_turtle.goto(0, 0)

# ASCII art representation for Hangman
hangman_art = """
  +---+
  |   |
      |
      |
      |
      |
========="""

# Displaying the initial hangman art
hangman_turtle.write(hangman_art, align="center", font=("Courier New", 16, "normal"))

# Hangman code
print("WELCOME TO HANGMAN!")
print()

# List of words for the game
word_list = ['apple', 'banana', 'cat', 'dog', 'happy', 'sun', 'tree', 'flower', 'red', 'blue', 'green', 'bird', 'book', 'pen',
             'run', 'jump', 'swim', 'small', 'big', 'hot', 'cold', 'rain', 'wind', 'snow', 'play', 'eat', 'sleep', 'friend',
             'smile', 'laugh', 'school', 'learn', 'easy', 'hard', 'fast', 'slow', 'happy', 'sad', 'good', 'bad', 'help',
             'kind', 'love', 'hug', 'star', 'moon', 'sky', 'sea', 'simple']

# Turtle for drawing lines representing the chosen_word
line_turtle = turtle.Turtle()
line_turtle.hideturtle()
line_turtle.penup()

# Choosing a random word from the word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Calculating the starting position to center the boxes
start_x = -((word_length * 40) // 2)  # Adjust 40 based on your box size

# Setting the starting position for drawing lines
line_turtle.goto(start_x, -100)

# Drawing lines for each letter in the chosen_word
line_size = 30
for _ in range(word_length):
    line_turtle.pendown()
    line_turtle.forward(line_size)
    line_turtle.penup()
    line_turtle.forward(10)  # Adding some space between boxes

# Initializing game variables
end_of_game = False
lives = 6

# Display list for tracking the guessed letters
display = ["_"] * word_length
print(display)

# Main game loop
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Checking if the letter has already been guessed
    if guess in display:
        print(f"You've already guessed {guess}")
    # Checking if the guessed letter is in the chosen_word
    elif guess in chosen_word:
        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = guess

        # Updating the display with the current state
        line_turtle.clear()
        line_turtle.goto(start_x, -100)
        for letter in display:
            line_turtle.write(letter, align="center", font=("Courier New", 16, "normal"))
            line_turtle.forward(40)  # Assuming a fixed width for the boxes

    # Handling incorrect guesses
    else:
        lives -= 1  # Decreasing lives by 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        # Ending the game if lives reach 0
        if lives == 0:
            end_of_game = True
            print("You lose.")
            hangman_turtle.write("You lose.", align="center", font=("Courier New", 24, "normal"))
            break

    # Checking if the word has been completely guessed
    if "_" not in display:
        end_of_game = True
        print("You win.")
        hangman_turtle.write("You win!", align="center", font=("Courier New", 24, "normal"))
        break

    # Updating the hangman display
    hangman_turtle.clear()
    hangman_turtle.write(stages[lives], align="center", font=("Courier New", 16, "normal"))

# Creating a turtle for displaying the chosen word
chosen_word_turtle = turtle.Turtle()
chosen_word_turtle.hideturtle()
chosen_word_turtle.penup()
chosen_word_turtle.goto(0, -150)  # Adjust the y-coordinate based on your preference

# Displaying the chosen word if the player loses
if lives == 0:
    chosen_word_turtle.write(f"Chosen Word: {chosen_word}", align="center", font=("Courier New", 16, "normal"))

# Keeping the window open
turtle.mainloop()
