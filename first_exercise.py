file_context = open("D:\\1.txt", "r")
context = file_context.read().replace("\n", " ").lower()
contexts = context.split(" ")
dict_1 = {}
for word in contexts:
    if dict_1.__contains__(word):
        dict_1[word] += 1
    else:
        dict_1[word] = 1
file_out = open("D:\\out.txt", "w")
for key in dict_1:
    file_out.write(key + "：" + str(dict_1[key]))
    file_out.write("\n")
    print(key + "：" + str(dict_1[key]))
file_context.close()
file_out.close()
