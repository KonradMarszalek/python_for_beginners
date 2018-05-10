import os
from os import path
from os.path import isfile

filename = "wycena.pdf"
directory = "/Users/konradm/Downloads/"

if not os.path.isdir(directory):
    print("Error: directory " + directory + " does not exist!")
    exit(1)
full_path = path.join(directory, filename)
if not isfile(full_path):
    print("Error: file " + full_path + " does not exist!")
    exit(1)
print("File " + full_path + " exist :)")
