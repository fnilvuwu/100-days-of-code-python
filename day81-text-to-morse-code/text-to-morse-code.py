print('''
  __  __                                          _           
 |  \/  |___ _ _ ___ ___   __ ___ _ ___ _____ _ _| |_ ___ _ _ 
 | |\/| / _ \ '_(_-</ -_) / _/ _ \ ' \ V / -_) ' \  _/ -_) '_|
 |_|  |_\___/_| /__/\___| \__\___/_||_\_/\___|_||_\__\___|_|  
                                                              
''')

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----'}

input_text = input(
    "Text to morse code (Letter A-Z and Number 0-9 Only)\n'#' is used for unknown character and should be ignored\n")
words = input_text.upper().split()

letters_table = []
for word in words:
    letters = list(word)
    letters_table.append(letters)

converted_string = ""

for index, word in enumerate(letters_table):
    for letter in word:
        try:
            converted_string += MORSE_CODE_DICT[letter] + ' '
        except KeyError:
            converted_string += "# "

    if index != len(letters_table)-1:
        converted_string += "/ "

print(converted_string)
