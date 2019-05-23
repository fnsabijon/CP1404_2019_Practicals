import os

def main():
    os.chdir("FilesToSort")

    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            extension = filename.split(".")
            try:
                os.mkdir(extension[1])
            except FileExistsError:
                pass
            print("{}/{}".format(extension, filename))
            os.rename(filename, os.path.join(extension[1], filename))


main()