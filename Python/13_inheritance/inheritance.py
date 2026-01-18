class vehicle:
    def general_usage(self):
        print("general usage : Transportation")

class car(vehicle):
    def __init__(self):
        print("i am a car")
        self.wheels = 4
        self.has_roof = True   

    def specific_usage(self):
        self.general_usage()
        print("Use for commute to work and family vcation")

class motor_cycle(vehicle):
    def __init__(self):
        print("i am a bike")
        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):
        self.general_usage()
        print("Use for riding and racing")
        

c = car()
c.specific_usage()

m = motor_cycle()
m.specific_usage()

