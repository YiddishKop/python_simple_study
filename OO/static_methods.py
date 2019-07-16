"""
本节介绍类方法or静态方法
"""

class Board(object):

    _game_tiles = []

    def __init__(self, length, width):

        if not Board._game_tiles:
            for _ in range( length * width ):
                Board._game_tiles.append(Tile())

    @staticmethod
    def move_together(x_amount, y_amount):

        for tile in Board._game_tiles:
            tile.move(x_amount, y_amount)

    @staticmethod
    def print_locations():
        for tile in Board._game_tiles:
            print("tile.x:{x}; tile.y:{y}".format(x=tile.x, y=tile.y))

class Tile(object):
    
    def __init__(self):
        self.x=0
        self.y=0

    def move(self, x, y):
        self.x+=x
        self.y+=y


my_board1 = Board(4, 4)
Board.print_locations()
Board.move_together(10, 20)
Board.print_locations()
