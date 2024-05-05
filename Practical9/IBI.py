class Student(object):
    def __init__(self, name, major, codescore, groupscore, examscore):
        self.name = name
        self.major = major
        self.codescore = codescore
        self.groupscore = groupscore
        self.examscore = examscore
student1 = Student("John Lee", "BMI", 85, 85, 85) #example
print(student1)