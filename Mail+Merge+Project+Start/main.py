#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



with open("./Input/Names/invited_names.txt") as file:
    my_list = file.read().split('\n')

for item in my_list:
    with open("./Input/Letters/starting_letter_copy.txt", mode="r") as file:
        content = file.read()
        new_content = content.replace("[name]", item)
        with open(f"./Output/ReadyToSend/letter_for_{item}.txt", mode="w") as modified:
            modified.write(new_content)
