import csv

# Define the vocabulary data
vocab_data = [
    ["apple", "Apfel"],
    ["bread", "Brot"],
    ["cheese", "Käse"],
    ["water", "Wasser"],
    ["potato", "Kartoffel"],
    ["milk", "Milch"],
    ["egg", "Ei"],
    ["meat", "Fleisch"],
    ["fish", "Fisch"],
    ["vegetable", "Gemüse"],
    ["fruit", "Obst"],
    ["rice", "Reis"],
    ["pasta", "Nudeln"],
    ["soup", "Suppe"],
    ["salad", "Salat"],
    ["chicken", "Huhn"],
    ["beef", "Rindfleisch"],
    ["pork", "Schweinefleisch"],
    ["tomato", "Tomate"],
    ["carrot", "Karotte"],
    ["onion", "Zwiebel"],
    ["garlic", "Knoblauch"],
    ["butter", "Butter"],
    ["salt", "Salz"],
    ["pepper", "Pfeffer"],
    ["sugar", "Zucker"],
    ["coffee", "Kaffee"],
    ["tea", "Tee"],
    ["juice", "Saft"],
    ["beer", "Bier"]
]

# Define the file name
file_name = "vocabulary.csv"

# Write the data to a CSV file
with open(file_name, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(vocab_data)

print(f"CSV file '{file_name}' created successfully.")
