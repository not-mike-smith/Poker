from BetAction import BetAction
from PokerDecisionMaker import PokerDecisionMaker
from PokerGameSubscriber import PokerGameSubscriber
from TexasHoldemPlayer import TexasHoldemPlayer
from TexasHoldemTable import TexasHoldemTable


class ConsoleUi(PokerGameSubscriber, PokerDecisionMaker):
    def __init__(self):
        super().__init__()
        self.all_players = []
        self.table = None

    def play(self):
        keep_playing = self.create_players()
        if keep_playing:
            self.create_table()
            self.table.play()
        # TODO
        print(self.all_players)

    def create_players(self):
        name = None
        while name != '':
            if name is not None:
                player = TexasHoldemPlayer()
                player.name = name
                player.subscriber = self
                player.decision_maker = self
                self.all_players.append(player)
            name = input('Enter player name to add player or nothing to move on: ')
            while name in [player.name for player in self.all_players]:
                name = input('{0} is not a unique name. Enter new name: '.format(name))
        if len(self.all_players) < 2:
            print('Not enough players')
            return False
        for player in self.all_players:
            stack = self.get_pos_int_from_user('Initial stack size for {0}: '.format(player.name),
                                               'stack size')
            player.award(stack)
        return True

    def create_table(self):
        limit = self.get_pos_int_from_user('Bet Limit: ', 'bet limit')
        if limit == 0:
            limit = None
        ante = self.get_pos_int_from_user('Ante (not including blinds): ', 'ante')
        big_blind = self.get_pos_int_from_user('Big Blind: ', 'big blind')
        small_blind = big_blind // 2
        print('Small Blind will be defaulted to {0}.'.format(str(small_blind)))
        answer = input('To override value, enter \'Y\': ')
        if answer == 'Y' or answer == 'y':
            small_blind = self.get_pos_int_from_user('Small Blind: ', 'small blind')
        self.table = TexasHoldemTable(limit, self.all_players, ante, big_blind, small_blind)
        self.table.subscriber = self

    def player_pays(self, player, amount):
        verb = 'pays'
        if amount < 0:
            verb = 'wins'
            amount *= -1
        print('{0} {1} {2}, now has {3} chips'.format(player.name, verb, str(amount), player.stack))

    def players_win(self, table, players):
        for winner_set in players:
            msg = 'Tier: {'
            for winner in winner_set:
                msg += '{0} with {1}, '.format(winner.name, winner.best_hand)
            msg = msg[0:len(msg)-3]
            msg += '}'
            print(msg)

    def player_bets(self, player, bet_action, amount):
        msg = player.name
        if bet_action == BetAction.Fold:
            msg += ' folded'
        elif bet_action == BetAction.Call:
            msg += ' called'
        else:
            msg += ' raised {0}'.format(str(amount))
        print(msg)

    def player_took_cards(self, player, cards):
        print('{0} received {1}'.format(player.name, cards))

    def table_cards_updated(self, table):
        print('Cards on table are: {0}'.format(table.table_cards))

    def get_bet_action(self, player, allowed_actions, table):
        return BetAction.Call, None

    @staticmethod
    def get_pos_int_from_user(input_text, value_name):
        value = -1
        while value < 0:
            str_value = input(input_text)
            try:
                value = int(str_value)
            except ValueError:
                print('{0} is not a valid number for {1}'.format(str_value, value_name))
                value = -1
        return value
