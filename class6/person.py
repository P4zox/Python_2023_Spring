class Person:
    # Consructor
    def __init__(self,name,age,favorite_food):
        self.name=name
        self.age=age
        self.favorite_food=favorite_food

    # add method
    def introduce(self):
        print("Hi, I am "+str(self.name)+", I am "+str(self.age)+" years old, I like to consume "+str(self.favorite_food)+".")

    def shout(self, info):
        print("Shout: \"" + str(info) + "!\"")

# create object
man=Person("Jake",11,"cookie")
# call method
man.introduce()
man.shout("I love to be rickroll")