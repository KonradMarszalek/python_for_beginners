import os


def find_file(directory, filename):
    if not os.path.isdir(directory):
        result = "Error: directory " + directory + " does not exist!"
        print(result)
        return result
    full_path = os.path.join(directory, filename)
    if not os.path.isfile(full_path):
        result = "Error: file " + full_path + " does not exist!"
        print(result)
        return result
    result = "File " + full_path + " exist :)"
    print(result)
    return result
