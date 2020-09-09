import json

class SetStatistics:
    def __init__(self):
        self.all_game_stats = {
            'win': [],
            'lose': [],
            'reset': []
        }

    def store_game(self, game_logic):
        game_stat = self.GameStat(game_logic)
        self.all_game_stats[game_stat.game_result].append(game_stat)

    class GameStat:
        def get_game_result(self):
            game_status = self.game_logic_attrs['game_status']
            if game_status == 'win' or game_status == 'lose':
                return game_status
            else:
                return 'reset'

        def __init__(self, game_logic):
            self.game_logic_attrs = vars(game_logic)
            self.game_id = game_logic.game_count
            self.successful_sets = game_logic.successful_set_pile
            self.failed_sets = game_logic.failed_set_pile
            self.game_result = self.get_game_result()
            self.penalty_states_entered = 0 # TODO: need to implement this still

