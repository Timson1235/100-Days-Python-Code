import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import csv
import random

dictionary = {}

def upload_dictionary():
    global dictionary
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            dictionary = {rows[0]: rows[1] for rows in reader}
            print("Dictionary uploaded:", dictionary)

def study_cards():
    if not dictionary:
        messagebox.showwarning("Warning", "Please upload a dictionary first.")
        return
    
    num_vocab = simpledialog.askinteger("Input", "How many vocabularies do you want to study?")
    
    if num_vocab is None or num_vocab <= 0:
        messagebox.showwarning("Warning", "Please enter a valid number of vocabularies.")
        return
    
    selected_keys = random.sample(list(dictionary.keys()), min(num_vocab, len(dictionary)))
    
    for key in selected_keys:
        answer = simpledialog.askstring("Study", f"What is the value for: {key}?")
        correct_answer = dictionary[key]
        if answer == correct_answer:
            messagebox.showinfo("Correct", f"Correct! The value for '{key}' is indeed '{correct_answer}'.")
        else:
            messagebox.showerror("Incorrect", f"Incorrect. The value for '{key}' is '{correct_answer}'.")

# Create the main window
root = tk.Tk()
root.title("Flashcard System")

# Set the window size
root.geometry("600x400")

# Set the background color to beige
root.configure(bg="beige")

# Create a frame for the top section with a slightly different color and increased height
top_frame = tk.Frame(root, bg="#e0d6b9", height=100)  # Increased height
top_frame.pack(side=tk.TOP, fill=tk.X, pady=10)
top_frame.pack_propagate(False)  # Prevent the frame from resizing to fit its children

# Create a frame for the rest of the window
middle_frame = tk.Frame(root, bg="beige")
middle_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Create the "Upload Dictionary" button
upload_button = tk.Button(top_frame, text="Upload Dictionary", command=upload_dictionary)
upload_button.pack(side=tk.LEFT, padx=5)

# Create the "Study Cards" button
study_button = tk.Button(top_frame, text="Study Cards", command=study_cards)
study_button.pack(side=tk.LEFT, padx=5)

# Create 5 more buttons and add them to the top frame
for i in range(5):
    button = tk.Button(top_frame, text=f"Button {i+3}")
    button.pack(side=tk.LEFT, padx=5)

# Start the Tkinter event loop
root.mainloop()
