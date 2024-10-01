#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Names/invited_names.txt") as invites:
    invitesNames = invites.readlines()
    counter = 0
    for item in invitesNames:
        newItem = item.strip('\n')
        invitesNames[counter] = newItem
        counter += 1

counter = 0
for item in invitesNames:
    with open("Input/Letters/starting_letter.txt") as originalLetter:
        originalTemplate = originalLetter.read()
        inviteTemplate = originalTemplate.replace("[name]", f"{invitesNames[counter]}")

    with open(f"Output/ReadyToSend/letter_to_{invitesNames[counter]}.txt", mode="w") as newLetter:
        newLetter.write(f"{inviteTemplate}")

    counter += 1



