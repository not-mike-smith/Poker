from PokerTable import PokerTable
from BetAction import BetAction


class NoLimitHoldemTable(PokerTable):
    def __init__(self, limit=None, players=None, ante=None, big_blind=0, small_blind=None):
        super(NoLimitHoldemTable, self).__init__(limit, players, ante)
        self._big_blind = big_blind
        if small_blind is None:
            small_blind = big_blind // 2
        self._small_blind = small_blind
        self._table_cards = []

    @property
    def small_blind(self):
        return self._small_blind

    @property
    def big_blind(self):
        return self._big_blind

    @property
    def table_cards(self):
        return self._table_cards.copy()

    def _ante_up(self):
        super(NoLimitHoldemTable, self)._ante_up()
        self._collect_bet(self._betting_players[-2], self._small_blind)
        self._collect_bet(self._betting_players[-1], self._big_blind)
        self._max_bet += self._big_blind

    def _deal(self):
        for player in self._betting_players:
            player.take_cards(self._deck.multi_deal(2))

    def play(self):
        for player in self._betting_players:
            player.make_bet_action([act for act in BetAction])  # TODO: fix this
        if self._last_player_to_raise is self._betting_players[-1]:
            for player in self._betting_players:
                player.make_bet_action([BetAction.Fold, BetAction.Call])
        self._deck.deal()
        self._table_cards.extend(self._deck.multi_deal(3))
        if not self._betting_round_and_continue():
            return
        self._deck.deal()
        self._table_cards.append(self._deck.deal())
        if not self._betting_round_and_continue():
            return
        self._deck.deal()
        self._table_cards.append(self._deck.deal())
        if not self._betting_round_and_continue():
            return
        winning_sets = self._sort_hand_sets()
        self._pot.award(winning_sets)
