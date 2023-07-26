#Create a "Person" class

#that has a name("name") and a age("age")

class person:
    def __init__(self,name, age ):
        self.name = name
        self.age = age 


p1 = person('ali',16)

print(p1.name )
print(p1.age)