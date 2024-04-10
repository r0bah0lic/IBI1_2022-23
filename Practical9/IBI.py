class Student(object):
    def __init__(self, name, major, codescore, groupscore, examscore):
        self.name = name
        self.major = major
        self.codescore = codescore
        self.groupscore = groupscore
        self.examscore = examscore
    def display(self):
        print(f"name:{self.name},major:{self.major},code portfolio score:{self.codescore},group project score:{self.groupscore},exam score:{self.examscore}")
student1 = Student("John Lee", "BMI", 85, 85, 85) #example
student1.display()