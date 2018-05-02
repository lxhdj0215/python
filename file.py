file = open("D:\\1.txt", "r")

for line in file.readlines():
    if line.__contains__("Football"):
        print(line)

file.close()
