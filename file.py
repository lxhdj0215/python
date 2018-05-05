# encoding=utf8
file = open("D:\\1.txt", "r")

for line in file.readlines():
    if line.__contains__("Football"):
        print(line)

file.close()

file = open("D:\\w.txt", "w")
for i in range(100):
    file.write("王桂军" + str(i))
    file.write("\n")
file.close()

file = open("D:\\w.txt", "r")
print(file.read())
file.close()
