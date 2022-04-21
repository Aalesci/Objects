# Hi Guys, my name is Alberto Alesci I studied economics and finance actually now
# I'm working in Accenture as ABAP developer. But I love 
# mathematics and statistics. 
# 
# I hope this can be useful to find a work in Banks, investment found,
# crypto exchange, in the role of data analist or developer.
# I'm looking for a job with Mathemtics, statistic, pyhton and menage of money.    
# This are simple example about object programmation in Python. 
# I create an object and I explain the different variables.

# Magic methods or dunder methods in Python 
# Magic methods in Python are the special methods that start and end with 
# the double underscores. They are also called dunder methods.
# Magic methods are not meant to be invoked directly by you, but the invocation
# happens internally from the class on a certain action.
# In this example I'll use __str__ and __repr__ .  


class Student:
    Number_of_student = 0

    def __init__(self, name, surmane , age ): 
        self.name = name
        self.surname = surmane
        self.age = age 
        Student.Number_of_student += 1
    
    def personal_data(self):
        return  f""" DATA:\n 
        Nome:{self.name}\n
        Cognome:{self.surname}\n 
        Age:{self.age}\n """


    def __str__(self) :
        #Rappresentation in string of the object, it should be readable and easy. It's made for Public.  
        return f""" The student: Nome:{self.name}, Cognome:{self.surname} """ 
    
    def __repr__(self) :
        #The obbiective of rep is to be Exaustive but not ambiguous. It is oriented for developers. 
        #With this I should able to reproduce the object. 
        return f"""{self.name}','{self.surname}','{self.age} """ 
      

st_1 = Student("Jens","Weidmann", "53") 

print(repr(st_1))




        