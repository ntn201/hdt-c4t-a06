class Counter:
    def __init__(self):
        self.count = 0
        # property
    

    # method
    def tick(self):
        self.count += 1


# instance/ object
# counter = Counter()
# counter.tick()
# counter.tick()
# print(counter.count)

class Dog:
    def __init__(self,name,age,breed,weight):
        self.name = name
        self.age = age
        self.breed = breed
        self.weight = weight
    
    def eat(self):
        self.weight += 0.
        
# byn = Dog("Byn",5,"Corgi",5)

# print(byn.name)
# print(byn.age)
# print(byn.breed)

# byn.eat()
# print(byn.weight)



class Clock:
    def __init__(self,hours,minutes,seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds)

    def display(self):
        print(self.hours,":",self.minutes,":",self.seconds,sep="")

    def tick(self):
        pass

clock = Clock(2,5,9)
clock.display()
print(clock)