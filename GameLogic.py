import Deck

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

    @staticmethod
    def is_match(selected_attrs):
        previous_attr = selected_attrs[0]
        for attr in selected_attrs:
            if previous_attr != attr:
                return False
        return True

    @staticmethod
    def is_set(selected_attrs):
        return len(set(selected_attrs)) == 3

    def evaluate_selected_colors(self):
        selected_colors = list(map(lambda card: card.getColor(), self.selected))
        return { 'match': self.is_match(selected_colors), 'set': self.is_set(selected_colors) }

    def evaluate_selected_fills(self):
        selected_fills = list(map(lambda card: card.getFill(), self.selected))
        return { 'match': self.is_match(selected_fills), 'set': self.is_set(selected_fills) }

    def evaluate_selected_numbers(self):
        selected_numbers = list(map(lambda card: card.getNumber(), self.selected))
        return { 'match': self.is_match(selected_numbers), 'set': self.is_set(selected_numbers) }

    def evaluate_selected_shapes(self):
        selected_shapes = list(map(lambda card: card.getShape(), self.selected))
        return { 'match': self.is_match(selected_shapes), 'set': self.is_set(selected_shapes) }

    def is_a_card_set(self):
        evaluated_selected_attrs = { 'color': self.evaluate_selected_colors(), 'fill': self.evaluate_selected_fills(), 'number': self.evaluate_selected_numbers(), 'shape': self.evaluate_selected_shapes() }
        selected_match_bools = []
        selected_set_bools = []

        for selected_attr_bools in evaluated_selected_attrs.values():
            selected_match_bools.append(selected_attr_bools['match'])
            selected_set_bools.append(selected_attr_bools['set'])

        if selected_match_bools.count(True) + selected_set_bools.count(True) == 4:
            return True
        else:
            return False

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

    def set_success(self):
        self.successful_set_pile.append(self.selected)
        self.replace_cards()
        self.selected.clear()

    def set_failure(self):
        self.failed_set_pile.append(self.selected)
        self.selected.clear()

    def check_selected_cards(self):
        if len(self.selected) == 3:
            if self.is_a_card_set():
                self.set_success()
                print("SUCCESS")
            else:
                self.set_failure()
                print("FAILURE")