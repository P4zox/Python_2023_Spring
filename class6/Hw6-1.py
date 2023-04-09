class Lesson:
    # Constructor
    def __init__(self,teacher,days):
        self.teacher=teacher
        self.days=days

    @classmethod
    def t1(cls):
        return cls("Emma","Monday")
    @classmethod
    def t2(cls):
        return cls("Peter","Thursday")
    
    def intro(self):
        print("This lesson was taught by {} on {}".format(self.teacher,self.days))

emma=Lesson.t1()
peter=Lesson.t2()
emma.intro()
peter.intro()

