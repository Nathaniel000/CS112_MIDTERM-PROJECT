#creating a hangman game, where the hangman and output is presented in the turtle funtion. 
import turtle
import random
from hangman_art import stages

# initialize turtle
screen = turtle.Screen()
screen.title("Hangman Turtle Game")
screen.bgcolor("white")
screen.setup(width=600, height=600)

hangman_turtle = turtle.Turtle()
hangman_turtle.speed(0)
hangman_turtle.hideturtle()
hangman_turtle.penup()
hangman_turtle.goto(-200, -200)

#welcome message 
welcome_turtle = turtle.Turtle()
welcome_turtle.hideturtle()
welcome_turtle.penup()
welcome_turtle.goto(0, 200)
welcome_turtle.write("Welcome to Hangman!", align="center", font=("Courirer New", 24, "normal"))

# hangman turtle, welcome
hangman_turtle = turtle.Turtle()
hangman_turtle.hideturtle()
hangman_turtle.penup()
hangman_turtle.goto(0, 0)

#art for Hangman
hangman_art = """
  +---+
  |   |
      |
      |
      |
      |
========="""

# display art
hangman_turtle.write(hangman_art, align="center", font=("Courier New", 16, "normal"))

# hangman code
print("WELCOME TO HANGMAN!")
print()

word_list = ['apple', 'banana', 'cat', 'dog', 'happy', 'sun', 'tree', 'flower', 'red', 'blue', 'green', 'bird', 'book', 'pen',
             'run', 'jump', 'swim', 'small', 'big', 'hot', 'cold', 'rain', 'wind', 'snow', 'play', 'eat', 'sleep', 'friend',
             'smile', 'laugh', 'school', 'learn', 'easy', 'hard', 'fast', 'slow', 'happy', 'sad', 'good', 'bad', 'help',
             'kind', 'love', 'hug', 'star', 'moon', 'sky', 'sea', 'simple']

# create turtle lines representing the chosen_word
line_turtle = turtle.Turtle()
line_turtle.hideturtle()
line_turtle.penup()

# chosen word, choosing random word from the word_list
chosen_word = random.choice(word_list)  
word_length = len(chosen_word)

# to calculate the starting position to center the boxes
start_x = -((word_length * 40) // 2)  # Adjust 40 based on your box size

line_turtle.goto(start_x, -100)

# Draw line for each letter in the chosen_word
line_size = 30
for _ in range(word_length):
    line_turtle.pendown()
    line_turtle.forward(line_size)
    line_turtle.penup()
    line_turtle.forward(10)  # add some space between boxes

end_of_game = False
lives = 6

#display 
display = ["_"] * word_length
print(display)

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")
    elif guess in chosen_word:
        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = guess

        # update with the current state
        line_turtle.clear()
        line_turtle.goto(start_x, -100)
        for letter in display:
            line_turtle.write(letter, align="center", font=("Courier New", 16, "normal"))
            line_turtle.forward(40)  # assuming a fixed width for the boxes

    else:
        lives -= 1 #-=1 to substract from the 6 lives
        print(f"You guessed {guess}, that's not in the word. You lose a life.") 
        if lives == 0: #if lives = 0 then the game is over
            end_of_game = True
            print("You lose.")
            hangman_turtle.write("You lose.", align="center", font=("Courier New", 24, "normal"))
            break

    if "_" not in display: #display win 
        end_of_game = True
        print("You win.")
        hangman_turtle.write("You win!", align="center", font=("Courier New", 24, "normal"))
        break

    hangman_turtle.clear()
    hangman_turtle.write(stages[lives], align="center", font=("Courier New", 16, "normal")) #display the hangman art
    
# creating a turtle for displaying the chosen word
chosen_word_turtle = turtle.Turtle()
chosen_word_turtle.hideturtle()
chosen_word_turtle.penup()
chosen_word_turtle.goto(0, -150)  # adjust the y-coordinate based on your preference

if lives == 0:    
    chosen_word_turtle.write(f"Chosen Word: {chosen_word}", align="center", font=("Courier New", 16, "normal"))

# keep the window open
turtle.mainloop()

