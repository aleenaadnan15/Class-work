class student():
    def __init__(self, name,age,rollno,gender):
        self.name = name
        self.age = age
        self.rollno = rollno
        self.gender = gender

    def print_details(self):
        print('name:',self.name,'age:',self.age, 'rollno:',self.rollno, 'gender:',self.gender)

student1 = student('Ailn', 22, 55,'female')
student2 = student('jaisha' , 23, 56 , 'female')
student3 = student('Kanwal', 22, 57 , 'female')
student1.print_details()
student2.print_details()
student3.print_details()