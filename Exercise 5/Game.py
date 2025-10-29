"""
Snake - Water - Gun game (like Rock-Paper-Scissors)

Rules:
- Snake drinks Water  -> Snake wins (S beats W)
- Water douses Gun    -> Water wins (W beats G)
- Gun kills Snake     -> Gun wins  (G beats S)

Usage:
- Run the script and choose S / W / G (case-insensitive).
- The computer chooses randomly each round.
- The program shows who won the round and keeps score.
- At the end you can play again.
"""

import random

# valid moves and their readable names
MOVES = {"S": "Snake", "W": "Water", "G": "Gun"}

def get_computer_move():
    """Return a random move key from MOVES."""
    return random.choice(list(MOVES.keys()))

def decide_winner(player, computer):
    """
    Decide the winner of a single round.
    Returns: "player", "computer", or "tie"
    Rules:
      S beats W (Snake drinks Water)
      W beats G (Water douses Gun)
      G beats S (Gun kills Snake)
    """
    if player == computer:
        return "tie"

    # Winning combinations for player
    wins = {
        ("S", "W"),  # Snake beats Water
        ("W", "G"),  # Water beats Gun
        ("G", "S"),  # Gun beats Snake
    }

    if (player, computer) in wins:
        return "player"
    else:
        return "computer"

def input_player_move():
    """
    Prompt the user for a move.
    Accepts full word or single letter: snake, water, gun or S/W/G
    Returns uppercase key "S", "W", or "G".
    """
    while True:
        choice = input("Choose [S]nake, [W]ater or [G]un: ").strip().lower()
        if not choice:
            print("Please enter something (S, W, or G).")
            continue

        # normalize common inputs
        if choice in ("s", "snake"):
            return "S"
        if choice in ("w", "water"):
            return "W"
        if choice in ("g", "gun"):
            return "G"

        print("Invalid choice. Enter S, W, G or the full word (snake, water, gun).")

def play_round():
    """Play a single round and return result and moves."""
    player_move = input_player_move()
    computer_move = get_computer_move()

    result = decide_winner(player_move, computer_move)

    # user-friendly printout
    print(f"\nYou chose:     {MOVES[player_move]}")
    print(f"Computer chose:{MOVES[computer_move]}")

    if result == "tie":
        print("Result: It's a tie!")
    elif result == "player":
        print("Result: You win this round! 🎉")
    else:
        print("Result: Computer wins this round. 🤖")

    return result, player_move, computer_move

def play_game():
    """Main game loop. Lets user choose number of rounds or best-of."""
    print("Welcome to Snake, Water, Gun!")
    while True:
        # Choose play mode
        mode = input("\nPlay mode - Enter number of rounds (e.g., 3), or 'b' for best-of (odd number): ").strip().lower()

        if mode == "b":
            # best-of mode
            while True:
                try:
                    n = int(input("Best of how many rounds? (must be odd, e.g., 3,5,7): ").strip())
                    if n % 2 == 1 and n > 0:
                        rounds = n
                        break
                    else:
                        print("Please enter a positive odd number.")
                except ValueError:
                    print("Please enter a valid integer.")
        else:
            try:
                rounds = int(mode)
                if rounds <= 0:
                    print("Please enter a positive integer for rounds.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a positive integer or 'b'.")
                continue

        # Play the rounds
        player_score = 0
        computer_score = 0
        ties = 0

        for r in range(1, rounds + 1):
            print("\n" + "-" * 30)
            print(f"Round {r} of {rounds}:")
            result, _, _ = play_round()

            if result == "player":
                player_score += 1
            elif result == "computer":
                computer_score += 1
            else:
                ties += 1

            print(f"\nScores → You: {player_score} | Computer: {computer_score} | Ties: {ties}")

            # Early termination for best-of: if either reaches majority
            if rounds % 2 == 1:
                majority = rounds // 2 + 1
                if player_score == majority or computer_score == majority:
                    print("\nA player has reached majority. Ending early.")
                    break

        # Final result summary
        print("\n" + "=" * 40)
        print("Final Scores:")
        print(f"You: {player_score}")
        print(f"Computer: {computer_score}")
        print(f"Ties: {ties}")

        if player_score > computer_score:
            print("\n🎉 Congratulations — you won the game!")
        elif computer_score > player_score:
            print("\n🤖 Computer won this time. Try again!")
        else:
            print("\nIt's a draw overall.")

        # Play again?
        again = input("\nDo you want to play again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Thanks for playing — goodbye!")
            break

if __name__ == "__main__":
    play_game()
