from random import choice, random

print("Game Manual:\n"
      "Scissors cuts Paper\n"
      "Paper covers Rock\n"
      "Rock crushes Lizard\n"
      "Lizard poisons Spock\n"
      "Spock smashes Scissors\n"
      "Scissors decapitates Lizard\n"
      "Lizard eats Paper\n"
      "Paper disproves Spock\n"
      "Spock vaporizes Rock\n"
      "and as it always has Rock crushes Scissors")

class LoadGame:
    def __init__(self):
        self.computer_points = 0
        self.player_points = 0
        self.actions = ["rock", "paper", "scissors", "lizard", "spock"]
        self.computer_choice = None  # Initialize computer choice

    def play_round(self, player_choice, mdp):
        self.computer_choice = self.choose_action(mdp)  # Choose action based on Q-table
        return self.computer_choice, self.determine_outcome(player_choice)

    def determine_outcome(self, player_choice):
        if player_choice == self.computer_choice:
            print(f"It's a tie! Both chose {player_choice}.")
            return 0  # Tie reward
        elif self.win(player_choice):
            return 1  # Win reward
        else:
            return -1  # Loss penalty

    def win(self, player_choice):
        if (player_choice == 'scissors' and self.computer_choice in ['paper', 'lizard']) or \
           (player_choice == 'paper' and self.computer_choice in ['rock', 'spock']) or \
           (player_choice == 'rock' and self.computer_choice in ['lizard', 'scissors']) or \
           (player_choice == 'lizard' and self.computer_choice in ['spock', 'paper']) or \
           (player_choice == 'spock' and self.computer_choice in ['scissors', 'rock']):
            print(f"You win! {player_choice} beats {self.computer_choice}.")
            self.player_points += 1
            return True
        else:
            self.lose(player_choice)
            return False

    def lose(self, player_choice):
        if (self.computer_choice == 'scissors' and player_choice in ['paper', 'lizard']) or \
           (self.computer_choice == 'paper' and player_choice in ['rock', 'spock']) or \
           (self.computer_choice == 'rock' and player_choice in ['lizard', 'scissors']) or \
           (self.computer_choice == 'lizard' and player_choice in ['spock', 'paper']) or \
           (self.computer_choice == 'spock' and player_choice in ['scissors', 'rock']):
            print(f"You lose! {self.computer_choice} beats {player_choice}.")
            self.computer_points += 1

    def get_scores(self):
        print(f"Player Points: {self.player_points}, Computer Points: {self.computer_points}")

    def choose_action(self, mdp):
        # Choose action based on Q-values, with exploration
        exploration_rate = 0.2  # Rate for exploring new actions
        if random() < exploration_rate:
            return choice(self.actions)  # Random choice for exploration
        else:
            # Choose action with the highest Q-value
            return max(self.actions, key=lambda action: max(mdp.Q_table[action].values()))


class MDP:
    def __init__(self, game):
        self.game = game 
        self.Q_table = {action: {action: 0 for action in game.actions} for action in game.actions}
        self.learning_rate = 0.1
        self.discount_factor = 0.9
        self.history = []  # Store the history of actions and rewards

    def update_Q_table(self, player_action, computer_action, reward):
        if self.history:
            # Get the last action and its reward
            prev_player_action, prev_computer_action, prev_reward = self.history[-1]
            # Update the Q-value using the Q-learning formula
            max_future_q = max(self.Q_table[player_action].values())
            self.Q_table[prev_player_action][prev_computer_action] += self.learning_rate * (
                reward + self.discount_factor * max_future_q -
                self.Q_table[prev_player_action][prev_computer_action]
            )
        # Append the current action and reward to history
        self.history.append((player_action, computer_action, reward))

    def print_Q_table(self):
        print("Q-table:")
        for state, actions in self.Q_table.items():
            print(f"{state}: {actions}")


# Main Game Loop
if __name__ == "__main__":
    game = LoadGame()  
    mdp = MDP(game)  

    while True:
        user_input = input("What is your act (rock, paper, scissors, lizard, spock): ").lower()

        if user_input in game.actions:
            computer_action, reward = game.play_round(user_input, mdp)  # Pass mdp to play_round
            game.get_scores()  # Display scores
            
            # Update the MDP Q-table with the current round's results
            mdp.update_Q_table(user_input, computer_action, reward)
            
            # Print Q-table after each round
            mdp.print_Q_table()
            
            input_continue = input("Do you wanna continue? (Y/N) ")
            if input_continue.upper() == 'N':
                break
        else:
            print("Invalid input! Please choose between rock, paper, scissors, lizard, or spock.")
