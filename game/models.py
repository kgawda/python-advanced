import random
from typing import Self

class Position:
    x: int
    y: int
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
    
    @classmethod
    def random(cls, board_size_x: int, board_size_y: int) -> Self:
        x = random.randrange(board_size_x)
        y = random.randrange(board_size_y)
        return cls(x, y)
    
    def __eq__(self, value) -> bool:
        if not isinstance(value, Position):
            return False
        return (self.x == value.x) and (self.y == value.y)
    
    # # dzięki __hash__ możemy dodać do set()
    # # ale musimy wtedy zadbać żeby x i y były niezmienne
    # def __hash__(self):
    #     return hash((self.x, self.y))


class Card:
    position: Position
    def __init__(self, *, position: Position):
        self.position = position
        # self.position = Position(x, y)

    def get_symbol(self) -> str:
        return "X"

class Creature(Card):
    live: int
    attack: int
    def __init__(self, *, live=100, attack=10, **kwargs):
        self.live = live
        self.attack = attack
        super().__init__(**kwargs)

    def get_symbol(self) -> str:
        return "C"

class Hero(Creature):
    name: str
    def __init__(self, *, name: str, **kwargs) -> None:
        self.name = name
        super().__init__(**kwargs)
    
    def get_symbol(self) -> str:
        return self.name[0]
    
class Enemy(Creature):
    def get_symbol(self) -> str:
        return "E"