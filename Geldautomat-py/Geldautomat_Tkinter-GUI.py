import tkinter as tk
from tkinter import messagebox
import os

class Geldautomat:
    def __init__(self, start_kontostand=0):
        self.__kontostand = self.lade_kontostand(start_kontostand)

    def einzahlung(self, betrag):
        if betrag > 0:
            self.__kontostand += betrag
            self.speichere_kontostand()
            return f"{betrag}€ eingezahlt. Neuer Kontostand: {self.__kontostand}€"
        else:
            return "Einzahlungsbetrag muss positiv sein."

    def auszahlung(self, betrag):
        if 0 < betrag <= self.__kontostand:
            self.__kontostand -= betrag
            self.speichere_kontostand()
            return f"{betrag}€ ausgezahlt. Neuer Kontostand: {self.__kontostand}€"
        else:
            return "Ungültiger Auszahlungsbetrag oder nicht genügend Guthaben."

    def get_kontostand(self):
        return self.__kontostand

    def speichere_kontostand(self):
        with open("kontostand.txt", "w") as file:
            file.write(str(self.__kontostand))

    def lade_kontostand(self, default=0):
        if os.path.exists("kontostand.txt"):
            try:
                with open("kontostand.txt", "r") as file:
                    return float(file.read().strip())
            except ValueError:
                return default
        return default


class GeldautomatGUI:
    def __init__(self, root):
        self.automat = Geldautomat(100)

        root.title("Geldautomat")
        root.geometry("350x300")
        root.protocol("WM_DELETE_WINDOW", self.beenden)

        self.kontostand_label = tk.Label(root, text=f"Kontostand: {self.automat.get_kontostand()}€", font=("Arial", 14))
        self.kontostand_label.pack(pady=10)

        self.betrag_entry = tk.Entry(root, font=("Arial", 12))
        self.betrag_entry.pack(pady=5)

        self.einzahlung_button = tk.Button(root, text="Einzahlen", command=self.einzahlen, font=("Arial", 12),
                                           bg="green", fg="white")
        self.einzahlung_button.pack(pady=5)

        self.auszahlung_button = tk.Button(root, text="Auszahlen", command=self.auszahlen, font=("Arial", 12), bg="red",
                                           fg="white")
        self.auszahlung_button.pack(pady=5)

        self.exit_button = tk.Button(root, text="Beenden", command=self.beenden, font=("Arial", 12), bg="gray", fg="white")
        self.exit_button.pack(pady=10)

    def einzahlen(self):
        try:
            betrag = float(self.betrag_entry.get())
            message = self.automat.einzahlung(betrag)
            self.update_kontostand()
        except ValueError:
            messagebox.showerror("Fehler", "Bitte eine gültige Zahl eingeben.")

    def auszahlen(self):
        try:
            betrag = float(self.betrag_entry.get())
            message = self.automat.auszahlung(betrag)
            self.update_kontostand()
        except ValueError:
            messagebox.showerror("Fehler", "Bitte eine gültige Zahl eingeben.")

    def update_kontostand(self):
        self.kontostand_label.config(text=f"Kontostand: {self.automat.get_kontostand()}€")

    def beenden(self):
        self.automat.speichere_kontostand()
        root.destroy()


root = tk.Tk()
app = GeldautomatGUI(root)
root.mainloop()
