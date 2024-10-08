import pandas as pd

# Example DataFrame
df = pd.read_csv(r"C:\Users\TimPr\100-Days-Python-Code-2\Day26\nato_phonetic_alphabet.csv")

# Create the dictionary using dictionary comprehension
result_dict = {row['letter']: row['code'] for index, row in df.iterrows()}

# Take an input string from the user
input_string = input("Enter a string: ").upper()

# Create a list of each uppercase letter in the input string
letter_list = list(input_string)

# Check if each letter occurs in the dictionary and print the corresponding value
for letter in letter_list:
    if letter in result_dict:
        print(f"The value for '{letter}' is {result_dict[letter]}")
    else:
        print(f"'{letter}' is not in the dictionary")
