class ComparisonLogic:
    def __init__(self, selected):
        self.selected = selected

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

    def evaluate_selected_colors(self, selected = []):
        selected_colors = list(map(lambda card: card.getColor(), selected))
        return { 'match': self.is_match(selected_colors), 'set': self.is_set(selected_colors) }

    def evaluate_selected_fills(self, selected = []):
        selected_fills = list(map(lambda card: card.getFill(), selected))
        return { 'match': self.is_match(selected_fills), 'set': self.is_set(selected_fills) }

    def evaluate_selected_numbers(self, selected = []):
        selected_numbers = list(map(lambda card: card.getNumber(), selected))
        return { 'match': self.is_match(selected_numbers), 'set': self.is_set(selected_numbers) }

    def evaluate_selected_shapes(self, selected = []):
        selected_shapes = list(map(lambda card: card.getShape(), selected))
        return { 'match': self.is_match(selected_shapes), 'set': self.is_set(selected_shapes) }

    def is_a_card_set(self, selected = []):
        evaluated_selected_attrs = {
            'color': self.evaluate_selected_colors(selected),
            'fill': self.evaluate_selected_fills(selected),
            'number': self.evaluate_selected_numbers(selected),
            'shape': self.evaluate_selected_shapes(selected)
        }
        selected_match_bools = []
        selected_set_bools = []

        for selected_attr_bools in evaluated_selected_attrs.values():
            selected_match_bools.append(selected_attr_bools['match'])
            selected_set_bools.append(selected_attr_bools['set'])

        if selected_match_bools.count(True) + selected_set_bools.count(True) == 4:
            return True
        else:
            return False
