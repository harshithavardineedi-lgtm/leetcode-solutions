import random
import math

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> list[float]:
        angle = random.uniform(0, 2 * math.pi)
        distance = self.r * math.sqrt(random.random())

        x = self.x + distance * math.cos(angle)
        y = self.y + distance * math.sin(angle)

        return [x, y]