import ComparisonLogic
import Deck

ComparisonLogic = ComparisonLogic.ComparisonLogic
Deck = Deck.Deck

class GameLogic:
    def __init__(self):
        self.play_deck = Deck()

        self.cards_in_play = []
        self.selected = []

        self.successful_set_pile = []
        # NOTE: keep for stats and fail count
        self.failed_set_pile = []

        self.game_count = 0
        self.game_status = 'new_game'

    def cards_in_play_count(self):
        return len(self.cards_in_play)
    def selected_count(self):
        return len(self.selected)
    def play_deck_count(self):
        return self.play_deck.getNumberOfCards()

    def draw_cards(self, draw_number):
        drawn_cards = []
        for i in range(0, draw_number):
            drawn_cards.append(self.play_deck.draw())

        return drawn_cards

    def successful_set_followup(self):
        cards_in_play_count = self.cards_in_play_count()
        play_deck_count = self.play_deck_count()
        selected_count = self.selected_count()

        if cards_in_play_count == 12 and play_deck_count >= selected_count:
            for removed_card in self.selected:
                i = self.cards_in_play.index(removed_card)
                self.cards_in_play[i] = self.play_deck.draw()
        elif cards_in_play_count == 12 and play_deck_count < selected_count:
            self.game_status = 'win'
        elif cards_in_play_count == 15:
            for removed_card in self.selected:
                self.cards_in_play.remove(removed_card)
        else:
            print('ERROR')
            raise Exception('Entered Impossible Game State!')

    def failed_set_followup(self):
        cards_in_play_count = self.cards_in_play_count()
        play_deck_count = self.play_deck_count()

        if cards_in_play_count == 12 and play_deck_count >= 3:
            drawn_cards = self.draw_cards(3)
            self.cards_in_play += drawn_cards
        elif cards_in_play_count == 12 and play_deck_count < 3:
            self.game_status = 'lose'
        elif cards_in_play_count == 15:
            self.game_status = 'lose'
        else:
            print('ERROR')
            raise Exception('Entered Impossible Game State!')

    def set_success_behavior(self, selected):
        self.successful_set_pile.append(selected)
        self.successful_set_followup()
        self.selected.clear()

    def set_failure_behavior(self, selected):
        self.failed_set_pile.append(selected)
        self.failed_set_followup()
        self.selected.clear()

    def apply_game_status(self):
        game_status = self.game_status
        if game_status == 'win':
                print('WINNER: You get a chicken dinner!'),
                self.new_game()
        elif game_status == 'lose':
                print('LOSER: major failure!'),
                self.new_game()
        else:
            print('CONTINUE')

    # TODO: remove win_test behavior!
    def new_game(self, draw_number = 12, win_test = False):
        self.failed_set_pile.clear()
        self.successful_set_pile.clear()
        self.selected.clear()

        self.play_deck = Deck()
        self.play_deck.shuffle()

        self.cards_in_play = self.draw_cards(draw_number)

        if win_test:
            print('TEST: WIN MODE')
            self.play_deck.cardList = []

        self.game_count += 1
        self.game_status = 'playing'
        print(f'NEW GAME #{self.game_count}')

    def check_selected_cards(self):
        selected = self.selected
        comparison_logic = ComparisonLogic(selected)

        if self.selected_count() == 3:
            if comparison_logic.is_a_card_set():
                self.set_success_behavior(selected)
                print('SUCCESS! Good Job')
            else:
                self.set_failure_behavior(selected)
                print('Failure! Be Better')

            self.apply_game_status()