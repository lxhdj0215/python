import pymysql.cursors

connection = pymysql.connect(host="localhost", user="root", password="admin", db="wgj", charset="utf8",
                             cursorclass=pymysql.cursors.DictCursor)


class AddressBook:
    def __init__(self):
        self.contact_list = []

    def add_contact(self, name, mobile_phone, conn):
        self.contact_list.append({"name": name, "mobile_phone": mobile_phone})
        try:
            cursor = conn.cursor()
            sql = "insert into contacts (name, mobile_phone) VALUES (%s, %s)"
            cursor.execute(sql, (name, mobile_phone))
            cursor.close()
            conn.commit()
        finally:
            print()

    def print(self):
        for contact in self.contact_list:
            print("name:%s mobile_phone:%s" % (contact["name"], contact["mobile_phone"]))

    def print_list(self, conn):
        try:
            cursor = conn.cursor()
            sql = "SELECT * FROM contacts"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
        finally:
            conn.close()


addressBook = AddressBook()
addressBook.add_contact("wgj", "1212", connection)
addressBook.print_list(connection)
# addressBook.add_contact("LiBai", "9999")
# addressBook.add_contact("DuPu", "888")
# addressBook.print_list()


# try:
#     cursor = connection.cursor()
#     sql = "insert into contacts (name, mobile_phone) VALUES (%s, %s)"
#     cursor.execute(sql, ('fireflyc', '18921312900'))
#     cursor.close()
#
#     connection.commit()
#
#     cursor = connection.cursor()
#     sql = "SELECT * FROM contacts"
#     cursor.execute(sql)
#     result = cursor.fetchall()
#     print(result)
# finally:
#     connection.close()
