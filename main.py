def replace_occurrence(chaine, mot, character, occurrence):
    mots = list(chaine) # to convert the string into a list
    count = 0
    i = 0

    while i <= len(mots) - len(mot): # parkour of the list
        if "".join(mots[i:i+len(mot)]) == mot: # to check if we found the full word
            count += 1
            if count == occurrence:
                    mots[i:i+len(mot)] = character # replace the entire word with the character
                    break # stop after replacing the required occurrence
        i += 1

    return "".join(mots) # rebuild the final string

# the code to use :
#phrase = "Je suis étudiant à l'USTHB, je me gare à l'USTHB, j'habite près de l'USTHB et je connais l'USTHB depuis 2 ans"
#result = replace_occurrence(phrase, "USTHB", "?", 2)
#print(result)

phrase = input("enter the string : ")
mot = input("enter the word to replace : ")
character = input("enter the character to replace with : ")
occurrence = int(input("enter the occurrence (1-4) : "))

result = replace_occurrence(phrase, mot, character, occurrence)
print("final result :", result)