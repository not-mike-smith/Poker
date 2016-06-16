from PokerHand import HandType, PokerHand
from PlayingCard import Suit, FaceValue, PlayingCard
import itertools

cards = [PlayingCard(Suit.Spades, FaceValue.Deuce), PlayingCard(Suit.Diamonds, FaceValue.Tre),
         PlayingCard(Suit.Clubs, FaceValue.Four), PlayingCard(Suit.Hearts, FaceValue.Five),
         PlayingCard(Suit.Spades, FaceValue.Six), PlayingCard(Suit.Diamonds, FaceValue.Six),
         PlayingCard(Suit.Clubs, FaceValue.Seven)]
x = itertools.combinations(cards, 5)
for item in x:
    print(list(item))
