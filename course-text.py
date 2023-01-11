class Track():
    def __init__(self,taille):
        self._taille=taille
    def addSpaceShip(self,Space_Ship):
        pass
    def startRace(self):
        pass
    def WhoWin(self):
        pass

class SpaceShip():
    def __init__(self,vitesse,nom):
        self._nom=nom
        self._vitesse=vitesse
    



track1=Track(2000)
SpaceShip1=SpaceShip(5,"SpaceS1")
SpaceShip2=SpaceShip(8,"SpaceS2")
SpaceShip3=SpaceShip(6,"SpaceS3")
SpaceShip4=SpaceShip(7,"SpaceS4")
SpaceShip5=SpaceShip(3,"SpaceS5")

track1.addSpaceShip(SpaceShip1)
track1.startRace()
print(track1.WhoWin())
