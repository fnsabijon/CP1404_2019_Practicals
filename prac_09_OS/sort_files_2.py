import os

def main():
    os.chdir("FilesToSort")
    extension_to_category = {}
    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            extension = filename.split(".")[-1]
            if extension not in extension_to_category:
                category = input("What category would you like to sort {} files into? ".format(extension))
                try:
                    os.mkdir(category)
                except FileExistsError:
                    pass
                extension_to_category[extension] = category
                print(extension_to_category)

            os.rename(filename, os.path.join(extension_to_category[extension], filename))
main()