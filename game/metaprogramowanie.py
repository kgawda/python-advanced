class Token(int):
  def __new__(cls, s):
   return int.__new__(cls, {'up': 1, 'down': -1}.get(s, 0))

card_types = []
class Card:
    def __init_subclass__(cls):
        card_types.append(cls)

class Creature(Card):
   pass

class Hero(Creature):
   pass

print(card_types)

