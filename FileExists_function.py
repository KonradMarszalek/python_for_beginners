from os.path import isfile, isdir, join

filename = "wycena.pdf"
directory = "/Users/konradm/Downloads"


def exists(file_name, file_directory):
    if not isdir(file_directory):
        print("Error: directory " + file_directory + " does not exist!")
        return False
    full_path = join(file_directory, file_name)
    if not isfile(full_path):
        print("Error: file " + full_path + " does not exist!")
        return False
    print("File " + full_path + " exist :)")
    return True


result = exists(file_name=filename, file_directory=directory)
print(result)
