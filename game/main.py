import io
import sys
import time
from typing import Iterable

from .models import Card, Position, Hero, Enemy

def iter_cards_at(cards: list[Card], x:int, y:int) -> Iterable[Card]:
    for card in cards:
        if card.position.x == x and card.position.y == y:
            yield card

def print_board(cards, board_size_x, board_size_y, print_target):
    for y in range(board_size_y):
        for x in range(board_size_x):
            for card in iter_cards_at(cards, x, y):
                print(card.get_symbol() + " ", end="", file=print_target)
                break
            else:  # po pętli for, jeśli nie było break
                print(". ", end="", file=print_target)
        print(file=print_target)
    print("".join(c.summary() for c in cards), file=print_target)


def prepare_cards(board_size_x, board_size_y, n_enemies, n_heroes):
    cards = []
    positions = []
    for _ in range(n_enemies):
        position = Position.random(board_size_x, board_size_y)
        if position in positions:
            continue
        positions.append(position)
        cards.append(Enemy(position=position, live=10, attack=5))

    for _ in range(n_heroes):
        position = Position.random(board_size_x, board_size_y)
        hero = Hero(position=position, name="Henryk", attack=90)
        cards.append(hero)
    
    return cards


def run_turn(board_size_x, board_size_y, cards, min_cards, print_target, sleep_time) -> int:
    new_cards = 0
    if print_target:
        print_board(cards, board_size_x, board_size_y, print_target)
    for card in cards:
        card.do_movement()
        card.lmit_to_board(board_size_x, board_size_y)

        for other in cards:
            if (card.position == other.position) and (other != card) and (card in cards):
                # TODO: change `card in cards` to faster solution
                card.interact_with(other, card_remover=cards.remove)

    if len(cards) < min_cards:
        # TODO: add more cards if more than 1 missing
        position = Position.random(board_size_x, board_size_y)
        cards.append(Enemy(position=position, live=10, attack=5))
        new_cards += 1
    
    if sleep_time:
        time.sleep(sleep_time)

    return new_cards


def simulate() -> int:
    board_size_x = 15
    board_size_y = 15
    new_cards_counter = 0
    cards = prepare_cards(board_size_x, board_size_y, 5, 0)
    print_buffer = io.StringIO()
    for _ in range(10_000):
        new_cards_counter += run_turn(board_size_x, board_size_y, cards, min_cards=5, print_target=print_buffer, sleep_time=0)
    return new_cards_counter

def interactive_game():
    board_size_x = 15
    board_size_y = 15
    
    assert Position(1, 1) == Position(1, 1), "Powinny być równe"
    assert Position(1, 1) != "cokolwiek", "Powinny być różne"
    assert Position(1, 1) in [Position(1, 1)]

    # Rozstawiamy na planszy
    cards = prepare_cards(board_size_x, board_size_y, 5, 1)
    
    # Gramy
    while True:
        run_turn(board_size_x, board_size_y, cards, min_cards=4, print_target=sys.stdout, sleep_time=0.1) 

if __name__ == "__main__":
    new_cards_counter = simulate()
    print(new_cards_counter)