from os.path import isfile, join, isdir

filename = "wycena.pdf"
directory = "/Users/konradm/Downloads/"

if not isdir(directory):
    print("Error: directory {directory} does not exist!".format(directory=directory))
    exit(1)
full_path = join(directory, filename)
if not isfile(full_path):
    print("Error: file {full_path} does not exist!".format(full_path=full_path))
    exit(1)
print("File {full_path} exist :)".format(full_path=full_path))
