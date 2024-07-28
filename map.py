import pygame as pg

_ = False

mini_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, 1, 1, 1, 1, 1, _, _, 1, 1, _, 1, 1, _, 1],
    [1, _, _, _, _, _, 1, _, _, 1, 1, _, 1, 1, _, 1],
    [1, _, 1, 1, 1, 1, 1, _, _, 1, _, _, _, _, 1, 1],
    [1, _, 1, _, _, _, 1, _, _, 1, 1, 1, 1, 1, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()

    def get_map(self): # creates a dictionary of the map for easy access
        for y, row in enumerate(self.mini_map):
            for x, value in enumerate(row):
                if value:
                    self.world_map[(x, y)] = value
    
    def draw(self): # draws the map on the screen
        [pg.draw.rect(self.game.screen, 'red', (pos[0] * 100, pos[1] * 100, 100, 100), 2) 
         for pos in self.world_map]