import json

class SetStatistics:
    def __init__(self):
        self.all_game_stats = []
        self.total_wins = []
        self.total_losses = []
        self.total_resets = []

    def store_game(self, game_logic):
        game_stat = self.GameStat(
            game_id=game_logic.game_count,
            successful_sets=game_logic.successful_set_pile,
            failed_sets=game_logic.failed_set_pile,
            game_status=game_logic.game_status,
            penalty_states_entered=0
        )
        

    class GameStat:
        def __init__(self, game_id, successful_sets, failed_sets, game_status, penalty_states_entered):
            self.game_id = game_id
            self.successful_sets = successful_sets
            self.failed_sets = failed_sets
            self.game_status = game_status
            self.penalty_states_entered = penalty_states_entered
