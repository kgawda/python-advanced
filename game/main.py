import time
from models import Card, Position, Hero, Enemy


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
    print("".join(c.summary() for c in cards))

if __name__ == "__main__":
    board_size_x = 15
    board_size_y = 15
    cards = []

    assert Position(1, 1) == Position(1, 1), "Powinny być równe"
    assert Position(1, 1) != "cokolwiek", "Powinny być różne"
    assert Position(1, 1) in [Position(1, 1)]

    # Rozstawiamy na planszy
    positions = []
    for _ in range(5):
        position = Position.random(board_size_x, board_size_y)
        if position in positions:
            continue
        positions.append(position)
        cards.append(Enemy(position=position, live=10, attack=5))

    position = Position.random(board_size_x, board_size_y)
    hero = Hero(position=position, name="Henryk", attack=90)
    cards.append(hero)
    
    # Gramy
    print_board(cards, board_size_x, board_size_y)
    while True:
        for card in cards:
            card.do_movement()
            card.lmit_to_board(board_size_x, board_size_y)

            for other in cards:
                if (card.position == other.position) and (other != card):
                    card.interact_with(other, card_remover=cards.remove)

        print_board(cards, board_size_x, board_size_y)
        time.sleep(0.1)
