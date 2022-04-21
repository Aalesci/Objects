# Hi Guys, my name is Alberto Alesci I studied economics and finance actually now
# I'm working in Accenture as ABAP developer. But I love 
# mathematics and statistics. 
# 
# I hope this can be useful to find a work in Banks, investment found,
# crypto exchange, in the role of data analist or developer.  
# This are simple example about object programmation in Python. 
# I create an object and I explain the different variables.

#We get from the previous script (Object_first_script.py and Object_second_script.py)
# the three different classes. We now are goig to implement class methods and static method. 


# @CLASS METHOD AND @STATIC METHOD 
# A Class Method is a method that is bound to a class rather than its object. 
# It doesn't require creation of a class instance, much like static method.
# The difference between a static method and a class method is: Static method knows 
# nothing about the class and just deals with the parameters. 


class Person:

    def __init__(self, name, surmane , age , adress ):
        self.name = name
        self.surname = surmane
        self.age = age 
        self.adress = adress 

    #Here is the Class method. I use it to create another way for istanciate the object. 
    # I want to istanciate it with Berlisoni = Silvio-Berlusconi-86-Arcore
    @classmethod   #It si use to create the Class method  (Decorator)
    def costructor_from_string(cls, stringa, *args):
        name, surmane , age , adress = stringa.split("-")
        return cls(name, surmane , age , adress, *args)
    #Note *args It is used to allow the 'Passages' of other data.

    #Instead of accepting a self parameter, class methods take a cls parameter that points to the class—and 
    # not the object instance—when the method is called.
    @classmethod
    def occupation(cls):
        return cls.__name__   

    #A static method can neither modify object state nor class state. 
    @staticmethod
    def info( ):      
        info = '''
        Program : Object_third_script.py
        Created by: Albeto Alesci
        Python Version: 3.6  
        '''
        return info 


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



class Student(Person):
    profile = 'Student'

    def __init__(self, name, surmane , age , adress, course):
        super().__init__(name, surmane , age , adress)
        self.course = course  
  
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


string_p = "Silvio-Berlusconi-86-Arcore"
P1 = Person.costructor_from_string(string_p)
print(P1.data())

string_s = "Romano-Prodi-74-Via Bella"
S1 = Student.costructor_from_string( string_s, 'Economics' )
print(S1.data())

#to get the name of the class: 
print(P1.occupation())    #--> Person 
print(S1.occupation())    #--> Student 


# The three Concept to pick up are 
# Instance Methods (init + self)
# Class Methods   (@ClassMethod + cls )
# Static Methods  (@StaticMethod )

