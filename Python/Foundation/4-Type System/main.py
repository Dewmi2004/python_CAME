x = 10
print(type(x))
x = "CAME"
print(type(x))

x = 10
y = "2"
print(x * y)
# print(x - y)

class Student:
    def printDetails(self):
        print("student Class")

class customer:
    def printDetails(self):
        print("customer class")

        s = Student()
        c = Customer()

        def printPerson(p):
            p.printDetails()

            printPerson(s)
            printPerson(c)

            name = "CAME"
            print(NAME)