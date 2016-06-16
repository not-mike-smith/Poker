from enum import IntEnum
from _ComparableMixin import ComparableMixin


class HandType(IntEnum):
    HighCard = 0
    Pair = 1
    TwoPair = 2
    ThreeOfAKind = 3
    Straight = 4
    Flush = 5
    FullHouse = 6
    FourOfAKind = 7
    StraightFlush = 8


class PokerHand(ComparableMixin):
    def __init__(self, cards):
        self._cards = [card for card in cards]
        self._cards.sort()
        self._hand_type = None
        self._cards_to_compare = None
        self.tag = None

    @property
    def hand_type(self):
        if self._hand_type is None:
            self._hand_type = self._get_hand_type()
        return self._hand_type

    @property
    def cards(self):
        return self._cards

    @property
    def cards_to_compare(self):
        if self._cards_to_compare is None:
            self._cards_to_compare = self._get_cards_to_compare()
        return self._cards_to_compare

    def __repr__(self):
        return "(" + "{0}, {1}, {2}, {3}, {4}".format(self._cards[0],
                                                      self._cards[1],
                                                      self._cards[2],
                                                      self._cards[3],
                                                      self._cards[4]) + ")"

    def _get_hand_type(self):
        num_face_values = self._get_num_face_values()
        if num_face_values == 5:
            straight = self.is_straight()
            flush = self.is_flush()
            if not straight and not flush:
                return HandType.HighCard
            elif straight and not flush:
                return HandType.Straight
            elif not straight:
                return HandType.Flush
            else:
                return HandType.StraightFlush
        elif num_face_values == 4:
            return HandType.Pair
        elif num_face_values == 3:
            if not self.has_3_of_a_kind():
                return HandType.TwoPair
            return HandType.ThreeOfAKind
        if not self.has_4_of_a_kind():
            return HandType.FullHouse
        return HandType.FourOfAKind

    def _get_num_face_values(self):
        face_values = []
        for card in self._cards:
            if card.face_value not in face_values:
                face_values.append(card.face_value)
        return len(face_values)

    def is_flush(self):
        for card in self._cards[1:5]:
            if card.suit != self._cards[0].suit:
                return False
        return True

    def is_straight(self):
        for i in range(1, 5):
            if (self._cards[i].face_value.value - self._cards[i - 1].face_value.value) != 1:
                return False
        return True

    def has_3_of_a_kind(self):
        return self._cards[0].face_value == self._cards[2].face_value or \
               self._cards[2].face_value == self._cards[4].face_value or \
               self._cards[1].face_value == self._cards[3].face_value

    def has_4_of_a_kind(self):
        return self._cards[2].face_value == self._cards[1].face_value and \
               self._cards[2].face_value == self._cards[3].face_value

    def __lt__(self, other):
        if self.hand_type.value != other.hand_type.value:
            return self._hand_type.value < other.hand_type.value
        for i in range(0, len(self.cards_to_compare)):
            if self.cards_to_compare[i] != other.cards_to_compare[i]:
                return self.cards_to_compare[i] < other.cards_to_compare[i]
        return False  # because they are tied

    def __eq__(self, other):
        for i in range(0, 5):
            if self._cards[i].face_value.value != other.cards.face_value.value:
                return False
        return self.is_flush() == other.is_flush()

    def __ne__(self, other):
        return not (self == other)

    def _get_cards_to_compare(self):
        if self.hand_type == HandType.ThreeOfAKind or \
                        self.hand_type == HandType.Straight or \
                        self.hand_type == HandType.FullHouse or \
                        self.hand_type == HandType.FourOfAKind or \
                        self.hand_type == HandType.StraightFlush:
            return [self._cards[2]]
        elif self.hand_type == HandType.Flush or self.hand_type == HandType.HighCard:
            return [card for card in reversed(self._cards)]
        # else:
        singles = []
        doubles = []
        for i in range(3, -1, -1):
            if self._cards[-1].face_value == self._cards[i+1].face_value:
                doubles.append(self._cards[i])
            else:
                singles.append(self._cards[i+1])
        if self._cards[0].face_value == self._cards[1].face_value:
            singles.append(self._cards[0])
        return doubles + singles

    def __hash__(self):
        ret = hash(self._cards[0])
        for i in range(1, 5):
            ret ^= hash(self._cards[i])
        return ret
