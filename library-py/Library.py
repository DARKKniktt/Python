import tkinter as tk
from tkinter import messagebox
import os


class Verlag:
    def __init__(self, name, ort):
        self.__name = name
        self.__ort = ort

    def get_info(self):
        return f"Verlag: {self.__name}, Ort: {self.__ort}"


class Buch(Verlag):
    def __init__(self, titel, author, name, ort):
        super().__init__(name, ort)
        self.titel = titel
        self.author = author

    def veröffentlichen(self):
        return f"{self.get_info()} veröffentlichte das Buch '{self.titel}' von {self.author}"


def buch_speichern(buch_info):
    with open("buecher.txt", "a", encoding="utf-8") as file:
        file.write(buch_info + "\n")


def lade_buecher():
    buch_liste.delete(0, tk.END)
    if os.path.exists("buecher.txt"):
        with open("buecher.txt", "r", encoding="utf-8") as file:
            for line in file:
                buch_liste.insert(tk.END, line.strip())


def buch_veröffentlichen():
    verlag_name = verlag_entry.get()
    ort = ort_entry.get()
    titel = titel_entry.get()
    autor = autor_entry.get()

    if not (verlag_name and ort and titel and autor):
        messagebox.showerror("Fehler", "Bitte alle Felder ausfüllen!")
        return

    buch = Buch(titel, autor, verlag_name, ort)
    buch_info = buch.veröffentlichen()

    buch_speichern(buch_info)
    buch_liste.insert(tk.END, buch_info)

    verlag_entry.delete(0, tk.END)
    ort_entry.delete(0, tk.END)
    titel_entry.delete(0, tk.END)
    autor_entry.delete(0, tk.END)


def buch_löschen():
    try:
        selected_index = buch_liste.curselection()[0]
        selected_text = buch_liste.get(selected_index)

        buch_liste.delete(selected_index)

        with open("buecher.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
        with open("buecher.txt", "w", encoding="utf-8") as file:
            for line in lines:
                if line.strip() != selected_text:
                    file.write(line)

        messagebox.showinfo("Erfolg", "Buch wurde gelöscht!")

    except IndexError:
        messagebox.showwarning("Fehler", "Bitte wähle ein Buch zum Löschen aus!")


root = tk.Tk()
root.title("Buchverlag GUI")
root.geometry("500x400")

main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

input_frame = tk.Frame(main_frame)
input_frame.pack(fill=tk.X, pady=5)

tk.Label(input_frame, text="Verlag:").grid(row=0, column=0, sticky="w", padx=5, pady=2)
verlag_entry = tk.Entry(input_frame)
verlag_entry.grid(row=0, column=1, padx=5, pady=2)

tk.Label(input_frame, text="Ort:").grid(row=1, column=0, sticky="w", padx=5, pady=2)
ort_entry = tk.Entry(input_frame)
ort_entry.grid(row=1, column=1, padx=5, pady=2)

tk.Label(input_frame, text="Buchtitel:").grid(row=0, column=2, sticky="w", padx=5, pady=2)
titel_entry = tk.Entry(input_frame)
titel_entry.grid(row=0, column=3, padx=5, pady=2)

tk.Label(input_frame, text="Autor:").grid(row=1, column=2, sticky="w", padx=5, pady=2)
autor_entry = tk.Entry(input_frame)
autor_entry.grid(row=1, column=3, padx=5, pady=2)

button_frame = tk.Frame(main_frame)
button_frame.pack(pady=5)

veröffentlichen_button = tk.Button(button_frame, text="Buch veröffentlichen", command=buch_veröffentlichen, fg="white", bg="green")
veröffentlichen_button.pack(side=tk.LEFT, padx=10)

löschen_button = tk.Button(button_frame, text="Buch löschen", command=buch_löschen, fg="white", bg="red")
löschen_button.pack(side=tk.LEFT, padx=10)

tk.Label(main_frame, text="Gespeicherte Bücher:").pack()

listbox_frame = tk.Frame(main_frame)
listbox_frame.pack(fill=tk.BOTH, expand=True)

buch_liste = tk.Listbox(listbox_frame, width=70, height=8)
buch_liste.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(listbox_frame, orient=tk.VERTICAL, command=buch_liste.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
buch_liste.config(yscrollcommand=scrollbar.set)

lade_buecher()

root.mainloop()
