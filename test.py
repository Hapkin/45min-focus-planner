


    

class Animal():
    def __init__(self, name):
        self.name=name
    
    def walk(self):
        return f"{self.name} is walking"
        
        

class Dog(Animal):
    def __init__(self,name, legs):
        super().__init__(name)
        #property name is now set via the Animal class
        self.legs=legs
    def walk(self):
        walking=super().walk()
        walking+=f" on {self.legs} legs"
        return walking
    
class Snake(Animal):
    def __init__(self,name):
        super().__init__(name)
        #property name is now set via the Animal class
        self.legs=legs
    def walk(self):
        walking=super().walk
        walking+=f" on {self.legs} legs"
        return walking




class MainApp():
    my_dog=Dog("Barf",4)
    print(my_dog.walk())


# run the App.
if __name__=='__main__':
    MainApp()