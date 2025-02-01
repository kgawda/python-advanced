###### __new__

class Token(int):
  def __new__(cls, s):
   return int.__new__(cls, {'up': 1, 'down': -1}.get(s, 0))



###### __init_subclass__

card_types = []
class Card:
    def __init_subclass__(cls):
        card_types.append(cls)

class Creature(Card):
   pass

class Hero(Creature):
   pass

print(card_types)



###### metaclass

class Meta(type):
    def __new__(cls, name, bases, dct):
        new_cls = super().__new__(cls, name, bases, dct)
        # new_cls jest nową klasą (np. MyClass tworzoną poniżej), którą możemy w tym miejscu modyfikować 
        # A czym jest cls? To po prostu akutalna Meta, na wypadek gdybyśmy jej potrzebowali
        return new_cls

class MyClass(metaclass=Meta):
    pass
