# ai.py

import random  

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

if __name__ == "__main__":
    for _ in range(5):
        print(f"Computer chose: {get_computer_choice()}")
