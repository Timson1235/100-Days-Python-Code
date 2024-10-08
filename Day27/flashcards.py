import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
import csv
import random

# Flashcard class definition
class Flashcard:
    def __init__(self, question, answer, status='Apprentice'):
        self.question = question
        self.answer = answer
        self.status = status

# Flashcard system
class FlashcardSystem:
    def __init__(self):
        self.flashcards = []
        self.status_weights = {
            'Apprentice': 5,
            'Guru': 4,
            'Master': 3,
            'Enlightened': 2,
            'Burned': 1
        }
        self.status_order = ['Apprentice', 'Guru', 'Master', 'Enlightened', 'Burned']

    def add_card(self, question, answer):
        card = Flashcard(question.strip(), answer.strip())
        self.flashcards.append(card)

    def edit_card(self, question, new_answer):
        card = self._find_card(question)
        if card:
            card.answer = new_answer.strip()
            card.status = 'Apprentice'

    def delete_card(self, question):
        card = self._find_card(question)
        if card:
            self.flashcards.remove(card)

    def view_cards(self):
        return self.flashcards

    def study_cards(self, num_cards):
        if not self.flashcards:
            return []

        study_list = self._select_cards_to_study(num_cards)
        return study_list

    def _find_card(self, question):
        for card in self.flashcards:
            if card.question == question:
                return card
        return None

    def _select_cards_to_study(self, num_cards):
        weighted_flashcards = [
            card for card in self.flashcards
            for _ in range(self.status_weights[card.status])
        ]
        random.shuffle(weighted_flashcards)
        selected_cards = list({card: None for card in weighted_flashcards}.keys())
        return selected_cards[:min(num_cards, len(selected_cards))]

    def _promote_card(self, card):
        current_index = self.status_order.index(card.status)
        if current_index < len(self.status_order) - 1:
            card.status = self.status_order[current_index + 1]

    def _demote_card(self, card):
        current_index = self.status_order.index(card.status)
        if current_index > 0:
            card.status = self.status_order[current_index - 1]

    def upload_dictionary(self, file_path):
        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    if len(row) >= 2:
                        question, answer = row[:2]
                        card = Flashcard(question.strip(), answer.strip())
                        self.flashcards.append(card)
        except Exception as e:
            print(f"An error occurred: {e}")

# GUI Implementation
class FlashcardApp:
    def __init__(self, root, system):
        self.system = system
        self.root = root
        self.root.title("Flashcard System")

        self.main_frame = tk.Frame(root)
        self.main_frame.pack(pady=20)

        self.create_buttons()
        self.text_area = tk.Text(root, width=100, height=20)
        self.text_area.pack(pady=20)

    def create_buttons(self):
        button_texts = ["Add Card", "Edit Card", "Delete Card", "View Cards", "Study Cards", "Upload Dictionary"]
        button_commands = [self.add_card, self.edit_card, self.delete_card, self.view_cards, self.study_cards, self.upload_dictionary]

        for i, (text, command) in enumerate(zip(button_texts, button_commands)):
            button = tk.Button(self.main_frame, text=text, command=command)
            button.grid(row=0, column=i, padx=10)

    def add_card(self):
        question = simpledialog.askstring("Input", "Enter the question:")
        answer = simpledialog.askstring("Input", "Enter the answer:")
        if question and answer:
            self.system.add_card(question, answer)
            messagebox.showinfo("Info", "Card added successfully!")

    def edit_card(self):
        question = simpledialog.askstring("Input", "Enter the question of the card you want to edit:")
        if question:
            new_answer = simpledialog.askstring("Input", "Enter the new answer:")
            if new_answer:
                self.system.edit_card(question, new_answer)
                messagebox.showinfo("Info", "Card updated successfully!")
            else:
                messagebox.showwarning("Warning", "No new answer provided.")
        else:
            messagebox.showwarning("Warning", "No question provided.")

    def delete_card(self):
        question = simpledialog.askstring("Input", "Enter the question of the card you want to delete:")
        if question:
            self.system.delete_card(question)
            messagebox.showinfo("Info", "Card deleted successfully!")
        else:
            messagebox.showwarning("Warning", "No question provided.")

    def view_cards(self):
        flashcards = self.system.view_cards()
        self.text_area.delete(1.0, tk.END)
        if flashcards:
            for card in flashcards:
                self.text_area.insert(tk.END, f"Q: {card.question} A: {card.answer} Status: {card.status}\n")
        else:
            self.text_area.insert(tk.END, "No flashcards to display.")

    def study_cards(self):
        num_cards = simpledialog.askinteger("Input", "How many cards do you want to study?")
        if num_cards:
            study_list = self.system.study_cards(num_cards)
            correct_count = 0

            for card in study_list:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, f"Question: {card.question}\n")
                user_answer = simpledialog.askstring("Input", "Enter your answer:")

                if user_answer and user_answer.lower() == card.answer.lower():
                    correct_count += 1
                    self.system._promote_card(card)
                    messagebox.showinfo("Info", "Correct!")
                else:
                    self.system._demote_card(card)
                    messagebox.showwarning("Info", f"Wrong. The correct answer is: {card.answer}")

            messagebox.showinfo("Info", f"Study session complete. You got {correct_count} out of {num_cards} correct.")

    def upload_dictionary(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.system.upload_dictionary(file_path)
            messagebox.showinfo("Info", "Dictionary uploaded successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    system = FlashcardSystem()
    app = FlashcardApp(root, system)
    root.mainloop()
