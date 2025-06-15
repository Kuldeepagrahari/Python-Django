class Student:
    college = "PDPM IIITDM Jabalpur"
    # Constructor
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.assignmentStarted: bool = False
        self.collName:str = "pdpm"
    
    # Instance methods -> Which uses object members------------------------------------------------
    def startAssignment(self):
        if(self.assignmentStarted):
            print("Assignment started already!")
        else:
            self.assignmentStarted = True
            print("Assignment Started!")

    def endAssignment(self):
        if(self.assignmentStarted == False):
            print("Assignment ended already!")
        else:
            self.assignmentStarted = False
            print("Assignment Ended!")
    
    def runAssignment(self, minutes: int):
        if(self.assignmentStarted):
            print("Assignment Started for", minutes, "Minutes")
        else:
            print("First Start the Assignment")
    #----------------------------------------------
    # Class method -> uses class members
    def collegeName(cls):
        print(cls.college)
    #--------------------------------------------------------------
    # Static method -> utility method, does not use class members
    def sum(a, b):
        print(a + b)

# Objects with Constructor Calling
student1:Student = Student("Sam", "22bec106")
student2:Student = Student("Prateek", "22bcs194")
print(student1.name, ":", student1.rollno)
print(student2.name, ":", student2.rollno)

student1.startAssignment()
student1.runAssignment(30)
student1.startAssignment()
student1.endAssignment()
student1.runAssignment(40)
student1.endAssignment()

print(student1.college)
student1.collegeName()

# self vs cls : self -> reference to object, cls -> reference to class members