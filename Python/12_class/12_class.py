class human:
    def __init__(self,n,o):
        self.name = n
        self.occupation = o

    def do_work(self):
        if self.occupation == "tennis player":
            print(self.name,"play tennis")
        elif self.occupation == "actor":
            print(self.name,"do acting for film")
        elif self.occupation == "student":
            print(self.name,"is a student")

    def speaks(self):
        print(self.name,"is saying Hello!!")

    
mohit = human("mohit rohda","student")
mohit.do_work()
mohit.speaks()

