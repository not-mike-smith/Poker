from TexasHoldemPlayer import TexasHoldemPlayer
from TexasHoldemTable import TexasHoldemTable


class ConsoleUi(object):
    def __init__(self):
        self.all_players = []
        self.table = None

    def play(self):
        keep_playing = self.create_players()
        if keep_playing:
            self.create_table()
        # TODO
        print(self.all_players)

    def create_players(self):
        name = None
        while name != '':
            if name is not None:
                player = TexasHoldemPlayer()
                player.name = name
                self.all_players.append(player)
            name = input('Enter player name to add player or nothing to move on: ')
            while name in self.all_players:
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
        ante = self.get_pos_int_from_user('Ante (not including blinds): ', 'ante')
        big_blind = self.get_pos_int_from_user('Big Blind: ', 'big blind')
        small_blind = big_blind // 2
        print('Small Blind will be defaulted to {0}.'.format(str(small_blind)))
        answer = input('To override value, enter \'Y\': ')
        if answer == 'Y' or answer == 'y':
            small_blind = self.get_pos_int_from_user('Small Blind: ', 'small blind')
        self.table = TexasHoldemTable(limit, self.all_players, ante, big_blind, small_blind)

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
