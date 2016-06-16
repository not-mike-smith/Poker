import itertools
from PokerHand import PokerHand
from PokerPlayer import PokerPlayer


class TexasHoldemPlayer(PokerPlayer):
    def __init__(self):
        super(TexasHoldemPlayer, self).__init__()

    def make_bet_action(self, allowed_actions):
        pass  # TODO: add Console UI here?

    @property
    def best_hand(self):
        if len(self.table.table_cards) + len(self._cards) < 5:
            return None
        hands = [PokerHand(list(card_set)) for card_set in itertools.combinations(
            self._cards + self.table.table_cards, 5)]
        # only look at hand_type, not card values
        hands.sort(key=lambda h: h.hand_type.value, reverse=True)
        # throw out hands of lower valued hand_type
        for i in range(len(hands)-1, 0, -1):
            if hands[i].hand_type != hands[0].hand_type:
                del hands[i]
        # Sort hands by face_value and return best
        hands.sort()
        return hands[-1]
