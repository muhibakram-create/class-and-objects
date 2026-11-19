class car:
    def __init__(self,maxspeed,mileage,color):
        self.maxspeed= maxspeed
        self.mileage = mileage
        self.color = color
Lambo = car(120,60,"yellow")
print("The specifications of lambo")
print("The maxspeed:", Lambo.maxspeed)
print("The mileage:", Lambo.mileage)
print("The color:", Lambo.color)        

