import math
from random import randint

class SimplePulseBehaviour:
    def __init__(self, insect):
        self.insect = insect
        self.c = 0
        self.cycleLength = randint(60,200)
        self.initIntensity = self.insect.getIntensity()

    def doBehave(self):
        scale = math.sin(math.pi / self.cycleLength * (self.c % self.cycleLength))
        self.insect.setIntensity(self.initIntensity * scale * 0.2)
        self.c += 1
