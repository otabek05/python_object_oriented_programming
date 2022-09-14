class Person:
    person=0
    def __init__(self,name,surname):
        self.name=name
        self.surname=surname
        self.person+=1
    def get_name(self):
        print(f'name:{self.name} surname:{self.surname}')


myname=Person('Otabek','Toshmukhammedov')
myname.get_name()


class Student(Person):
    def __init__(self, name, surname,age,enrolled_year):
        super().__init__(name, surname)
        self.age=age
        self.enrolled_year=enrolled_year
    def get_all(self):
        print(f'name:{self.name},surname:{self.surname},age:{self.age},enrolled_year:{self.enrolled_year}')
    
    def get_name(self):
        print(f'name:{self.name};')


new_Student=Student('John','Mark',22,2022)

new_Student.get_all()