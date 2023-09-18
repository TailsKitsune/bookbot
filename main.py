file = "books/frankenstein.txt"
with open(file) as f:
    file_contents = f.read()
    words = file_contents.split()

    print(f"--- Begin report of {file} ---")
    print(f"{len(words)} words found in the document")

    letter_count = {}
    for letter in file_contents:
        lower_letter = letter.lower()
        if lower_letter in letter_count:
            letter_count[lower_letter] = letter_count[lower_letter] + 1
        else:
            letter_count[lower_letter] = 1

    letters = []
    for letter in letter_count:
        if letter.isalpha():
            letters.append((letter_count[letter], letter))

    letters.sort(reverse=True)

    for letter in letters:
        print(f"The '{letter[1]}' character was found {letter[0]} times")

    print("--- End report ---")