# TODO: Create a letter using starting_letter.txt
with open("./Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_text:
    contents = letter_text.read()
    for name in names:
        fixed_name = name.strip()
        final_letter = contents.replace("[name]", fixed_name)
        with open(f"./Output/ReadyToSend/letter_to_{fixed_name}.txt", mode="w") as letter:
            letter.write(final_letter)
