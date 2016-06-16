from PlayingCard import Suit, FaceValue, PlayingCard
import numpy as np


class Deck(object):
    def __init__(self):
        self._available_cards = [i for i in range(0, 52)]
        self._dealt_cards = []

    def deal(self):
        if len(self._available_cards) == 0:
            raise StopIteration("Out of cards")
        mask_index = np.random.randint(0, len(self._available_cards))
        card_index = self._available_cards[mask_index]
        self._dealt_cards.append(card_index)
        del self._available_cards[mask_index]
        return self.cards[card_index]

    def multi_deal(self, num):
        return [self.deal() for i in range(0, num)]

    def collect_and_shuffle(self):
        self._available_cards = [i for i in range(0, 52)]
        self._dealt_cards = []

    def __len__(self):
        return len(self._available_cards)

    _cards = None

    @property
    def cards(self):
        if Deck._cards is None:
            Deck._cards = []
            for face_value in FaceValue:
                for suit in Suit:
                    Deck._cards.append(PlayingCard(suit, face_value))
        return Deck._cards
