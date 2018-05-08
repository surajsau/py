import fileinput

# Read in the file
with open("edict2.json", 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace("{\"tags\"", ",{\"tags\"")

# Write the file out again
with open("edict1.json", 'w') as file:
  file.write(filedata)

# with fileinput.FileInput("../edict2.json", inplace=True, backup='.bak') as file:
#     for line in file:
#         print(line.replace("{\"tags\"", ",{\"tags\""), end="")
