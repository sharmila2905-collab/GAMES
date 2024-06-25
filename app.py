import streamlit as st
from game import RockPaperScissors 

# Set page title and configure layout
st.set_page_config(page_title="Rock Paper Scissors", layout="centered")
# Display application title and description
st.title("Rock Paper Scissors Game")
st.write("Choose your move and see if you can beat the computer!")

# Create an instance o f the game
game = RockPaperScissors()

# Get user input
player_choice = st.selectbox("Select your move:", game.choices)

# Play the game
if st.button("Play"):
    try:
        # Call the play method to determine the result and computer's choice
        result, computer_choice = game.play(player_choice)
        
        # Display the player's and computer's choices
        st.write("You chose:", player_choice)
        st.write("Computer chose:", computer_choice)
        
        # Display the result and scores
        st.write(result)
        st.write("Player Score:", game.player_score)
        st.write("Computer Score:", game.computer_score)
    except ValueError as e:
        # Handle invalid choices by displaying an error message
        st.write("Error:", str(e))
import random

class RockPaperScissors:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.player_score = 0
        self.computer_score = 0

    def play(self, player_choice):
        # Randomly select the computer's choice
        computer_choice = random.choice(self.choices)

        # Validate the player's choice
        if player_choice not in self.choices:
            raise ValueError("Invalid choice. Please select 'rock', 'paper', or 'scissors'.")

        # Determine the result based on the choices
        if player_choice == computer_choice:
            result = "It's a tie!"
        elif (
            (player_choice == "rock" and computer_choice == "scissors") or
            (player_choice == "paper" and computer_choice == "rock") or
            (player_choice == "scissors" and computer_choice == "paper")
        ):
            # Player wins
            self.player_score += 1
            result = "You win!"
        else:
            # Computer wins
            self.computer_score += 1
            result = "Computer wins!"

        return result, computer_choice