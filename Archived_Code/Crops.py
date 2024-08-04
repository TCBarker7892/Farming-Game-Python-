class CropInstance:
    def __int__(self, crop, xPos, yPos, age, growthStage, harvestable):
        self.x = xPos
        self.y = yPos
        self.species = crop
        self.age = age
        self.growthStage = growthStage
        self.harvestable = harvestable
    
    def render(self):
        dummycode = 0

    def harvest(self):
        dummycode = 0

    def dehydrate(self):
        dummycode = 0

    def grow(self):
        dummycode = 0