import numpy as np


class _SubPot(object):
    def __init__(self):
        self.bets = {}
        self.pot = 0
        self.max_bet = None

    def bet(self, player, amount):
        self.pot += amount
        try:
            self.bets[player] += amount
        except KeyError:
            self.bets[player] = amount

    def award(self, winners):
        award = self.pot // len(winners)
        for winner in winners:
            winner.award(award)
        # award remainders randomly to the winners
        for i in range(0, award % len(winners)):
            winners[np.random.randint(0, len(winners))].award(1)
            self.pot -= 1

    def create_side_pot(self, all_in_player):
        side_pot = _SubPot()
        self.max_bet = self.bets[all_in_player]
        new_bets = {player: self.bets[player] - self.max_bet for player in self.bets.keys()}
        for player, bet in self.bets.items():
            if new_bets[player] > 0:
                side_pot.bet(player, new_bets[player])
                self.bet(player, -1 * new_bets[player])
        return side_pot

    def copy(self):
        ret = _SubPot()
        ret.bets = self.bets.copy()
        ret.pot = self.pot
        ret.max_bet = self.max_bet
        return ret


class PokerPot(object):
    def __init__(self):
        self._subpots = []
        self._subpots.append(_SubPot())

    def bet(self, player, amount):
        for pot in self._subpots:
            if pot.max_bet is not None and pot.bets[player] < pot.max_bet:
                sub_amount = pot.max_bet - pot.bets[player]
                pot.bets[player] = pot.max_bet
                amount -= sub_amount
                if amount == 0:
                    return
        self._subpots[-1].bet(player, amount)

    def all_in(self, broke_player):
        self._subpots.append(self._subpots[-1].create_side_pot(broke_player))

    def award(self, winner_sets):
        for pot in self._subpots:
            betters = set(pot.bets.keys())
            for potentials in winner_sets:
                winners = betters & potentials
                if len(winners) > 0:
                    pot.award(list(winners))
                    break  # go to next subpot

    def winnable_pot(self, player):
        ret = 0
        for pot in self._subpots:
            if player in pot.bets.keys():
                ret += pot.pot
            else:
                break
        return ret

    def contribution(self, player):
        ret = 0
        for pot in self._subpots:
            try:
                ret += pot.bets[player]
            except KeyError:
                break
        return ret

    def copy(self):
        ret = PokerPot()
        for pot in self._subpots:
            ret._subpots.append(pot.copy())
        return ret
