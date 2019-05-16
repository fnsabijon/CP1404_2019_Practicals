
def main():

    filename = "oLhiUJLK ih.TXT"

    new_name = get_fixed_filename(filename)

def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    # new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    for i, char in enumerate(filename):
        if i == 0:
            char = char.upper()
            break
        elif char.isupper():

    return

main()