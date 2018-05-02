# encoding=utf-8
print('hello world，王桂军')
# data type
print(100 + 150)
print(500 / 6)
print(500.0 / 6)
print("100+100=" + str(100 + 100))
print(88888899999999999999999999999999999999 * 99999999999999999999999999999999)

print("-------------------list")
l = [1, 2, 3, 4, 'hello']
print(l)
print("类型：" + str(type(l)))
print(l[0])
print("长度：" + str(len(l)))
print(l[0:1])
print(l[-5:-4])
print(l[:3])
print(l[1:])

print("------------------dict")
person = {"name": "wgj", "age": 25, "city": "HeNan"}
print(person)
print(type(person))
print(person["name"])
person["name"] = "tom"
print(person["name"])

# if else
if "tom" == person["name"]:
    print("name is tom")
else:
    print("wgj")

# for
print("------------------for")
for i in range(0, 10):
    print(i)
print("------------------while")
name_list = ["wgj", "tom", "jack"]
i = 0
while name_list[i] != "jack":
    i += 1
i = 0
if i < len(name_list):
    print(name_list[i])
while i < len(name_list) and name_list[i] != "jck":
    i += 1
if i < len(name_list):
    print(name_list)
for name in name_list:
    if name == "wgj":
        break
print(name)

print("---------------function")


def my_max(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2


print(my_max(1, 100))

print("====================file")
print("====================write")
f = open("D:\\wgj.txt", "w")
for i in range(1, 10):
    f.write("wgj")
    f.write("\n")
f.write("wgj")
f.close()
print("====================read")
f = open("D:\\wgj.txt", "r")
print(f.read())
f.close()
