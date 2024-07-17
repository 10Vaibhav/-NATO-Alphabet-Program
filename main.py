import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

dictor = {row.letter: row.code  for (index,row) in data.iterrows()}

def generate():
    try:
        word = input("Enter a word: ").upper()
        phonetic =[dictor[select] for select in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate()
    else:
        print(phonetic)

generate()