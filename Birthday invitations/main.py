#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("input/Letters/starting_letter.txt", mode="r") as starting_text:
    matrix = starting_text.read()


with open("input/Names/invited_names.txt", mode="r") as invited_names_doc:
    names_list = invited_names_doc.readlines()

for x in range(len(names_list)):
    name = names_list[x].strip()
    personalized_letter = matrix.replace("[name]", name)
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as new_letter:
        new_letter.write(personalized_letter)
