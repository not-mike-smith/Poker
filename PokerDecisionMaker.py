from abc import abstractmethod


class PokerDecisionMaker(object):
    def __init__(self):
        pass

    @abstractmethod
    def get_bet_action(self, player, allowed_actions, table):
        pass
