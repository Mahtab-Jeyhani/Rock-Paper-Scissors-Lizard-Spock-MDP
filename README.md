# Rock-Paper-Scissors-Lizard-Spock Game

## Overview
This is a simple implementation of the Rock-Paper-Scissors-Lizard-Spock game using Python, featuring a Markov Decision Process (MDP) that enables the computer to learn from the player's actions through a Q-learning algorithm.

## Game Manual
Here’s a quick overview of how the game works:
- **Scissors cuts Paper**
- **Paper covers Rock**
- **Rock crushes Lizard**
- **Lizard poisons Spock**
- **Spock smashes Scissors**
- **Scissors decapitates Lizard**
- **Lizard eats Paper**
- **Paper disproves Spock**
- **Spock vaporizes Rock**
- **Rock crushes Scissors**

## Classes
### LoadGame
- **Attributes**:
    - `computer_points`: Tracks the computer's score.
    - `player_points`: Tracks the player's score.
    - `actions`: List of possible actions (rock, paper, scissors, lizard, spock).
    - `computer_choice`: Stores the computer's current choice.
    
- **Methods**:
    - `play_round(player_choice, mdp)`: Plays a round with the player's choice and the MDP instance.
    - `determine_outcome(player_choice)`: Determines the outcome of the round based on the player's choice.
    - `get_scores()`: Displays the current scores.
    - `choose_action(mdp)`: Chooses an action for the computer based on the Q-table and exploration strategy.

### MDP (Markov Decision Process)
- **Attributes**:
    - `game`: Reference to the LoadGame instance.
    - `Q_table`: A dictionary to store the Q-values for each action.
    - `learning_rate`: Rate at which the Q-values are updated.
    - `discount_factor`: Factor for future reward consideration.
    - `history`: Stores the history of actions and rewards.
    
- **Methods**:
    - `update_Q_table(player_action, computer_action, reward)`: Updates the Q-table based on the player's and computer's actions and the reward received.
    - `print_Q_table()`: Prints the current Q-table.

## Main Loop
The main game loop prompts the player to enter their action, plays a round, updates the Q-table, and prints the scores and Q-table after each round. The player can continue playing or exit the game.
