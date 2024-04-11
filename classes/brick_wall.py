from pygame import *
from classes.blockabc import Block
from abc import ABC
class BrickWall(Block):
    def __init__(self, x, y, filename, width, height):
        super().__init__(x, y, filename, width, height)
        self.num_hits = 0
    
    def hit(self):
        self.num_hits += 1
    
    