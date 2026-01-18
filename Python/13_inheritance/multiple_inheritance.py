'''
class father:
    def gardening(self):
        print("i enjoy gardening")

class mother:
    def cooking(self):
        print("i enjoy cooking")

class child(father,mother):
    def sport(self):
        print("i enjoy sport")

c = child()
c.sport()
c.cooking()
c.gardening()

'''
class father:
    def skill(self):
        print("i enjoy gardening")

class mother:
    def skill(self):
        print("i enjoy cooking")

class child(father,mother):
    def skill(self):
        father.skill(self)
        mother.skill(self)
        print("i enjoy sport")

c = child()
c.skill()