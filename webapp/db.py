from flask import g

cards = []

class DatabaseConnection:
    def get_cards(self):
        return cards
    
    def append_cards(self, new_cards):
        cards.extend(new_cards)

    def remove_card(self, card):
        cards.remove(card)


def get_db() -> DatabaseConnection:
    if "db" not in g:
        g.db = DatabaseConnection()
    return g.db
