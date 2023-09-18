with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    words = file_contents.split()
    print(len(words))

    letter_count = {}
    for letter in file_contents:
        lower_letter = letter.lower()
        if lower_letter in letter_count:
            letter_count[lower_letter] = letter_count[lower_letter] + 1
        else:
            letter_count[lower_letter] = 1

    print(letter_count)