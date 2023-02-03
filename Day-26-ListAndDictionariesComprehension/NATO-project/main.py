import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}

user_type = input("Enter a word: ").upper()
user_type_letter = [letter for letter in user_type]

answer = [nato_alphabet[letter] for letter in user_type_letter]
print(answer)
