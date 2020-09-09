import json

class SetStatistics:
    def __init__(self):
        self.all_game_stats = {
            'win': [],
            'lose': [],
            'reset': []
        }

    def win_count(self):
        return len(self.all_game_stats['win'])

    def lose_count(self):
        return len(self.all_game_stats['lose'])

    def reset_count(self):
        return len(self.all_game_stats['reset'])

    def total_game_count(self):
        return self.win_count() + self.lose_count() + self.reset_count()

    def store_game(self, game_logic):
        game_stat = self.GameStat(game_logic)
        game_result = game_stat.game_result

        if game_result:
            self.all_game_stats[game_result].append(game_stat)

        # TODO: Remove this print line
        print(f'STORED: game_id: {game_logic.game_count},\n wins: {self.win_count()},\n losses: {self.lose_count()},\n resets: {self.reset_count()}')

    class GameStat:
        def get_game_result(self):
            game_status = self.game_logic_attrs['game_status']
            if game_status == 'win' or game_status == 'lose':
                return game_status
            elif game_status == 'new_game':
                return None
            else:
                return 'reset'

        def __init__(self, game_logic):
            self.game_logic_attrs = vars(game_logic)
            self.game_id = game_logic.game_count
            self.successful_sets = game_logic.successful_set_pile
            self.failed_sets = game_logic.failed_set_pile
            self.game_result = self.get_game_result()
            self.penalty_states_entered = 0 # TODO: need to implement this still

