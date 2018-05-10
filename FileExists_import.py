from os.path import isfile, isdir, join

filename = "Charter.pdf"
directory = "/Users/kmarszalek/Downloads/"

if not isdir(directory):
    print("Error: directory " + directory + " does not exist!")
    exit(1)
full_path = join(directory, filename)
if not isfile(full_path):
    print("Error: file " + full_path + " does not exist!")
    exit(1)
print("File " + full_path + " exist :)")
