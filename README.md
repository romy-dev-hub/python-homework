# python-homework

## description:
This Python script allows users to replace a specific occurrence of a word in a given text with a specified character. The script takes user input for the text, the word to be replaced, the replacement character, and the occurrence number to modify.

## Features

Replaces a specific occurrence (1st, 2nd, 3rd, etc.) of a word in a string.

Allows the user to input the sentence, target word, replacement character, and occurrence number.

Ensures that only the specified occurrence is modified.

Does not use the built-in replace() function.

## Usage

### Running the Script

1. Open a terminal or command prompt.

2. Run the script using Python:

python replace_occurrence.py

3. Enter the required inputs when prompted:

. Phrase: The sentence in which replacement should occur.

. Word to replace: The target word.

. Replacement character: The character to replace the word with.

. Occurrence to replace: The occurrence number (1-4).

### Example

Input:

Entrez la phrase : Je suis étudiant à l'USTHB, je me gare à l'USTHB, j'habite près de l'USTHB et je connais l'USTHB depuis 2 ans
Entrez le mot à remplacer : USTHB
Entrez le caractère de remplacement : ?
Entrez l'occurrence à remplacer (1-4) : 2

Output:

Je suis étudiant à l'USTHB, je me gare à ?, j'habite près de l'USTHB et je connais l'USTHB depuis 2 ans

## Constraints

. The function does not use the replace() method.

. The function correctly handles cases where the string does not contain punctuation (commas, apostrophes, etc.).

. The replacement applies only to the specified occurrence.

## Requirements

Python 3.x

## File Structure


├── replace_occurrence.py  # Main script

├── README.md              # Documentation

## License

This project is open source.

## Author

Developed by xiao ro

