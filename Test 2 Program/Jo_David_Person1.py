# David Jo Test 2 Program
# Program prupose: To implement a Person class and Student subclass to practice object oriented programming and inheritance
from datetime import date

class Person():
    def __init__(self, firstName, middleName="", lastName=""):
        self.firstName = firstName
        self.middleName = middleName
        self.lastName = lastName

    def getFirstName(self):
        return self.firstName
    
    def getMiddleName(self):
        return self.middleName
    
    def getLastName(self):
        return self.lastName
    
    def setBirthday(self, birthdate: date):
        self.birthday = birthdate

    def getAge(self):
        today = date.today()
        birthday_passed = (today.month, today.day) < (self.birthday.month, self.birthday.day)
        age = today.year - self.birthday.year - birthday_passed
        return age
    
    def __str__(self):
        names = [self.firstName, self.middleName, self.lastName]
        full_name = " ".join(name for name in names if name)
        return f"{full_name} is {self.getAge()} years old."


class Student(Person):

    next_id = 1

    def __init__(self, firstName, middleName="", lastName="", gender=""):
        super().__init__(firstName, middleName, lastName)
        self.gender = gender
        self.idNumber = Student.next_id
        Student.next_id += 1


    def getidNumber(self):
        return self.idNumber
    
    def __str__(self):
        return f"{super().__str__()}, and {self.gender} student ID is {self.idNumber}."
    


def main():
    person1 = Person("Kobe", "", "Bryant")
    person1.setBirthday(date(1978, 8, 23))

    person2 = Person("Gigi", "", "Bryant")
    person2.setBirthday(date(2006, 5, 1))

    student1 = Student("David", "W.", "Jo", "his")
    student1.setBirthday(date(2005, 7, 15))

    student2 = Student("Mia", "A.", "Katsaros", "her")
    student2.setBirthday(date(2005, 4, 4))

    print(person1)
    print(person2)
    print(student1)
    print(student2)


if __name__ == "__main__":
    main()