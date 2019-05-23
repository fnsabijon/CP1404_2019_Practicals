import os

def main():
    # filenames = ["Away In A Manger.txt", "SilentNight.txt", "O little town of bethlehem.TXT", "ItIsWell (oh my soul).txt"]
    # for filename in filenames:
    #     new_name = get_fixed_filename(filename)
    #     print(new_name)
    os.chdir("Lyrics")

    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            os.rename(os.path.join(directory_name, filename), new_name)
            print("{} has been renamed to {}".format(filename, new_name))


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = ""
    for i, char in enumerate(filename):
        if i + 1 != len(filename):
            previous_character = filename[i - 1]
            next_character = filename[i + 1]
            if char.islower() and next_character.isupper():
                new_name += char + "_"
            elif previous_character == ".":
                new_name += char
            elif char.islower() and not previous_character.isalpha():
                new_name += char.upper()
            else:
                new_name += char
        else:
            new_name += char
    new_name = new_name.replace(" ", "_").replace(".TXT", ".txt")
    return new_name

main()