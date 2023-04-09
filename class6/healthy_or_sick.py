class Person:
    state="healthy"
    def getCold(self):
        self.__class__.state="sick"
    def getRecovered(self):
        self.__class__.state="healthy"

print("State:" + str(Person.state))
man=Person()
man.getCold()
print("State now:"+str(Person.state))