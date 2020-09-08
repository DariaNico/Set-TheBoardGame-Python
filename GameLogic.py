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

    def draw_cards(self, draw_number):
        drawn_cards = []
        for i in range(0, draw_number):
            drawn_cards.append(self.play_deck.draw())

        return drawn_cards

    def start_game(self, draw_number):
        self.cards_in_play = self.draw_cards(draw_number)

    def replace_cards(self):
        drawn_cards = self.draw_cards(len(self.selected))
        
        for removed_card in self.selected:
            i = self.cards_in_play.index(removed_card)
            self.cards_in_play[i] = drawn_cards.pop()

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
            if comparison_logic.is_a_card_set(selected):
                self.set_success(selected)
                print("SUCCESS")
            else:
                self.set_failure(selected)
                print("FAILURE")