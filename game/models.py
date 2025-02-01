import random
from typing import Self
from abc import ABC, abstractmethod

from getchar import getchar_arrow


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

    def copy_moved(self, delta: Self) -> Self:
        return Position(self.x + delta.x, self.y + delta.y)
    
    def limited_to(self, board_size_x: int, board_size_y: int) -> Self:
        new_x = max(0, self.x)
        new_x = min(new_x, board_size_x - 1)
        new_y = max(0, self.y)
        new_y = min(new_y, board_size_y - 1)
        return Position(new_x, new_y)
    
    @staticmethod
    def get_from_key_name(key_name):
        if key_name == "up":
            return Position(0, -1)
        elif key_name == "down":
            return Position(0, 1)
        elif key_name == "left":
            return Position(-1, 0)
        elif key_name == "right":
            return Position(1, 0)
        else:
            return Position(0, 0)


class Card(ABC):
    position: Position
    def __init__(self, *, position: Position):
        self.position = position
        # self.position = Position(x, y)

    @abstractmethod
    def get_symbol(self) -> str:
        ...
    
    def do_movement(self) -> None:
        "Modifies slef.position"
        pass

    def lmit_to_board(self, board_size_x: int, board_size_y: int) -> None:
        "Modifies self.position"
        self.position = self.position.limited_to(board_size_x, board_size_y)

    def interact_with(self, other, card_remover):
        pass

    def summary(self) -> str:
        return ""

class Creature(Card):
    live: int
    attack: int
    def __init__(self, *, live=100, attack=10, **kwargs):
        self.live = live
        self.attack = attack
        super().__init__(**kwargs)

    def get_symbol(self) -> str:
        return "C"
    
    def interact_with(self, other, card_remover):
        if not isinstance(other, Creature):
            return
        self.live = self.live - other.attack
        other.live = other.live - self.attack
        if other.live <= 0:
            card_remover(other)
        if self.live <= 0:
            card_remover(self)

class Hero(Creature):
    name: str
    def __init__(self, *, name: str, **kwargs) -> None:
        self.name = name
        super().__init__(**kwargs)
    
    def get_symbol(self) -> str:
        return self.name[0]

    def do_movement(self) -> None:
        key_pressed = getchar_arrow()
        delta = Position.get_from_key_name(key_pressed)
        self.position = self.position.copy_moved(delta)

    def summary(self) -> str:
        return f"[{self.name} {self.live}]"


class Enemy(Creature):
    def get_symbol(self) -> str:
        return "E"
    
    def do_movement(self) -> None:
        delta = Position(random.randint(-1,1), random.randint(-1,1))
        self.position = self.position.copy_moved(delta)
