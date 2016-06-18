from abc import abstractmethod
from BetAction import BetAction


class PokerPlayer(object):
    def __init__(self):
        self.name = ''
        self._cards = []
        self._stack = 0
        self.table = None

    def __repr__(self):
        return self.name + ' has ' + str(self._stack) + ' chips'

    @property
    def best_hand(self):
        raise Exception('Must be overridden')

    @property
    def stack(self):
        return self._stack

    def take_cards(self, cards):
        self._cards.extend(cards)

    def award(self, amount):
        self._stack += amount

    def release_chips(self, amount):
        self._stack -= amount

    @abstractmethod
    def make_bet_action(self, allowed_actions):
        pass

    def _fold(self):
        self.table.do_bet_action(BetAction.Fold)

    def _call(self):
        self.table.do_bet_action(BetAction.Call)

    def _raise(self, amount):
        self.table.do_bet_action(BetAction.Raise, amount)
