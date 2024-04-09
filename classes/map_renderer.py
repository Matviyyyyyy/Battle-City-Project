from classes.brick_wall import BrickWall
from classes.iron_wall import IronWall
from classes.bush import Bush


class MapRenderer:
    def __init__(self, map_data, block_size):
        self.map_data = map_data
        self.block_size = block_size
        self.blocks = []
        self.current_x = 0
        self.current_y = 0

    # Функція для відображення карти
    def draw_map(self):
        with open(self.map_data, "r") as file:
            map = file.readlines()
            for line in map:
                for letter in line:
                    if letter == "W":
                        self.blocks.append(
                            BrickWall(self.current_x, self.current_y, "images/brick_wall_test.jpg", self.block_size,
                                      self.block_size))
                    elif letter == "I":
                        self.blocks.append(
                            IronWall(self.current_x, self.current_y, "images/iron_wall_test.jpg", self.block_size,
                                     self.block_size))
                    elif letter == "B":
                        self.blocks.append(Bush(self.current_x, self.current_y, "images/bush_test.jpg", self.block_size,
                                                self.block_size))
                    elif letter == "_":
                        self.current_x += self.block_size
                        continue  # Продовжуємо наступну ітерацію циклу без виконання подальшого коду
                    self.current_x += self.block_size

                self.current_y += self.block_size
                self.current_x = 0

    def destruction(self, obj):
        if isinstance(obj, BrickWall):
            if obj.num_hits >= 3:
                self.blocks.remove(obj)


