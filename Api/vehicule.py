class vehicule:

    totalVehicule = 0

    def __init__(self, id:"int", type:["bateau", "voiture", "moto", "avion"], nom:"str", marque:"str", vitesseMax:"int", km:"float"):
        self.id = id    ### pour retrouver le véhicule par rapport à son id
        self.type = type
        self.nom = nom
        self.marque = marque
        self.vitesseMax = vitesseMax
        self.km = km


class bateau(vehicule):
    def __init__(self, voile:"bool", type:"bateau"):
        self.voile = voile
        self.type = type


class voiture(vehicule):
    def __init__(self, cabriole:"bool", type:"voiture"):
        self.cabriole = cabriole
        self.type = type

class moto(vehicule):
    def __init__(self, sporster:"bool", roadster:"bool", type:"moto"):
        self.sporster = sporster
        self.roadster = roadster
        self.type = type

class avion(vehicule):
    def __init__(self, voyage:"bool", type:"avion"):
        self.voyage = voyage
        self.type = type


if __name__ == "__main__":
    bateau = bateau()
    voiture = voiture()
    moto = moto()
    avion = avion()
