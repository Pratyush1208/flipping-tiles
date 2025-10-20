import random

def create_board(size):
    """Creates a shuffled board with pairs of numbers."""
    num_pairs = (size * size) // 2
    numbers = list(range(1, num_pairs + 1)) * 2
    random.shuffle(numbers)
    board = [numbers[i * size:(i + 1) * size] for i in range(size)]
    return board

def display_board(visible, revealed):
    """Displays the current state of the board."""
    for i in range(len(visible)):
        for j in range(len(visible[i])):
            print(visible[i][j] if revealed[i][j] else "X", end=" ")
        print()
    print()

def flip_tiles(board, revealed, pos1, pos2):
    """Checks if two flipped tiles match."""
    r1, c1 = pos1
    r2, c2 = pos2

    if board[r1][c1] == board[r2][c2]:
        revealed[r1][c1] = True
        revealed[r2][c2] = True
        return True
    return False

def play_game(size=4):
    """Main game logic for flipping tiles."""
    board = create_board(size)
    revealed = [[False] * size for _ in range(size)]
    visible = [[str(board[i][j]) for j in range(size)] for i in range(size)]
    attempts = 0
    matches = 0
    total_pairs = (size * size) // 2

    print("Welcome to the Flipping Tiles Game!\n")
    while matches < total_pairs:
        display_board(visible, revealed)
        try:
            r1, c1 = map(int, input("Enter first tile position (row col): ").split())
            r2, c2 = map(int, input("Enter second tile position (row col): ").split())
        except ValueError:
            print("Invalid input. Enter numbers like '1 2'.\n")
            continue

        if revealed[r1][c1] or revealed[r2][c2] or (r1 == r2 and c1 == c2):
            print("Invalid move. Try again.\n")
            continue

        print(f"Tiles: {board[r1][c1]} and {board[r2][c2]}")
        if flip_tiles(board, revealed, (r1, c1), (r2, c2)):
            print("🎉 It's a match!\n")
            matches += 1
        else:
            print("❌ Not a match.\n")

        attempts += 1

    print(f"Congratulations! You completed the game in {attempts} attempts!")

if __name__ == "__main__":
    play_game()
