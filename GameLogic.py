import Card
import Deck

Card = Card.Card
Deck = Deck.Deck

class GameLogic:
    def __init__(self):
        self.play_deck = Deck()
        self.discard_pile = []
        # TOdO: Get this hooked up with the GUI
        self.play_grid = []

        # TODO: Need to have GUI to finish this logic
        self.accrued_sets = []
        self.selected = []
        # TODO: Define play logic

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

        # TODO ? Add in the logic for if nothing matches?
        if selected_match_bools.count(True) == 3 and selected_set_bools.count(True) == 1:
            return True
        else:
            return False

    # TODO add play logic
    # Pseudo: when selected length == 3, immediately check set validity
    #   If is valid card set, add to accrued_sets as a tuple and refil the board. Show and alert of success
    #   Else empty out selected and deselect in gui. show an alert of failure

    # Provide a reset board button
    # Will probably not need a discard
    # What are the win/lose conditions?
    #   Win: TODO
    #   Lose: TODO
    # End game conditions?
    #   Add a I'm done button?
    # TODO: Add a number of possible sets left logic?