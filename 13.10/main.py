# main.py

from game_logic import determine_winner
import ai 

def main():
    print("Гра: Камінь, Ножиці, Папір")
    choices = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0

    rounds = int(input("Скільки раундів ви хочете зіграти? "))

    for round_num in range(1, rounds + 1):
        print(f"\nРаунд {round_num}")
        player_choice = input("Ваш вибір (rock/paper/scissors): ").lower()

        if player_choice not in choices:
            print("❌ Недійсний вибір. Спробуйте ще раз.")
            continue

        computer_choice = ai.get_computer_choice()
        print(f"Комп’ютер обрав: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)

        if result == "draw":
            print("🤝 Нічия!")
        elif result == "player":
            print("✅ Ви виграли цей раунд!")
            player_score += 1
        else:
            print("💻 Комп’ютер виграв цей раунд!")
            computer_score += 1

    
    print("\n🎯 Кінцевий рахунок:")
    print(f"Ви: {player_score} | Комп’ютер: {computer_score}")

    if player_score > computer_score:
        print("🎉 Вітаємо, ви переможець гри!")
    elif computer_score > player_score:
        print("😞 Ви програли. Спробуйте ще раз!")
    else:
        print("🔁 Нічия. Гарна гра!")


if __name__ == "__main__":
    main()
