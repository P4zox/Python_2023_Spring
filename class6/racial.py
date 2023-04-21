class Person:
    # 建構式
    def __init__(self,eyeColor,hairColor):
        self.eyeColor=eyeColor
        self.hairColor=hairColor
    # American
    @classmethod
    def American(cls):
        return cls("rainbow","brown")
    # Asian
    @classmethod
    def Asia(cls):
        return cls("black","black")
    
    def introduce(self):
        print("My eyes are "+ self.eyeColor+" and my hair is "+self.hairColor+".")

American=Person.American()
Asia=Person.Asia()
American.introduce()
Asia.introduce()