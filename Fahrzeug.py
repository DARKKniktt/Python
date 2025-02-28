# Basisklasse Fahrzeug (Vererbung, Verkapselung)
class Fahrzeug:
    def __init__(self, marke, modell):
        self.__marke = marke  # Verkapselung: private Variable
        self.__modell = modell  # Verkapselung: private Variable

    def get_info(self):
        return f"Marke: {self.__marke}, Modell: {self.__modell}"

    def fahren(self):
        raise NotImplementedError("Diese Methode muss in der abgeleiteten Klasse implementiert werden.")


# Abgeleitete Klasse Auto (Polymorphie)
class Auto(Fahrzeug):
    def __init__(self, marke, modell, türanzahl):
        super().__init__(marke, modell)  # Aufruf des Konstruktors der Basisklasse
        self.türanzahl = türanzahl

    def fahren(self):
        return f"Das Auto {self.get_info()} fährt mit {self.türanzahl} Türen."


# Abgeleitete Klasse Motorrad (Polymorphie)
class Motorrad(Fahrzeug):
    def __init__(self, marke, modell, ps):
        super().__init__(marke, modell)  # Aufruf des Konstruktors der Basisklasse
        self.ps = ps

    def fahren(self):
        return f"Das Motorrad {self.get_info()} fährt mit {self.ps} PS."


# Operatorüberladung: Beispiel für die Addition von Fahrzeugen (Design Pattern - Strategy)
class FahrzeugAddition:
    def __add__(self, other):
        if isinstance(other, Fahrzeug):
            return f"Zusammenführung von Fahrzeugen: {other.get_info()}"
        return "Kann nicht addiert werden."


# Instanziierung der Klassen
auto1 = Auto("Toyota", "Corolla", 4)
motorrad1 = Motorrad("Harley", "Sportster", 120)

# Anwendung von Vererbung und Polymorphie
print(auto1.fahren())  # Polymorphie: Auto fährt
print(motorrad1.fahren())  # Polymorphie: Motorrad fährt

# Beispiel für Operatorüberladung
addition = FahrzeugAddition()
print(addition + auto1)