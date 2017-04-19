class Insect:

    def __init__(self):
        self.behaviour = None
        self.intensity = 1.0

    def paint(self):
        raise NotImplementedError("")

    def behave(self):
        self.behaviour.doBehave() 

    def setIntensity(self, intensity):
        self.intensity = intensity

    def getIntensity(self):
        return self.intensity

    def setBehaviour(self, behaviour):
        self.behaviour = behaviour
        
