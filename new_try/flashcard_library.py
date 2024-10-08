import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import csv
import random

class FlashcardApp:
    def __init__(self):
        self.flashcard_dict = []

    def upload_dictionary(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    csv_reader = csv.reader(file)
                    self.flashcard_dict = [entry if len(entry) == 3 else entry + ['beginner'] for entry in csv_reader]
                messagebox.showinfo("Upload Successful", f"Dictionary uploaded successfully. {len(self.flashcard_dict)} entries found.")
            except Exception as e:
                messagebox.showerror("Error", f"Error reading the file: {e}")

    def save_dictionary(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8', newline='') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerows(self.flashcard_dict)
                messagebox.showinfo("Save Successful", "Dictionary saved successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Error saving the file: {e}")

    def study_cards(self):
        if not self.flashcard_dict:
            messagebox.showwarning("No Dictionary", "Please upload a dictionary first.")
            return

        num_cards = simpledialog.askinteger("Study Cards", "How many cards do you want to study?", 
                                            minvalue=1, maxvalue=len(self.flashcard_dict))
        if not num_cards:
            return

        study_set = random.sample(self.flashcard_dict, num_cards)
        
        for card in study_set:
            english, german, status = card
            answer = simpledialog.askstring("Study", f"What is the German word for '{english}'?")
            
            if answer and answer.lower().strip() == german.lower().strip():
                messagebox.showinfo("Correct!", f"Correct! '{english}' in German is '{german}'.")
                if status == 'beginner':
                    card[2] = 'apprentice'
                elif status == 'apprentice':
                    card[2] = 'guru'
                elif status == 'guru':
                    card[2] = 'master'
                elif status == 'master':
                    card[2] = 'enlightened'
                elif status == 'enlightened':
                    card[2] = 'burned'
                messagebox.showinfo("Status Upgrade", f"Status upgraded to '{card[2]}' for '{english}'.")
            else:
                messagebox.showinfo("Incorrect", f"Incorrect. '{english}' in German is '{german}'.")

        messagebox.showinfo("Study Complete", "Study session completed.")

    def add_card(self):
        english = simpledialog.askstring("Add Card", "Enter the English word:")
        if not english:
            return
        german = simpledialog.askstring("Add Card", "Enter the German word:")
        if not german:
            return
        self.flashcard_dict.append([english, german, 'beginner'])
        messagebox.showinfo("Card Added", f"Card '{english} - {german}' added successfully.")

    def delete_card(self):
        if not self.flashcard_dict:
            messagebox.showwarning("No Dictionary", "Please upload a dictionary first.")
            return
        
        card_list = [f"{english} - {german}" for english, german, status in self.flashcard_dict]
        card_selection = simpledialog.askinteger("Delete Card", f"Select a card to delete (1-{len(card_list)}):", 
                                                 minvalue=1, maxvalue=len(card_list))
        if card_selection:
            del self.flashcard_dict[card_selection - 1]
            messagebox.showinfo("Card Deleted", "Card deleted successfully.")

    def view_cards(self):
        if not self.flashcard_dict:
            messagebox.showwarning("No Dictionary", "Please upload a dictionary first.")
            return
        
        card_list = [f"{english} - {german} (Status: {status})" for english, german, status in self.flashcard_dict]
        card_list_str = "\n".join(card_list)
        messagebox.showinfo("View Cards", card_list_str)

    def edit_card(self):
        if not self.flashcard_dict:
            messagebox.showwarning("No Dictionary", "Please upload a dictionary first.")
            return
        
        card_list = [f"{english} - {german}" for english, german, status in self.flashcard_dict]
        card_selection = simpledialog.askinteger("Edit Card", f"Select a card to edit (1-{len(card_list)}):", 
                                                 minvalue=1, maxvalue=len(card_list))
        if card_selection:
            card_index = card_selection - 1
            english, german, status = self.flashcard_dict[card_index]
            new_english = simpledialog.askstring("Edit Card", "Enter the new English word:", initialvalue=english)
            new_german = simpledialog.askstring("Edit Card", "Enter the new German word:", initialvalue=german)
            if new_english and new_german:
                self.flashcard_dict[card_index] = [new_english, new_german, status]
                messagebox.showinfo("Card Edited", "Card edited successfully.")
