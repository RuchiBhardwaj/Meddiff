class Student:
    def __init__(self, name, rollno, age, gender):
        self.name = name
        self.rollno = rollno
        self.age = age
        self.gender= gender

    def insert(self, Name, Rollno, Age, Gender):
        ob = Student(Name, Rollno, Age, Gender)
        ls.append(ob)

    def Get(self, ob):
        print("RollNo : {}\nName: {}\nAge: {}\nGender: {}\n ".format(ob.rollno,ob.name, ob.age, ob.gender))

    def search(self, rn):
        for i in range(ls.__len__()):
            if (ls[i].rollno == rn):
                return i

    def delete(self, rn):
        i = obj.search(rn)
        del ls[i]

    def update(self, rn, No, Name):
        i = obj.search(rn)
        roll = No
        ls[i].rollno = roll
        ls[i].name = Name


ls = []
obj = Student('', 0, 0, '')

obj.insert("Ram", 1, 10, "F")
obj.insert("Shyam", 2, 90, "M")
obj.insert("BalRam", 3, 80, "F")

print("\n")
print("\nList of Students\n")
for i in range(ls.__len__()):
    obj.Get(ls[i])


print("\n Student Found, ")
s = obj.search(2)
obj.Get(ls[s])


obj.delete(2)
print(ls.__len__())
print("List after deletion")
for i in range(ls.__len__()):
    obj.Get(ls[i])


obj.update(3, 2,"Shyamu")
print(ls.__len__())
print("List after updation")
for i in range(ls.__len__()):
    obj.Get(ls[i])


print("This is all about Student Details!")

