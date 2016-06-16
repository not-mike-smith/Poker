from unittest import TestCase
from PokerHand import PokerHand, HandType
from PlayingCard import PlayingCard, Suit, FaceValue


class TestPokerHand(TestCase):
    def __init__(self, methodName='runTest'):
        super(TestPokerHand, self).__init__(methodName=methodName)
        self._all_ties = None

    def test__get_hand_type(self):
        for hand in self.straight_flushes:
            if hand.hand_type != HandType.StraightFlush:
                self.fail('straight flush ({0}) called {1}'.format(hand, hand.hand_type.name))
        for hand in self.four_of_a_kinds:
            if hand.hand_type != HandType.FourOfAKind:
                self.fail('4 of a kind ({0}) called {1}'.format(hand, hand.hand_type.name))
        for hand in self.full_houses:
            if hand.hand_type != HandType.FullHouse:
                self.fail('full house ({0}) called {1}'.format(hand, hand.hand_type.name))
        for hand in self.straights:
            if hand.hand_type != HandType.Straight:
                self.fail('straight ({0}) called {1}'.format(hand, hand.hand_type.name))
        for hand in self.flushes:
            if hand.hand_type != HandType.Flush:
                self.fail('flush ({0}) called {1}'.format(hand, hand.hand_type.name))
        for hand in self.three_of_a_kinds:
            if hand.hand_type != HandType.ThreeOfAKind:
                self.fail('triple ({0}) called {1}'.format(hand, hand.hand_type.name))
        for hand in self.two_pairs:
            if hand.hand_type != HandType.TwoPair:
                self.fail('two pair ({0}) called {1}'.format(hand, hand.hand_type.name))
        for hand in self.pairs:
            if hand.hand_type != HandType.Pair:
                self.fail('pair ({0}) called {1}'.format(hand, hand.hand_type.name))
        for hand in self.high_cards:
            if hand.hand_type != HandType.HighCard:
                self.fail('high ({0}) called {1}'.format(hand, hand.hand_type.name))

    @property
    def all_hands(self):
        ret = self.straight_flushes
        ret.extend(self.four_of_a_kinds)
        ret.extend(self.full_houses)
        ret.extend(self.flushes)
        ret.extend(self.straights)
        ret.extend(self.three_of_a_kinds)
        ret.extend(self.two_pairs)
        ret.extend(self.pairs)
        ret.extend(self.high_cards)
        return ret

    @property
    def all_ties(self):
        if self._all_ties is None:
            self._all_ties = {self.royal_flush_hearts: self.royal_flush_spades,
                              self.six_high_straight2: self.six_high_straigt,
                              self.flush_s_A7532: self.flush_h_A7532,
                              self.tens_9s_8v2: self.tens_9s_8,
                              self.fives_J_9_6v2: self.fives_J_9_6,
                              self.ace_K_Q_J_8v2: self.ace_K_Q_J_8}
        return self._all_ties

    @property
    def straight_flushes(self):
        return [self.royal_flush_spades,
                self.royal_flush_hearts,
                self.king_high_straight_flush]

    @property
    def royal_flush_spades(self):
        return PokerHand([PlayingCard(Suit.Spades, FaceValue.Ace),
                          PlayingCard(Suit.Spades, FaceValue.King),
                          PlayingCard(Suit.Spades, FaceValue.Queen),
                          PlayingCard(Suit.Spades, FaceValue.Jack),
                          PlayingCard(Suit.Spades, FaceValue.Ten)])

    @property
    def royal_flush_hearts(self):
        return PokerHand([PlayingCard(Suit.Hearts, FaceValue.Ace),
                          PlayingCard(Suit.Hearts, FaceValue.King),
                          PlayingCard(Suit.Hearts, FaceValue.Queen),
                          PlayingCard(Suit.Hearts, FaceValue.Jack),
                          PlayingCard(Suit.Hearts, FaceValue.Ten)])

    @property
    def king_high_straight_flush(self):
        return PokerHand([PlayingCard(Suit.Diamonds, FaceValue.King),
                          PlayingCard(Suit.Diamonds, FaceValue.Queen),
                          PlayingCard(Suit.Diamonds, FaceValue.Jack),
                          PlayingCard(Suit.Diamonds, FaceValue.Ten),
                          PlayingCard(Suit.Diamonds, FaceValue.Nine)])

    @property
    def four_of_a_kinds(self):
        return [self.four_8s_3,
                self.four_4s_9]

    @property
    def four_8s_3(self):
        return PokerHand([PlayingCard(Suit.Spades, FaceValue.Eight),
                          PlayingCard(Suit.Diamonds, FaceValue.Eight),
                          PlayingCard(Suit.Clubs, FaceValue.Eight),
                          PlayingCard(Suit.Hearts, FaceValue.Eight),
                          PlayingCard(Suit.Diamonds, FaceValue.Tre)])

    @property
    def four_4s_9(self):
        return PokerHand([PlayingCard(Suit.Spades, FaceValue.Four),
                          PlayingCard(Suit.Diamonds, FaceValue.Four),
                          PlayingCard(Suit.Clubs, FaceValue.Four),
                          PlayingCard(Suit.Hearts, FaceValue.Four),
                          PlayingCard(Suit.Spades, FaceValue.Nine)])

    @property
    def full_houses(self):
        return [self.eights_full_of_2s,
                self.sevens_full_of_aces]

    @property
    def sevens_full_of_aces(self):
        return PokerHand([PlayingCard(Suit.Spades, FaceValue.Seven),
                          PlayingCard(Suit.Diamonds, FaceValue.Seven),
                          PlayingCard(Suit.Clubs, FaceValue.Seven),
                          PlayingCard(Suit.Clubs, FaceValue.Ace),
                          PlayingCard(Suit.Diamonds, FaceValue.Ace)])

    @property
    def eights_full_of_2s(self):
        return PokerHand([PlayingCard(Suit.Spades, FaceValue.Eight),
                          PlayingCard(Suit.Diamonds, FaceValue.Eight),
                          PlayingCard(Suit.Clubs, FaceValue.Eight),
                          PlayingCard(Suit.Spades, FaceValue.Deuce),
                          PlayingCard(Suit.Diamonds, FaceValue.Deuce)])

    @property
    def straights(self):
        return [self.ace_high_straight,
                self.six_high_straigt,
                self.six_high_straight2]

    @property
    def ace_high_straight(self):
        return PokerHand([PlayingCard(Suit.Diamonds, FaceValue.Ace),
                          PlayingCard(Suit.Hearts, FaceValue.King),
                          PlayingCard(Suit.Hearts, FaceValue.Queen),
                          PlayingCard(Suit.Hearts, FaceValue.Jack),
                          PlayingCard(Suit.Hearts, FaceValue.Ten)])

    @property
    def six_high_straigt(self):
        return PokerHand([PlayingCard(Suit.Spades, FaceValue.Six),
                          PlayingCard(Suit.Diamonds, FaceValue.Five),
                          PlayingCard(Suit.Clubs, FaceValue.Four),
                          PlayingCard(Suit.Diamonds, FaceValue.Tre),
                          PlayingCard(Suit.Diamonds, FaceValue.Deuce)])

    @property
    def six_high_straight2(self):
        return PokerHand([PlayingCard(Suit.Clubs, FaceValue.Six),
                          PlayingCard(Suit.Hearts, FaceValue.Five),
                          PlayingCard(Suit.Spades, FaceValue.Four),
                          PlayingCard(Suit.Hearts, FaceValue.Tre),
                          PlayingCard(Suit.Hearts, FaceValue.Deuce)])

    @property
    def flushes(self):
        return [self.flush_s_A7532,
                self.flush_h_A7532,
                self.flush_h_KQJ98]

    @property
    def flush_h_KQJ98(self):
        return PokerHand([PlayingCard(Suit.Hearts, FaceValue.King),
                          PlayingCard(Suit.Hearts, FaceValue.Queen),
                          PlayingCard(Suit.Hearts, FaceValue.Jack),
                          PlayingCard(Suit.Hearts, FaceValue.Nine),
                          PlayingCard(Suit.Hearts, FaceValue.Eight)])

    @property
    def flush_h_A7532(self):
        return PokerHand([PlayingCard(Suit.Hearts, FaceValue.Ace),
                          PlayingCard(Suit.Hearts, FaceValue.Seven),
                          PlayingCard(Suit.Hearts, FaceValue.Five),
                          PlayingCard(Suit.Hearts, FaceValue.Tre),
                          PlayingCard(Suit.Hearts, FaceValue.Deuce)])

    @property
    def flush_s_A7532(self):
        return PokerHand([PlayingCard(Suit.Spades, FaceValue.Ace),
                          PlayingCard(Suit.Spades, FaceValue.Seven),
                          PlayingCard(Suit.Spades, FaceValue.Five),
                          PlayingCard(Suit.Spades, FaceValue.Tre),
                          PlayingCard(Suit.Spades, FaceValue.Deuce)])

    @property
    def three_of_a_kinds(self):
        return [self.three_Ks_QJ,
                self.three_2s_AK]

    @property
    def three_Ks_QJ(self):
        return PokerHand([PlayingCard(Suit.Spades, FaceValue.King),
                          PlayingCard(Suit.Diamonds, FaceValue.King),
                          PlayingCard(Suit.Clubs, FaceValue.King),
                          PlayingCard(Suit.Spades, FaceValue.Queen),
                          PlayingCard(Suit.Spades, FaceValue.Jack)])

    @property
    def three_2s_AK(self):
        return PokerHand([PlayingCard(Suit.Spades, FaceValue.Tre),
                          PlayingCard(Suit.Diamonds, FaceValue.Tre),
                          PlayingCard(Suit.Clubs, FaceValue.Tre),
                          PlayingCard(Suit.Spades, FaceValue.Ace),
                          PlayingCard(Suit.Hearts, FaceValue.King)])

    @property
    def two_pairs(self):
        return [self.aces_2s_K,
                self.aces_2s_3,
                self.Ks_Qs_J,
                self.tens_9s_8,
                self.tens_9s_8v2,
                self.fours_3s_K]

    @property
    def aces_2s_K(self):
        return PokerHand([PlayingCard(Suit.Spades, FaceValue.Ace),
                          PlayingCard(Suit.Diamonds, FaceValue.Ace),
                          PlayingCard(Suit.Spades, FaceValue.Deuce),
                          PlayingCard(Suit.Diamonds, FaceValue.Deuce),
                          PlayingCard(Suit.Spades, FaceValue.King)])

    @property
    def aces_2s_3(self):
        return PokerHand([PlayingCard(Suit.Clubs, FaceValue.Ace),
                          PlayingCard(Suit.Hearts, FaceValue.Ace),
                          PlayingCard(Suit.Clubs, FaceValue.Deuce),
                          PlayingCard(Suit.Hearts, FaceValue.Deuce),
                          PlayingCard(Suit.Spades, FaceValue.Tre)])

    @property
    def Ks_Qs_J(self):
        return PokerHand([PlayingCard(Suit.Diamonds, FaceValue.King),
                          PlayingCard(Suit.Clubs, FaceValue.King),
                          PlayingCard(Suit.Spades, FaceValue.Queen),
                          PlayingCard(Suit.Diamonds, FaceValue.Queen),
                          PlayingCard(Suit.Spades, FaceValue.Jack)])

    @property
    def tens_9s_8(self):
        return PokerHand([PlayingCard(Suit.Spades, FaceValue.Ten),
                          PlayingCard(Suit.Diamonds, FaceValue.Ten),
                          PlayingCard(Suit.Spades, FaceValue.Nine),
                          PlayingCard(Suit.Diamonds, FaceValue.Nine),
                          PlayingCard(Suit.Spades, FaceValue.Eight)])

    @property
    def tens_9s_8v2(self):
        return PokerHand([PlayingCard(Suit.Clubs, FaceValue.Ten),
                          PlayingCard(Suit.Hearts, FaceValue.Ten),
                          PlayingCard(Suit.Clubs, FaceValue.Nine),
                          PlayingCard(Suit.Hearts, FaceValue.Nine),
                          PlayingCard(Suit.Diamonds, FaceValue.Eight)])

    @property
    def fours_3s_K(self):
        return PokerHand([PlayingCard(Suit.Spades, FaceValue.Four),
                          PlayingCard(Suit.Diamonds, FaceValue.Four),
                          PlayingCard(Suit.Diamonds, FaceValue.Tre),
                          PlayingCard(Suit.Clubs, FaceValue.Tre),
                          PlayingCard(Suit.Hearts, FaceValue.King)])

    @property
    def pairs(self):
        return [self.aces_K_Q_J,
                self.aces_4_3_2,
                self.tens_K_3_2,
                self.tens_8_7_6,
                self.fives_J_9_6,
                self.fives_J_9_6v2,
                self.twos_K_Q_J]

    @property
    def aces_K_Q_J(self):
        return PokerHand([PlayingCard(Suit.Spades, FaceValue.Ace),
                          PlayingCard(Suit.Diamonds, FaceValue.Ace),
                          PlayingCard(Suit.Spades, FaceValue.King),
                          PlayingCard(Suit.Spades, FaceValue.Queen),
                          PlayingCard(Suit.Spades, FaceValue.Jack)])

    @property
    def aces_4_3_2(self):
        return PokerHand([PlayingCard(Suit.Clubs, FaceValue.Ace),
                          PlayingCard(Suit.Hearts, FaceValue.Ace),
                          PlayingCard(Suit.Spades, FaceValue.Four),
                          PlayingCard(Suit.Spades, FaceValue.Tre),
                          PlayingCard(Suit.Spades, FaceValue.Deuce)])

    @property
    def tens_K_3_2(self):
        return PokerHand([PlayingCard(Suit.Spades, FaceValue.Ten),
                          PlayingCard(Suit.Diamonds, FaceValue.Ten),
                          PlayingCard(Suit.Diamonds, FaceValue.King),
                          PlayingCard(Suit.Diamonds, FaceValue.Tre),
                          PlayingCard(Suit.Diamonds, FaceValue.Deuce)])

    @property
    def tens_8_7_6(self):
        return PokerHand([PlayingCard(Suit.Clubs, FaceValue.Ten),
                          PlayingCard(Suit.Hearts, FaceValue.Ten),
                          PlayingCard(Suit.Spades, FaceValue.Eight),
                          PlayingCard(Suit.Spades, FaceValue.Seven),
                          PlayingCard(Suit.Spades, FaceValue.Six)])

    @property
    def fives_J_9_6v2(self):
        return PokerHand([PlayingCard(Suit.Clubs, FaceValue.Five),
                          PlayingCard(Suit.Hearts, FaceValue.Five),
                          PlayingCard(Suit.Clubs, FaceValue.Jack),
                          PlayingCard(Suit.Diamonds, FaceValue.Nine),
                          PlayingCard(Suit.Clubs, FaceValue.Six)])

    @property
    def fives_J_9_6(self):
        return PokerHand([PlayingCard(Suit.Spades, FaceValue.Five),
                          PlayingCard(Suit.Diamonds, FaceValue.Five),
                          PlayingCard(Suit.Diamonds, FaceValue.Jack),
                          PlayingCard(Suit.Spades, FaceValue.Nine),
                          PlayingCard(Suit.Diamonds, FaceValue.Six)])

    @property
    def twos_K_Q_J(self):
        return PokerHand([PlayingCard(Suit.Clubs, FaceValue.Deuce),
                          PlayingCard(Suit.Hearts, FaceValue.Deuce),
                          PlayingCard(Suit.Clubs, FaceValue.King),
                          PlayingCard(Suit.Diamonds, FaceValue.Queen),
                          PlayingCard(Suit.Hearts, FaceValue.Jack)])

    @property
    def high_cards(self):
        return [self.ace_k_q_j_9,
                self.ace_K_Q_J_8,
                self.ace_K_Q_J_8v2,
                self.seven_5_4_3_2]

    @property
    def ace_k_q_j_9(self):
        return PokerHand([PlayingCard(Suit.Spades, FaceValue.Ace),
                          PlayingCard(Suit.Diamonds, FaceValue.King),
                          PlayingCard(Suit.Spades, FaceValue.Queen),
                          PlayingCard(Suit.Spades, FaceValue.Jack),
                          PlayingCard(Suit.Spades, FaceValue.Nine)])

    @property
    def ace_K_Q_J_8(self):
        return PokerHand([PlayingCard(Suit.Diamonds, FaceValue.Ace),
                          PlayingCard(Suit.Spades, FaceValue.King),
                          PlayingCard(Suit.Diamonds, FaceValue.Queen),
                          PlayingCard(Suit.Diamonds, FaceValue.Jack),
                          PlayingCard(Suit.Spades, FaceValue.Eight)])

    @property
    def ace_K_Q_J_8v2(self):
        return PokerHand([PlayingCard(Suit.Clubs, FaceValue.Ace),
                          PlayingCard(Suit.Hearts, FaceValue.King),
                          PlayingCard(Suit.Clubs, FaceValue.Queen),
                          PlayingCard(Suit.Clubs, FaceValue.Jack),
                          PlayingCard(Suit.Clubs, FaceValue.Eight)])

    @property
    def seven_5_4_3_2(self):
        return PokerHand([PlayingCard(Suit.Spades, FaceValue.Seven),
                          PlayingCard(Suit.Spades, FaceValue.Five),
                          PlayingCard(Suit.Diamonds, FaceValue.Four),
                          PlayingCard(Suit.Spades, FaceValue.Tre),
                          PlayingCard(Suit.Spades, FaceValue.Deuce)])
