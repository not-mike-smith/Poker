from enum import IntEnum


class Suit(IntEnum):
    Hearts = 0
    Clubs = 1
    Diamonds = 2
    Spades = 3


class FaceValue(IntEnum):
    Deuce = 0
    Tre = 1
    Four = 2
    Five = 3
    Six = 4
    Seven = 5
    Eight = 6
    Nine = 7
    Ten = 8
    Jack = 9
    Queen = 10
    King = 11
    Ace = 12


class PlayingCard(object):
    def __init__(self, suit, face_value):
        self._suit = suit
        self._face_value = face_value
        self._rank = None

    @property
    def suit(self):
        return self._suit

    @property
    def face_value(self):
        return self._face_value

    @property
    def rank(self):
        if self._rank is None:
            self._rank = self._get_rank(self)
        return self._rank

    def __repr__(self):
        return self._get_card_char(self._face_value) + "." + self._suit.name[0]

    def __lt__(self, other):
        return self.rank < other.rank

    def __eq__(self, other):
        return self._face_value == other.face_value and self._suit == other.suit

    def __hash__(self):
        return self.rank

    @staticmethod
    def _get_rank(card):
        return card.face_value.value*4 + card.suit.value

    @staticmethod
    def _get_card_char(face_value):
        if face_value.value <= 8:
            return str(face_value.value + 2)
        return face_value.name[0]
