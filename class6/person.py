class Person:
    def __init__(self,name,age,favorite_food):
        self.name=name
        self.age=age
        self.favorite_food=favorite_food

    def introduce(self):
        print("Hi, I am "+str(self.name)+", I am "+str(self.age)+", I like to consume "+str(self.favorite_food)+".")

    def shout(self, info):
        print("Shout: \"" + str(info) + "!\"")

man=Person("Jake",11,"cookie")
man.introduce()
man.shout("I love to be rickroll")