import pandas
alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
phonetic_dict = {row.letter: row.code for (index, row) in alphabet_data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()
for letter in user_input:
    phonetic_words = [phonetic_dict[letter] for letter in user_input]

print(phonetic_words)
