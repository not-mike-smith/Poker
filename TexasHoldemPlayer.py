import itertools

from PokerHand import PokerHand
from PokerPlayer import PokerPlayer


class TexasHoldemPlayer(PokerPlayer):
    def __init__(self):
        super(TexasHoldemPlayer, self).__init__()

    def make_bet_action(self, allowed_actions):
        if self.decision_maker is None:
            return
        bet_action, amount = self.decision_maker.get_bet_action(self, allowed_actions, self.table)
        if self.subscriber is not None:
            self.subscriber.player_bets(self, bet_action, amount)
        self.table.do_bet_action(self, bet_action, amount)

    @property
    def best_hand(self):
        if len(self.table.table_cards) + len(self._cards) < 5:
            return None
        hands = [PokerHand(list(card_set)) for card_set in itertools.combinations(
            self._cards + self.table.table_cards, 5)]
        # only look at hand_type, not card values
        hands.sort(key=lambda h: h.hand_type.value, reverse=True)
        # throw out hands of lower valued hand_type
        contenders = []
        for hand in hands:
            if hand.hand_type == hands[0].hand_type:
                contenders.append(hand)
            else:
                break
        # Sort hands by face_value and return best
        contenders.sort()
        return contenders[-1]
