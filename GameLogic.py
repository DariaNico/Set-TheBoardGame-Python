from functools import reduce
import Card
import Deck

Card = Card.Card
Deck = Deck.Deck

class GameLogic:
    def __init__(self):
        self.playDeck = Deck()
        self.discardPile = []
        # TODO: Get this hooked up with the GUI
        self.playGrid = []

        # TODO: Need to have GUI to finish this logic
        self.accruedSets = []
        self.selected = []
        # TODO: Define play logic

    @staticmethod
    def isMatch(selectedAttrs):
        reduce((lambda x, y: x == y), selectedAttrs)

    @staticmethod
    def isSet(selectedAttrs):
        len(set(selectedAttrs)) == 3

    def evaluateSelectedColors(self):
        selectedColors = list(map(lambda card: card.getColor(), self.selected))
        return { 'match': self.isMatch(selectedColors), 'set': self.isSet(selectedColors) }

    def evaluateSelectedFills(self):
        selectedFills = list(map(lambda card: card.getFill(), self.selected))
        return { 'match': self.isMatch(selectedFills), 'set': self.isSet(selectedFills) }

    def evaluateSelectedNumbers(self):
        selectedNumbers = list(map(lambda card: card.getNumber(), self.selected))
        return { 'match': self.isMatch(selectedNumbers), 'set': self.isSet(selectedNumbers) }

    def evaluateSelectedShapes(self):
        selectedShapes = list(map(lambda card: card.getShape(), self.selected))
        return { 'match': self.isMatch(selectedShapes), 'set': self.isSet(selectedShapes) }

    def isACardSet(self):
        evaluatedSelectedAttrs = { 'color': self.evaluateSelectedColors, 'fill': self.evaluateSelectedFills, 'number': self.evaluateSelectedNumbers, 'shape': self.evaluateSelectedShapes }
        selectedMatchBools = list(map(lambda x: x['match'], evaluatedSelectedAttrs.values()))
        selectedSetBools = list(map(lambda x: x['set'], evaluatedSelectedAttrs.values()))

        # TODO ? Add in the logic for if nothing matches?
        if selectedMatchBools.count(True) == 3 and selectedSetBools.count(True) == 1:
            return True
        else:
            return False

    # TODO add play logic
    # Pseudo: when selected length == 3, immediately check set validity
    #   If is valid card set, add to accruedSets as a tuple and refil the board. Show and alert of success
    #   Else empty out selected and deselect in gui. show an alert of failure

    # Provide a reset board button
    # Will probably not need a discard
    # What are the win/lose conditions?
    #   Win: TODO
    #   Lose: TODO
    # End game conditions?
    #   Add a I'm done button?
    # TODO: Add a number of possible sets left logic?