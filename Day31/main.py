import tkinter as tk
from tkinter import PhotoImage, Button
import pandas as pd
import random

# -----------------------------UI---------------------------------

BACKGROUND_COLOR = "#B1DDC6"

# Erstelle das Hauptfenster
window = tk.Tk()
window.title("Flashcard project")
window.geometry("900x726")
window.config(bg=BACKGROUND_COLOR)

# Erstelle einen Canvas mit der Größe 800x526
canvas = tk.Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2, padx=50, pady=(50, 0))

# Lade die Bilder
front_image = PhotoImage(file=r"C:\Users\TimPr\100-Days-Python-Code-2\Day31\images\card_front.png")
back_image = PhotoImage(file=r"C:\Users\TimPr\100-Days-Python-Code-2\Day31\images\card_back.png")
right_image = PhotoImage(file=r"C:\Users\TimPr\100-Days-Python-Code-2\Day31\images\right.png")
wrong_image = PhotoImage(file=r"C:\Users\TimPr\100-Days-Python-Code-2\Day31\images\wrong.png")

canvas_image = canvas.create_image(400, 263, image=front_image)  # Bild in der Mitte (400, 263)
canvas_word_text = canvas.create_text(400, 263, text="", font=("Arial", 30, "bold"), fill="black")
canvas_language_text = canvas.create_text(400, 150, text="", font=("Arial", 15, "italic"), fill="black")

# Erstelle Buttons für die beiden unteren Bilder
right_button = Button(window, image=right_image, highlightthickness=0)
wrong_button = Button(window, image=wrong_image, highlightthickness=0)

right_button.grid(row=1, column=0, padx=(50, 0), pady=10)
wrong_button.grid(row=1, column=1, padx=(0, 50), pady=10)

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

# -----------------------------Data Loading---------------------------------

# Definiere den Pfad zur CSV-Datei
csv_file_path = r"C:\Users\TimPr\100-Days-Python-Code-2\Day31\data\french_words.csv"

# Lese die CSV-Datei ein
data = pd.read_csv(csv_file_path)

# Füge eine 'Rank'-Spalte hinzu, falls sie noch nicht existiert
if 'Rank' not in data.columns:
    data['Rank'] = 1  # Initialisiere alle Wörter mit dem Rang 1

to_learn = data.to_dict(orient="records")  # Liste von Wörterpaaren als Dicts
current_word = {}

# -----------------------------Functions---------------------------------

# Funktion, um ein zufälliges Wort anhand von Gewichten (Ränge) auszuwählen
def pick_random_word():
    global current_word
    if to_learn:  # Falls es noch Wörter zum Lernen gibt
        # Berechne die Wahrscheinlichkeiten basierend auf den Rängen (je niedriger der Rang, desto wahrscheinlicher)
        weights = [1 / word['Rank'] for word in to_learn]
        current_word = random.choices(to_learn, weights=weights, k=1)[0]
        # Aktualisiere das Bild und den Text
        canvas.itemconfig(canvas_image, image=front_image)
        canvas.itemconfig(canvas_word_text, text=current_word['French'], fill="black")
        canvas.itemconfig(canvas_language_text, text="French", fill="black")
        # Karte nach 3 Sekunden umdrehen
        window.after(3000, flip_card)
    else:
        canvas.itemconfig(canvas_word_text, text="All words learned!", fill="black")

# Funktion, um die Karte umzudrehen und die englische Übersetzung zu zeigen
def flip_card():
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(canvas_word_text, text=current_word['English'], fill="white")
    canvas.itemconfig(canvas_language_text, text="English", fill="white")

# Funktion für den rechten Button (Wort gelernt)
def on_right_click():
    global to_learn, current_word
    if current_word in to_learn:
        # Erhöhe den Rang des aktuellen Wortes
        current_word['Rank'] += 1
        # Speichere die aktualisierte Liste der Wörter
        pd.DataFrame(to_learn).to_csv("words_to_learn.csv", index=False)
    pick_random_word()  # Zeige das nächste Wort an

# Funktion für den falschen Button (Wort noch nicht gelernt)
def on_wrong_click():
    pick_random_word()  # Zeige das nächste Wort an

# Füge die Funktionen zu den Buttons hinzu
right_button.config(command=on_right_click)
wrong_button.config(command=on_wrong_click)

# -----------------------------Start---------------------------------
pick_random_word()  # Starte mit einem zufälligen Wort
window.mainloop()
