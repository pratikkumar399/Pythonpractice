# create a class name as student specify variables like students strength course duration , course name ,university name , etc
#create object of the class , object name will be obj , then create some methods like getdata to take all the data from the user based on the user input and then display all the information by using display method.
#2 . Demonstarte the use of static method , class method in python
# 3. How to declare public and private variables in python . Write a program to print such values which are public and private .

class Student:
    
    def get_data(self,strength,course_duration , course_name , university_name ):
        self.strength =strength
        self.course_duration = course_duration 
        self.course_name = course_name
        self.university_name =university_name
    def display_data(self):
        print(f"The strength of the class {self.strength}")
        print(f"The course duration is {self.course_duration}")
        print(f"The course name is {self.course_name}")
        print(f"The univeristy name is {self.university_name}")
        
obj =Student()
obj.get_data(10,4 , "CSE" ,"Chandigarh University" )
obj.display_data()
