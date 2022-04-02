# Hi Guys, my name is Alberto Alesci I studied economics and finance actually
# I'm working in Accenture as ABAP developer. But I love 
# mathematics and statistics. 
# 
# I hope this can be useful to find a work in Banks, investment found,
# crypto exchange, in the role of data analist or developer.  
# This are simple example about object programmation in Python. 
# I create an object and I explain the different variables.

##### CLASS AND ISTANCE 

class Student: 
    #Variable of the class(This are attribute that are shering with all istance of the class 
    Hours_of_lesson = 35

    Number_of_student = 0

    def __init__(self, name, surmane , age , subject ):
        #variable of the istance: 
        self.name = name
        self.surname = surmane
        self.age = age 
        self.subject = subject 
        Student.Number_of_student += 1

    def personal_data(self):
        return  f" DATA:\n Nome:{self.name}\n Cognome:{self.surname}\n Hours:{self.Hours_of_lesson}\n" 
        

#In this way I instanciate my ogject.
stud_1 = Student("Mario","Draghi","74","Economics" ) 
stud_2 = Student("Jerome","Powell","69","Economics")


print(stud_2.personal_data()) #I call the method to show me the attribute. 
print(Student.personal_data(stud_1)) #This is improtant because allows you to understand the reason of self. 
#The last two line of code do the same things 

#With function dict we can see: 
print(Student.__dict__) #The variable of the calss (Hours_of_lesson)  
print('')
print(stud_1.__dict__)  #The variable of my object  (name, surmane , age , subject + Hours_of_lesson)


#I wnat the evry time i istanciate a new Student the variable "Number_of_student" increment of one.
print(Student.Number_of_student)  # --> 2 
stud_3 = Student(" Andrew ","Bailey","63","Economics")

print(Student.Number_of_student)  # --> 3





