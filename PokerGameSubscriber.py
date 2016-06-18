from abc import abstractmethod


class PokerGameSubscriber(object):
    def __init__(self):
        pass

    @abstractmethod
    def player_pays(self, player, amount):
        pass

    @abstractmethod
    def player_bets(self, player, bet_action, amount):
        pass

    @abstractmethod
    def player_took_cards(self, player, cards):
        pass

    @abstractmethod
    def players_win(self, table, players):
        pass

    @abstractmethod
    def table_cards_updated(self, table):
        pass
