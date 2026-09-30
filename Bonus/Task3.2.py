import random

start_penalties = 12
rounds = 3

def get_secret(player):
    while True:
        word = input(f"{player}, type your secret word: ").strip().lower()
        if len(word) >= 3 and word.isascii() and word.isalpha():
            return word
        print("Letters only, at least 3 letters!")

def clear_screen():
    print("\n" * 50)

def get_char():
    while True:
        char = input("Enter a letter: ").strip().lower()
        if len(char) == 1 and char.isascii() and char.isalpha():
            return char
        print("Please enter a single letter!")

def play_turn(player, word):
    shown = ["_"] * len(word)
    guessed = []
    used = 0
    while used < start_penalties:
        print()
        print(player, "-", " ".join(shown))
        print("Penalties used:", used, "/", start_penalties)
        choice = input("1) Guess a letter\n2) Guess the full word\n> ").strip()
        if choice == "1":
            char = get_char()
            if char in guessed:
                print("You already guessed that!")
                continue
            guessed.append(char)
            if char in word:
                for i in range(len(word)):
                    if word[i] == char:
                        shown[i] = char
                if "_" not in shown:
                    print("You found the word:", word)
                    return used
            else:
                print("Wrong guess")
                used += 1
        elif choice == "2":
            if input("Enter the full word: ").strip().lower() == word:
                print("Correct! The word was:", word)
                return used
            print("Wrong guess")
            used += 5
        else:
            print("Enter a valid choice!")
    print("Out of penalties! The word was:", word)
    return start_penalties

def main():
    players = ["Player 1", "Player 2"]
    wins = [0, 0]
    total = [0, 0]

    for r in range(1, rounds + 1):
        print(f"\n===== ROUND {r} =====")
        pens = [0, 0]
        for setter in range(2):
            guesser = 1 - setter
            word = get_secret(players[setter])
            clear_screen()
            pens[guesser] = play_turn(players[guesser], word)

        total[0] += pens[0]
        total[1] += pens[1]
        print(f"\nRound {r}: {players[0]} = {pens[0]} penalties, {players[1]} = {pens[1]} penalties")
        if pens[0] < pens[1]:
            wins[0] += 1
            print(players[0], "wins the round!")
        elif pens[1] < pens[0]:
            wins[1] += 1
            print(players[1], "wins the round!")
        else:
            print("Round tie, no point.")

    print("\n===== FINAL =====")
    print(f"{players[0]}: {wins[0]} round wins, {total[0]} total penalties")
    print(f"{players[1]}: {wins[1]} round wins, {total[1]} total penalties")
    if wins[0] > wins[1]:
        print(players[0], "wins the game!")
    elif wins[1] > wins[0]:
        print(players[1], "wins the game!")
    else:
        print("It's a tie!")

main()