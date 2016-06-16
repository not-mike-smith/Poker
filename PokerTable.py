from Deck import Deck
from abc import abstractmethod
from PokerPot import PokerPot
from BetAction import BetAction


class PokerTable(object):
    def __init__(self, players, limit=None, ante=None):
        self._limit = limit
        self._betting_players = players
        for player in players:
            player.table = self
        self._unfolded_players = players.copy()
        self._ante = ante
        self._betting_player_index = 0
        self._pot = PokerPot()
        self._deck = Deck
        self._last_player_to_raise = None
        self._ante_up()
        self._max_bet = 0

    @property
    def limit(self):
        return self._limit

    @property
    def ante(self):
        return self._ante

    @property
    def first_player(self):
        return self._betting_players.peak()

    def copy_pot(self):
        return self._pot.copy()

    @property
    def max_bet(self):
        return self._max_bet

    def _ante_up(self):
        self._max_bet = self._ante
        for player in self._betting_players:
            self._collect_bet(player, self._ante)

    @abstractmethod
    def _deal(self):
        pass

    @abstractmethod
    def play(self):
        pass

    def _collect_bet(self, player, amount):
        all_in = False
        if player.stack <= amount:
            all_in = True
            amount = player.stack
        player.release_chips(amount)
        self._pot.bet(player, amount)
        if all_in:
            self._pot.all_in(player)
            self._betting_players.remove(player)
            # player can still win subpots because it is still in self._unfolded_players

    def betting_queue_position(self, player):
        return (self._betting_players.index(player) - self._betting_player_index) % len(self._betting_players)

    def sunk_bets(self, player):
        return self._pot.contribution(player)

    def cost_to_call(self, player):
        return self.max_bet - self._pot.contribution(player)

    @property
    def betting_player(self):
        return self._betting_players[self._betting_player_index]

    def winnable_pot(self, player):
        self._pot.winnable_pot(player)

    def _advance_betting_player(self):
        self._betting_player_index = (self._betting_player_index + 1) % len(self._betting_players)

    def do_bet_action(self, player, action_type, amount):
        if action_type == BetAction.Fold:
            self._betting_players.remove(player)
            self._unfolded_players.remove(player)
            self._betting_player_index %= len(self._betting_players)
            if self._last_player_to_raise is player:
                self._last_player_to_raise = self._betting_players[
                    (self._betting_player_index - 1) % len(self._betting_players)]
        elif action_type == BetAction.Call:
            self._collect_bet(player, self._max_bet - self._pot.contribution(player))
            self._advance_betting_player()
        elif action_type == BetAction.Raise:
            self._max_bet += amount
            self._last_player_to_raise = player
            self.do_bet_action(player, BetAction.Call, None)

    def _reset_betting_order(self):
        self._last_player_to_raise = self._betting_players[-1]
        self._betting_player_index = 0

    def _betting_round_and_continue(self):
        self._reset_betting_order()
        while len(self._betting_players) > 1 and self.betting_player is not self._last_player_to_raise:
            self.betting_player.make_bet_action([act for act in BetAction])
            self._advance_betting_player()
        if len(self._unfolded_players) == 1:
            self._pot.award({self._unfolded_players[0]})
            return False
        return True

    def _sort_hand_sets(self):
        winners = sorted(self._unfolded_players, key=lambda p: p.best_hand, reversed=True)
        ret = [{winners[0]}]  # list of sets
        hand = winners[0].best_hand
        ret_index = 0
        i = 1
        while i < len(winners):
            if winners[i].best_hand == hand:
                ret[ret_index].add(winners[i])
            else:
                ret.append({winners[i]})
                hand = winners[i].best_hand
                ret_index += 1
            i += 1
