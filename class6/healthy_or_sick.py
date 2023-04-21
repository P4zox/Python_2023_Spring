# The Person's state
class Person:
    state="healthy" #state elements: not object
    # Instance method
    def getCold(self):
        self.__class__.state="sick"
    def getRecovered(self):
        self.__class__.state="healthy"

print("Original State:" + str(Person.state))
man=Person()
man.getCold()
print("State now:"+str(Person.state))