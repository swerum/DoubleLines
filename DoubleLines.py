import sys

if len(sys.argv) != 2:
    print("program needs 1 commandline argument containing the name of your original text file.")
    exit(0)

file_name = sys.argv[1]
f = open(file_name, "r")
lines = f.readlines()


f.close()
f = open("output.txt", "wx")

for line in lines:
    line += "\n"
    print(line)
    f.writelines([line])

