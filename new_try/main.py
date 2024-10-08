import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import csv
import random

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.flashcard_dict = []
        self.setup_ui()

    def setup_ui(self):
        self.root.title("German Food Vocabulary Flashcards")
        self.root.geometry("1200x400")
        self.root.configure(bg="#F5F5DC")

        # Create a frame for the buttons with a slightly darker beige color
        button_frame = tk.Frame(self.root, bg="#E6E6C8")
        button_frame.pack(side="top", fill="x")

        # Create buttons
        button_texts = ["Upload Dictionary", "Study Cards", "Add Card", "Delete Card", "Edit Card", "View Cards", "Save"]
        buttons = []

        for text in button_texts:
            if text == "Upload Dictionary":
                button = tk.Button(button_frame, text=text, width=15, command=self.upload_dictionary, font=("Comic Sans MS", 12))
            elif text == "Study Cards":
                button = tk.Button(button_frame, text=text, width=15, command=self.study_cards, font=("Comic Sans MS", 12))
            elif text == "Add Card":
                button = tk.Button(button_frame, text=text, width=15, command=self.add_card, font=("Comic Sans MS", 12))
            elif text == "Delete Card":
                button = tk.Button(button_frame, text=text, width=15, command=self.delete_card, font=("Comic Sans MS", 12))
            elif text == "Edit Card":
                button = tk.Button(button_frame, text=text, width=15, command=self.edit_card, font=("Comic Sans MS", 12))
            elif text == "View Cards":
                button = tk.Button(button_frame, text=text, width=15, command=self.view_cards, font=("Comic Sans MS", 12))
            elif text == "Save":
                button = tk.Button(button_frame, text=text, width=15, command=self.save_dictionary, font=("Comic Sans MS", 12))
            button.pack(side="left", padx=5, pady=10)
            buttons.append(button)

        # Create a frame for the main content area
        self.content_frame = tk.Frame(self.root, bg="#F5F5DC")
        self.content_frame.pack(expand=True, fill="both", padx=20, pady=20)

        # Create a Text widget for logging messages
        self.log_text = tk.Text(self.content_frame, wrap=tk.WORD, height=10, width=80, font=("Comic Sans MS", 12), bg="#F5F5DC")
        self.log_text.pack(expand=True, fill="both")
        self.log_text.config(state=tk.DISABLED)

    def log_message(self, message):
        self.log_text.config(state=tk.NORMAL)
        self.log_text.insert(tk.END, message + "\n\n")
        self.log_text.yview(tk.END)
        self.log_text.config(state=tk.DISABLED)

    def upload_dictionary(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    csv_reader = csv.reader(file)
                    self.flashcard_dict = [entry if len(entry) == 3 else entry + ['beginner'] for entry in csv_reader]
                self.log_message(f"Dictionary uploaded successfully. {len(self.flashcard_dict)} entries found.")
            except Exception as e:
                self.log_message(f"Error reading the file: {e}")

    def save_dictionary(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8', newline='') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerows(self.flashcard_dict)
                self.log_message("Dictionary saved successfully.")
            except Exception as e:
                self.log_message(f"Error saving the file: {e}")

    def study_cards(self):
        if not self.flashcard_dict:
            self.log_message("Please upload a dictionary first.")
            return

        num_cards = simpledialog.askinteger("Study Cards", "How many cards do you want to study?", 
                                            minvalue=1, maxvalue=len(self.flashcard_dict))
        if not num_cards:
            return

        status_weights = {
            'beginner': 5,
            'apprentice': 4,
            'guru': 3,
            'master': 2,
            'enlightened': 1,
            'burned': 0
        }

        weighted_cards = []
        for card in self.flashcard_dict:
            english, german, status = card
            weight = status_weights.get(status, 1)
            weighted_cards.extend([card] * weight)

        if len(weighted_cards) < num_cards:
            study_set = random.sample(weighted_cards, len(weighted_cards))
        else:
            study_set = random.sample(weighted_cards, num_cards)

        correct_count = 0
        total_cards = len(study_set)

        for card in study_set:
            english, german, status = card

            # Create a Toplevel window for the question
            study_window = tk.Toplevel(self.root)
            study_window.title("Study")
            study_window.geometry("400x200")
            study_window.configure(bg="#F5F5DC")
            study_window.lift()
            study_window.focus_force()

            # Display question
            question_label = tk.Label(study_window, text=f"What is the German word for '{english}'?", font=("Comic Sans MS", 12), bg="#F5F5DC")
            question_label.pack(pady=20)

            # Create an Entry widget for the user's answer
            answer_entry = tk.Entry(study_window, font=("Comic Sans MS", 12))
            answer_entry.pack(pady=10)

            def submit_answer():
                answer = answer_entry.get()
                study_window.destroy()
                if answer and answer.lower().strip() == german.lower().strip():
                    nonlocal correct_count
                    correct_count += 1
                    self.log_message(f"Correct! '{english}' in German is '{german}'.")
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
                    self.log_message(f"Status upgraded to '{card[2]}' for '{english}'.")
                else:
                    self.log_message(f"Incorrect. '{english}' in German is '{german}'.")

            submit_button = tk.Button(study_window, text="Submit", command=submit_answer, font=("Comic Sans MS", 12))
            submit_button.pack(pady=10)

            self.root.wait_window(study_window)  # Wait for the study_window to be destroyed

        percentage_correct = (correct_count / total_cards) * 100 if total_cards > 0 else 0
        self.log_message(f"Study session completed. Correct answers: {correct_count}/{total_cards} ({percentage_correct:.2f}%)")


    def add_card(self):
        english = simpledialog.askstring("Add Card", "Enter the English word:")
        if not english:
            return
        german = simpledialog.askstring("Add Card", "Enter the German word:")
        if not german:
            return
        self.flashcard_dict.append([english, german, 'beginner'])
        self.log_message(f"Card '{english} - {german}' added successfully.")

    def delete_card(self):
        if not self.flashcard_dict:
            self.log_message("Please upload a dictionary first.")
            return
        
        card_list = [f"{english} - {german}" for english, german, status in self.flashcard_dict]
        card_selection = simpledialog.askinteger("Delete Card", "Enter the number of the card to delete (1-based index):",
                                                minvalue=1, maxvalue=len(card_list))
        if not card_selection:
            return
        
        index = card_selection - 1
        if 0 <= index < len(self.flashcard_dict):
            del self.flashcard_dict[index]
            self.log_message("Card deleted successfully.")
        else:
            self.log_message("Invalid card number.")

    def edit_card(self):
        if not self.flashcard_dict:
            self.log_message("Please upload a dictionary first.")
            return
        
        card_list = [f"{english} - {german}" for english, german, status in self.flashcard_dict]
        card_selection = simpledialog.askinteger("Edit Card", "Enter the number of the card to edit (1-based index):",
                                                minvalue=1, maxvalue=len(card_list))
        if not card_selection:
            return
        
        index = card_selection - 1
        if 0 <= index < len(self.flashcard_dict):
            english = simpledialog.askstring("Edit Card", "Enter the new English word:", initialvalue=self.flashcard_dict[index][0])
            if not english:
                return
            german = simpledialog.askstring("Edit Card", "Enter the new German word:", initialvalue=self.flashcard_dict[index][1])
            if not german:
                return
            self.flashcard_dict[index] = [english, german, self.flashcard_dict[index][2]]
            self.log_message("Card edited successfully.")
        else:
            self.log_message("Invalid card number.")

    def view_cards(self):
        if not self.flashcard_dict:
            self.log_message("Please upload a dictionary first.")
            return
        
        # Create a new window for viewing cards
        view_window = tk.Toplevel(self.root)
        view_window.title("View Cards")
        view_window.geometry("600x300")  # Adjust size as needed
        view_window.configure(bg="#F5F5DC")
        view_window.lift()  # Bring the window to the foreground
        view_window.focus_force()  # Force focus on the window

        # Create a Text widget in the new window
        text_widget = tk.Text(view_window, wrap=tk.WORD, height=15, width=80, font=("Comic Sans MS", 12))
        text_widget.pack(expand=True, fill="both", padx=10, pady=10)

        # Insert card entries into the Text widget
        for english, german, status in self.flashcard_dict:
            text_widget.insert(tk.END, f"{english} - {german} (Status: {status})\n")
        
        text_widget.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()
