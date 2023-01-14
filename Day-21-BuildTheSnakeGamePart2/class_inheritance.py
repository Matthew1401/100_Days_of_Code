class Animal:

    def __init__(self):
        self.num_of_eyes = 2
        self.how_to_breathe = "Inhale, exhale."

    def breathe(self):
        print(self.how_to_breathe)


class WaterThing(Animal):

    def __init__(self):
        super().__init__()
        self.speed = 20


class Fish(WaterThing):

    def __init__(self):
        super().__init__()

    def swim(self):
        print("Moving ine the water.")


nemo = Fish()
nemo.breathe()
nemo.swim()
print(nemo.speed)
