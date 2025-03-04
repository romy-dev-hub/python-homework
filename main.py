import re

def replacement(chaine, mot, rep, occ):
    # Splitting using regex (handling multiple delimiters)
    words = re.split(r"([ ,;.!?'])", chaine)
    words = [word for word in words if word.strip()]  # Remove empty strings

    # Finding occurrences
    idexs = [i for i, word in enumerate(words) if word == mot]

    # If occurrence is invalid, return the original string
    if occ > len(idexs) or occ < 1:
        print("Error: The word doesn't appear that many times!")
        return chaine

    # Replace the specific occurrence
    words[idexs[occ - 1]] = rep

    # Reconstruct the string
    return " ".join(words)

# Main code
chaine = input("Paste your paragraph: ")
mot = input("Enter the string you want to change: ")
rep = input("Enter what you want to replace it with: ")
occ = int(input("Which occurrence: "))

print("\nThe paragraph before modification:\n" + chaine)

chaine = replacement(chaine, mot, rep, occ)

print("\nThe paragraph after modifications:\n" + chaine)
