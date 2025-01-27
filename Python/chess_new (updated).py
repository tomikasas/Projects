def is_capture_possible(white_piece, black_piece):
    """Determine if the white piece can capture the black piece."""
    white_type, (white_col, white_row) = white_piece[0], (white_piece[1][0], int(white_piece[1][1]))
    black_col, black_row = black_piece[1][0], int(black_piece[1][1])

    if white_type == 'P':  # Pawn capture logic
        return abs(ord(white_col) - ord(black_col)) == 1 and white_row + 1 == black_row
    elif white_type == 'R':  # Rook capture logic
        return white_col == black_col or white_row == black_row
    return False

# only lets to choose a valid cordinate from a-h and from 1-8 like in a chess board
def is_valid_coordinate(coordinate):
    if len(coordinate) == 2:
        col, row = coordinate[0], coordinate[1]
        if col in 'abcdefgh' and row in '12345678':
            return True
    return False


def main():
    print("Welcome to Chess Piece Selector!\nYou can choose between a Pawn (P) or a Rook (R)")

    # White piece input
    while True:
        user_input = input("Enter the white piece and its position (e.g., 'P a2'): ").strip().lower().split()
        if len(user_input) == 2 and user_input[0] in ['p', 'r'] and is_valid_coordinate(user_input[1]):
            white_piece = (user_input[0].upper(), user_input[1])
            break
        print("Invalid input. Please enter a valid piece type (P or R) and coordinates (a-h, 1-8).")

    # Black pieces input
    black_pieces = []
    print("\nAdd black pieces (up to 16). Type 'done' to finish.")
    while len(black_pieces) < 16:
        user_input = input(f"Enter black piece #{len(black_pieces) + 1} (or type 'done'): ").strip().lower()
        if user_input == 'done' and black_pieces:
            break
        parts = user_input.split()
        if len(parts) == 2 and parts[0] in ['p', 'r'] and is_valid_coordinate(parts[1]) and not is_invalid_black_piece(black_pieces, parts[1], white_piece[1]):
            black_pieces.append((parts[0].upper(), parts[1]))
        else:
            print("Invalid input or position taken. Please enter a valid piece type and coordinates (a-h, 1-8).")

    # Output positions
    print(f"\nWhite piece: {white_piece[0]} at {white_piece[1]}")
    for i, piece in enumerate(black_pieces, start=1):
        print(f"Black piece #{i}: {piece[0]} at {piece[1]}")

    # Check for captures
    captures = [black for black in black_pieces if is_capture_possible(white_piece, black)]
    if captures:
        print(f"\nThe white piece {white_piece[0]} {white_piece[1]} can capture:")
        for i, piece in enumerate(captures, start=1):
            print(f"Black piece #{i}: {piece[0]} at {piece[1]}")
    else:
        print(f"\nThe white piece {white_piece[0]} {white_piece[1]} cannot capture any black pieces.")

#checks if the position is already filled by a black or a white piece
def is_invalid_black_piece(black_pieces, black_coordinates, white_coordinates):
    return black_coordinates == white_coordinates or any(black_coordinates == bp[1] for bp in black_pieces)


if __name__ == "__main__":
    main()
