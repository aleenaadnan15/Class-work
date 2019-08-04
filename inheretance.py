class  Human():
    def __init__(self, name, father_name, nic):
        self.name = name
        self.father_name = father_name
        self.nic = nic
    def showdetails(self):
        print("Name:", self.name, "Father Name:", self.father_name, "CNIC:", self.nic)

    def printer(self):
        print("This is a human")

class Student(Human):
    def __init__(self, name, father_name, nic, rollno):
        super().__init__(name, father_name, nic)
        self.rollno = rollno

    #def eat(self):
        #print(self.name, self.father_name, "is eating biryani")

class Teacher(Human):
    def __init__(self, name, father_name, nic, id):
        super().__init__(name, father_name, nic)
        self.id = id

    # def eat(self):
    #     print(self.name, self.father_name, "is eating biryani")

class Admin(Human):
    def __init__(self, name, father_name, nic, designation):
        super().__init__(name, father_name, nic)
        self.designation = designation

    # def eat(self):
    #     print(self.name, self.father_name, "is eating biryani")


# st = Student(name = "Ailn", father_name = "Adnan", program = "eatting biryani")
# st2 = Student("Alina", "Ad", "Zinger")
# print(st2.name)
# st.eat()

st = Student("Alina", "Adnan", "4210140755946", 23)
tea = Teacher("Inam", "ad", "421012345678", 2)
admin = Admin("umair", "shahzad", "4210112345", "HR")
st.showdetails()
tea.showdetails()
admin.showdetails()
