# game_logic.py

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "draw"
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "scissors" and computer_choice == "paper") or
        (player_choice == "paper" and computer_choice == "rock")
    ):
        return "player"
    else:
        return "computer"



if __name__ == "__main__":
    test_cases = [
        ("rock", "scissors"),
        ("scissors", "rock"),
        ("paper", "rock"),
        ("paper", "paper"),
    ]

    for player, computer in test_cases:
        result = determine_winner(player, computer)
        print(f"Player: {player}, Computer: {computer} => Result: {result}")
