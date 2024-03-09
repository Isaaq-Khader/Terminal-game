class Move:
    def __init__(self, name, atk, description = ""):
        self.name = name
        self.atk = atk
        self.description = description

class FighterAttributes:
    hp = 25
    def default_moves():
        move1 = Move("BASH", 4, "Bashes shield into enemy")
        move2 = Move("SLASH", 6, "Slashes enemy with shortsword")
        moves = move1 + move2
        return moves

class Fighter:
    def __init__(self):
        self.hp = FighterAttributes.hp
        self.moves = FighterAttributes.default_moves()

class Player:
    def __init__(self, name, style):
        self.name = name
        self.style = style

class Skeleton:
    def __init__(self, name = "Skeleton", hp = 20, atk = 4):
        self.name = name
        self.age = hp
        self.atk = atk

