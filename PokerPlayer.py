from abc import abstractmethod

from BetAction import BetAction


# abstract class
class PokerPlayer(object):
    def __init__(self):
        self.name = ''
        self._cards = []
        self._stack = 0
        self.table = None
        self.subscriber = None
        self.decision_maker = None

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
        if self.subscriber is not None:
            self.subscriber.player_took_cards(self, cards)

    def award(self, amount):
        self._stack += amount
        if self.subscriber is not None:
            self.subscriber.player_pays(self, -1*amount)

    def release_chips(self, amount):
        self._stack -= amount
        if self.subscriber is not None:
            self.subscriber.player_pays(self, amount)

    @abstractmethod
    def make_bet_action(self, allowed_actions):
        pass

    def _fold(self):
        self.table.do_bet_action(BetAction.Fold)
        if self.subscriber is not None:
            self.subscriber.player_bets(self, BetAction.Fold, None)

    def _call(self):
        self.table.do_bet_action(BetAction.Call)
        if self.subscriber is not None:
            self.subscriber.player_bets(self, BetAction.Call, None)

    def _raise(self, amount):
        self.table.do_bet_action(BetAction.Raise, amount)
        if self.subscriber is not None:
            self.subscriber.player_bets(BetAction.Raise, amount)
