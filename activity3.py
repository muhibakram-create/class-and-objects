class parrot:
    species= "bird"
    def __init__(self,name,color,age):
        self.name = name
        self.color = color
        self.age = age
bluey = parrot("Bluey","blue",1.5)
twinkle = parrot("Twinkle","Yellow",2)
print("{} is {} {}. He is {} years old.".format(bluey.name,bluey.color,bluey.species,bluey.age))
print("{} is {} {}. He is {} years old.".format(twinkle.name,twinkle.color,twinkle.species,twinkle.age))
