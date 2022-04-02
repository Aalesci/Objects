# Hi Guys, my name is Alberto Alesci I studied economics and finance actually now
# I'm working in Accenture as ABAP developer. But I love 
# mathematics and statistics. 
# 
# I hope this can be useful to find a work in Banks, investment found,
# crypto exchange, in the role of data analist or developer.
# I'm looking for a job with Mathemtics, statistic, pyhton and menage of money.    
# This are simple example about object programmation in Python. 
# I create an object and I explain the different variables.

# Concept of Mother or superclass ()

class Person:

    def __init__(self, name, surmane , age , adress ):
        
        self.name = name
        self.surname = surmane
        self.age = age 
        self.adress = adress 

    def data(self):
        output_data = f"""
        Name: {self.name}
        Surname:{self.surname}
        Age: {self.age} 
        Adress:{self.adress}
        """
        return output_data
        
    def data_change(self):
        print("""1 Change Name
                 2 Change Surname
                 3 Change Age 
                 4 Change Adress """ ) 
        scelta = input("What do you want modify?")
        if scelta == '1': self.name = input("Insert Name  ")
        if scelta == '2': self.surname = input("Insert Surname  ")
        if scelta == '3': self.age = input("Insert Age  ")
        if scelta == '4': self.adress = input("Insert Adress  ")


             

# I create my child, 
# In the new two classes I put in the brackets the name of the 'father' class. 
# These two classes inherit all the methods of their parents. 

class Student(Person):
    profile = 'Student'

    def __init__(self, name, surmane , age , adress, course):
        super().__init__(name, surmane , age , adress)
        self.course = course  
 
#   Now me make an example of over writing 
    def data(self):
        output_data = f"""
        Profile: {Student.profile}
        Course:{self.course} 
        """
        return super().data() + output_data

    def change_course(self,course):
        self.course = course
        print('New course add')

class Teacher(Person): 
    profile = 'Teachers'

    def __init__(self, name, surmane , age , adress, subjects = None):
        super().__init__(name, surmane , age , adress)
        if subjects is None:
            self.subjects =  ['History', 'Phisics', 'English' ] 
        else:   
            self.subjects = subjects  

     #   Now me make an example of over writing 
    def data(self):
        output_data = f"""
        Profile: {Student.profile}
        Course:{self.subjects} 
        """
        return super().data() + output_data       

    def add_subject(self,new_subjects):
        if new_subjects not in self.subjects: 
            self.subjects.append(new_subjects)
            print('Get new Subject')       




#Istanciate the first Objects 
stud_1 = Student("Mario","Draghi","74","Via fasulla","Phisics") 
print(stud_1.data())
stud_1.change_course('Music')
print(stud_1.data())

#Istanciate the second Objects
tch_1 = Teacher("Cristine", "Lagarde", "66", "Via Bella",["Economics","Phisics"] )
print(tch_1.data())

tch_1.add_subject('Economics 2')
print(tch_1.data())


#Help Function in uefull because you can reach a lot of information about the Class  
print(help(Student)) 

#print(stud_1.data())
#stud_1.data_change()
#print(stud_1.data())

