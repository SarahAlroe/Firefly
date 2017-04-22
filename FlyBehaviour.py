import math
from random import randint

class FireFlyBehaviour:
    def __init__(self, insect):
        self.insect = insect
        self.c = 0
        self.cycleLength = randint(5,50)
        self.initIntensity = self.insect.getIntensity()

    def doBehave(self):
        if self.c <= self.cycleLength:
            scale = math.sin(math.pi / self.cycleLength * self.c)
            self.insect.setIntensity(self.initIntensity * scale * 0.2)
            self.c += 1
        else:
            self.insect.setIntensity(0)
            if randint(1,100) == 1:
                self.c = 0

