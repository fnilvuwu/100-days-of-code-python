import pandas
nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter:row.code for (index, row) in nato_alphabet.iterrows()}

def process_nato():
    user_input = input("Enter a word to convert\n").upper()
    input_nato = [nato_dict[letter] for letter in user_input]
    print(input_nato)

still_error = True
while still_error:
    try:
        process_nato()
    except KeyError:
        print("Sorry, only letters in the alphabet pwease.")
    else:
        still_error = False