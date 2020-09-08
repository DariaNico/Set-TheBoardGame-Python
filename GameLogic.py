import ComparisonLogic
import Deck

ComparisonLogic = ComparisonLogic.ComparisonLogic
Deck = Deck.Deck

class GameLogic:
    def __init__(self):
        self.play_deck = Deck()
        self.play_deck.shuffle()

        self.cards_in_play = []
        self.selected = []

        self.successful_set_pile = []
        # NOTE: keep for stats and fail count
        self.failed_set_pile = []

        self.game_count = 0
        self.game_status = 'new_game'

    def cards_in_play_count(self):
        return len(self.cards_in_play)

    def draw_cards(self, draw_number):
        drawn_cards = []
        for i in range(0, draw_number):
            drawn_cards.append(self.play_deck.draw())

        return drawn_cards

    def start_game(self, draw_number = 12):
        self.cards_in_play = self.draw_cards(draw_number)
        self.game_count += 1
        self.game_status = 'playing'

    def replace_cards(self):
        cards_in_play_count = self.cards_in_play_count()

        if cards_in_play_count == 12:
            for removed_card in self.selected:
                i = self.cards_in_play.index(removed_card)
                self.cards_in_play[i] = self.play_deck.draw()
        elif cards_in_play_count == 15:
            for removed_card in self.selected:
                self.cards_in_play.remove(removed_card)
        else:
            raise Exception(f'Wrong number of cards on board: expected 12 or 15, instead got {cards_in_play_count}.')

    def set_success(self, selected):
        self.successful_set_pile.append(selected)
        self.replace_cards()
        self.selected.clear()

    def set_failure(self, selected):
        self.failed_set_pile.append(selected)
        self.selected.clear()

    def check_selected_cards(self):
        selected = self.selected
        comparison_logic = ComparisonLogic(selected)

        if len(selected) == 3:
            if comparison_logic.is_a_card_set():
                self.set_success(selected)
                self.apply_game_status()
                print("SUCCESS")
            else:
                self.set_failure(selected)
                self.apply_game_status()
                print("FAILURE")

    def apply_game_status(self):
        game_status = self.game_status
        if game_status == 'win':
                print('WIN'),
        elif game_status == 'lose':
                print('LOSER'),
        else:
            print('CONTINUE')