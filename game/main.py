from models import Card, Position


def print_board(cards, board_size_x, board_size_y):
    for y in range(board_size_y):
        for x in range(board_size_x):
            for card in cards:
                if card.position.x == x and card.position.y == y:
                    print(card.get_symbol() + " ", end="")
                    break
            else:  # po pętli for, jeśli nie było break
                print(". ", end="")
        print()

if __name__ == "__main__":
    board_size_x = 15
    board_size_y = 15
    cards = []

    assert Position(1, 1) == Position(1, 1), "Powinny być równe"
    assert Position(1, 1) != "cokolwiek", "Powinny być różne"
    assert Position(1, 1) in [Position(1, 1)]

    positions = []
    for _ in range(5):
        position = Position.random(board_size_x, board_size_y)
        if position in positions:
            continue
        positions.append(position)
        cards.append(Card(position))

    position = Position.random(board_size_x, board_size_y)

    
    print_board(cards, board_size_x, board_size_y)
