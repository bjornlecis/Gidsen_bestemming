class Bestemming:
    def __init__(self,id,land,stad):
        self.id = id
        self.land = land
        self.stad = stad
    def wijzig_bestemming(self,land,stad):
        self.land = land
        self.stad = stad
    def toon_bestemming(self):
        return "Het land is {} en de stad is {}".format(self.land,self.stad)

class Gids:

    def __init__(self,id,naam,leeftijd,ervaring):
        self.id = id
        self.naam = naam
        self.leeftijd = leeftijd
        self.ervaring = ervaring
        self.tarief = 150
        self.bestemmingen = []

    def verander_gids_info(self,naam,leeftijd,ervaring):
        self.naam = naam
        self.leeftijd = leeftijd
        self.ervaring = ervaring
    def verander_naam(self,naam):
        self.naam = naam

    def verander_tarief(self,tarief):
        self.tarief = tarief
    def toon_gids_info(self):
        return "ID {} : De gids heet {} en is {} jaar oud en heeft {} jaar ervaring".format(self.id,self.naam,self.leeftijd,self.ervaring)
    def voeg_bestemming_toe(self,bestemming):
        self.bestemmingen.append(bestemming)
    def print_bestemmingen(self):
        for x in self.bestemmingen:
            print(x.toon_bestemming())

def toon_menu():
    print("Je kan kiezen uit.")
    print("1: Toon alle gidsen in de lijst")
    print("2: Toon gids Info")
    print("3: Verander de naam van de gids")
    print("4: Verander tarief van de gids")
    print("5: Verwijder gids")
    print("6: ken nieuwe bestemming toe aan gids")
    print("7: Verwijder de bestemming van de gids")
    print("8: Gids op basis van stad")


def toon_gidsen(lijst):
    print("Dit zijn alle gidsen en hun info")
    for x in lijst:
        print(x.toon_gids_info())

def toon_gids_info(lijst):
    gids_id = input("Geef het id van de gids")
    for x in lijst:
        if gids_id == x.id:
            print(x.toon_gids_info())
            x.print_bestemmingen()
def verander_naam_gids(lijst):
    gids_id = input("Geef het id van de gids")
    for x in lijst:
        if gids_id == x.id:
            nieuwe_naam = input("Geef een nieuwe naam voor de gids")
            x.verander_naam(nieuwe_naam)

def verander_tarief_gids(lijst):
    gids_id = input("Geef het id van de gids")
    for x in lijst:
        if gids_id == x.id:
            nieuw_tarief = input("Geef een nieuwe dagtarief voor de gids")
            x.verander_tarief(nieuw_tarief)
            print("Het nieuwe tarief is "+nieuw_tarief)

def verwijder_gids(lijst):
    id = input("van de gids die je wenst te verwijderen")
    for x,o in enumerate(lijst):
        if o.id == id:
            lijst.pop(x)

def ken_nieuwe_bestemming_toe_aan_gids(lijst):
    gids_id = input("Geef het id van de gids")
    for x in lijst:
        if gids_id == x.id:
            id = input("Geef het ID in")
            land = input("Geef het land in")
            stad = input("Geef de stad in")
            b = Bestemming(id,land,stad)
            x.voeg_bestemming_toe(b)

def verwijder_bestemming_van_een_gids(lijst):
    gids_id = input("Geef het id van de gids")
    for x in lijst:
        if gids_id == x.id:
            bestemming_id = input("Geef het ID van de bestemming")
            for y,o in enumerate (x.bestemmingen):
                if bestemming_id == o.id:
                    x.bestemmingen.pop(y)

def zoek_gids_voor_bestemming(lijst):
    stad = input("geef de naam van de stad")
    for x in lijst:
        for y in x.bestemmingen:
            if stad == y.stad:
                print(x.naam)




gidsen = []

b1 = Bestemming("I1","Italie","Rome")
b2 = Bestemming("I2","Italie","Milaan")
b3 = Bestemming("S1","Spanje","Madrid")
b4 = Bestemming("S2","Spanje","Barcelona")
g1 = Gids("G1","Dirk Jansen",42,16)
g1.voeg_bestemming_toe(b1)
g1.voeg_bestemming_toe(b2)

g2 = Gids("G2","An-Sofie Peters",38,14)
g2.voeg_bestemming_toe(b3)
g2.voeg_bestemming_toe(b4)

g3 = Gids("G3","Johan Jans",48,24)
g3.voeg_bestemming_toe(b1)

gidsen = [g1,g2,g3]


# hoofdprogramma
toon_menu()
keuze = input("geef je keuze in:")
while(not keuze == "stop"):
    if(keuze == "1"):
       toon_gidsen(gidsen)
    elif(keuze == "2"):
        toon_gids_info(gidsen)
    elif(keuze == "3"):
        verander_naam_gids(gidsen)
    elif(keuze == "4"):
        verander_tarief_gids(gidsen)
    elif(keuze == "5"):
        verwijder_gids(gidsen)
    elif(keuze == "6"):
        ken_nieuwe_bestemming_toe_aan_gids(gidsen)
    elif(keuze == "7"):
        verwijder_bestemming_van_een_gids(gidsen)
    elif(keuze == "8"):
        zoek_gids_voor_bestemming(gidsen)


    keuze = input("geef je keuze in:")






