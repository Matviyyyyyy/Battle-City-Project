from pygame import *
from classes.blockabc import Block
from abc import ABC
class Bush(Block):
    def __init__(self, x, y, filename, width, height):
        super().__init__(x, y, filename, width, height)
