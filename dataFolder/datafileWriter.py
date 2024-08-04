import os

class Item:

     itemList = []

     def __init__(self, name, itemType, buyPrice, sellPrice, unlockPrice):
          self.name = name
          self.itemType = itemType
          self.buyPrice = buyPrice
          self.sellPrice = sellPrice
          self.unlockPrice = unlockPrice
          Item.itemList.append(self)
     
     def infoString(self):
          info = [self.name, self.itemType, str(self.buyPrice), str(self.sellPrice), str(self.unlockPrice)]
          infoToString = ','.join(info) + '\n'
          return infoToString

#Crop Items
Carrot = Item('Carrot', 'Crop Produce', None, 2, 1000)
Potato = Item('Potato', 'Crop Produce', None, 4, 1000)
Wheat = Item('Wheat', 'Crop Produce', None, 6, 1000)
Beetroot = Item('Beetroot', 'Crop Produce', None, 8, 1000)
Melon = Item('Melon', 'Crop Produce', None, 10, 1000)
Bamboo = Item('Bamboo', 'Crop Produce', None, 12, 1000)
CarrotSeed = Item('Carrot Seed', 'Crop Seed', 1, None, None)
PotatoSeed = Item('Seed Potato', 'Crop Seed', 2, None, None)
WheatSeed = Item('Wheat Seed', 'Crop Seed', 3, None, None)
BeetrootSeed = Item('Beetroot Seed', 'Crop Seed', 4, None, None)
MelonSeed = Item('Melon Seed', 'Crop Seed', 5, None, None)
BambooSeed = Item('Bamboo Sprout', 'Crop Seed', 6, None, None)

#Tree Items
Cherry = Item('Cherry', 'Tree Fruit', None, 15, 5000)
Apple = Item('Apple', 'Tree Fruit', None, 20, 5000)
CherrySapling = Item('Cherry Sapling', 'Tree Sapling', 50, None, None)
AppleSapling = Item('Apple Sapling', 'Tree Sapling', 100, None, None)

#Animal Items
Chicken = Item('Chicken', 'Mature Animal', None, 400, 10000)
Goat = Item('Goat', 'Mature Animal', None, 600, 10000)
Pig = Item('Pig', 'Mature Animal', None, 800, 10000)
Sheep = Item('Sheep', 'Mature Animal', None, 1000, 10000)
Cow = Item('Cow', 'Mature Animal', None, 1200, 10000)
BabyChicken = Item('Baby Chicken', 'Baby Animal', 200, 100, None)
BabyGoat = Item('Baby Goat', 'Baby Animal', 300, 150, None)
BabyPig = Item('Baby Pig', 'Baby Animal', 400, 200, None)
BabySheep = Item('Baby Sheep', 'Baby Animal', 500, 250, None)
BabyCow = Item('Baby Cow', 'Baby Animal', 600, 300, None)
ChickenMeat = Item('Raw Chicken', 'Animal Meat', None, 300, None)
GoatMeat = Item('Raw Goat', 'Animal Meat', None, 450, None)
Pork = Item('Pork', 'Animal Meat', None, 600, None)
Mutton = Item('Mutton', 'Animal Meat', None, 750, None)
Beef = Item('Beef', 'Animal Meat', None, 900, None)
Egg = Item('Egg', 'Animal Produce', None, 50, None)
GoatsMilk = Item('Goats Milk', 'Animal Produce', None, 80, None)
Truffle = Item('Truffle', 'Animal Produce', None, 100, None)
Wool = Item('Wool', 'Animal Produce', None, 120, None)
CowsMilk = Item('Cows Milk', 'Animal Produce', None, 150, None)

#Decoration Items
Fence = Item('Fence', 'Decoration', 50, 50, 1000)
Sign = Item('Sign', 'Decoration', 50, 50, 1000)
StonePath = Item('Stone Path', 'Decoration', 50, 50, 1000)

#Base Materials (implement gathering later)
WoodLog = Item('Wood Log', 'Base Material', None, 20, None)
Stone = Item('Stone', 'Base Material', None, 20, None)

#Processed Items (implement crafting later)
FetaCheese = Item('Feta Cheese', 'Processed Item', None, 200, None)
Cheddar = Item('Cheddar Cheese', 'Processed Item', None, 300, None)
WoodenPlank = Item('Wooden Plank', 'Processed Item', None, 50, None)

def write_itemData(location):
     with open(os.path.join(location, 'itemData.txt'), 'w') as f:
          for itemInstance in Item.itemList:
               f.write(itemInstance.infoString())

class CropData:

     cropDataList = []

     def __init__(self, name, seedName, growTime, dehydrateTime):
          self.name = name
          self.seedName = seedName
          self.growTime = growTime
          self.dehydrateTime = dehydrateTime
          CropData.cropDataList.append(self)

     def infoString(self):
          info = [self.name, self.seedName, str(self.growTime), str(self.dehydrateTime)]
          infoToString = ','.join(info) + '\n'
          return infoToString
     
#Crop Species
CarrotSpecies = CropData('Carrot', 'Carrot Seed', 60, 30)
PotatoSpecies = CropData('Potato', 'Seed Potato', 120, 30)
WheatSpecies = CropData('Wheat', 'Wheat Seed', 240, 30)
BeetrootSpecies = CropData('Beetroot', 'Beetroot Seed', 300, 30)
MelonSpecies = CropData('Melon', 'Melon Seed', 480, 30)
BambooSpecies = CropData('Bamboo', 'Bamboo Sprout', 600, 30)

class TreeData:

     treeDataList = []

     def __init__(self, name, saplingName, growTime, fruitTime):
          self.name = name
          self.saplingName = saplingName
          self.growTime = growTime
          self.fruitTime = fruitTime
          TreeData.treeDataList.append(self)

     def infoString(self):
          info = [self.name, self.saplingName, str(self.growTime), str(self.fruitTime)]
          infoToString = ','.join(info) + '\n'
          return infoToString
     
#Tree Species
CherrySpecies = TreeData('Cherry', 'Cherry Sapling', 300, 60)
AppleSpecies = TreeData('Apple', 'Apple Sapling', 300, 60)
     
class AnimalData:

     animalDataList = []

     def __init__(self, name, babyName, produceName, meatName, matureTime, produceTime):
          self.name = name
          self.babyName = babyName
          self.produceName = produceName
          self.meatName = meatName
          self.matureTime = matureTime
          self.produceTime = produceTime
          AnimalData.animalDataList.append(self)

     def infoString(self):
          info = [self.name, self.babyName, self.produceName, self.meatName, str(self.matureTime), str(self.produceTime)]
          infoToString = ','.join(info) + '\n'
          return infoToString

#Animal Species
ChickenSpecies = AnimalData('Chicken', 'Baby Chicken', 'Egg', 'Raw Chicken', 180, 120)
GoatSpecies = AnimalData('Goat', 'Baby Goat', 'Goats Milk', 'Raw Goat', 300, 120)
PigSpecies = AnimalData('Pig', 'Baby Pig', 'Truffle', 'Pork', 480, 120)
SheepSpecies = AnimalData('Sheep', 'Baby Sheep', 'Wool', 'Mutton', 600, 120)
CowSpecies = AnimalData('Cow', 'Baby Cow', 'Cows Milk', 'Beef', 900, 120)

def write_cropData(location):
     with open(os.path.join(location, 'cropData.txt'), 'w') as f:
          for cropInstance in CropData.cropDataList:
               f.write(cropInstance.infoString())

def write_treeData(location):
     with open(os.path.join(location, 'treeData.txt'), 'w') as f:
          for treeInstance in TreeData.treeDataList:
               f.write(treeInstance.infoString())

def write_animalData(location):
     with open(os.path.join(location, 'animalData.txt'), 'w') as f:
          for animalInstance in AnimalData.animalDataList:
               f.write(animalInstance.infoString())


thisDirectory = os.path.dirname(__file__)
dataFolderLocation = thisDirectory
speciesFolderLocation = os.path.join(dataFolderLocation, 'speciesData')
if not os.path.exists(speciesFolderLocation):
     os.makedirs(speciesFolderLocation)

write_itemData(dataFolderLocation)
write_cropData(speciesFolderLocation)
write_treeData(speciesFolderLocation)
write_animalData(speciesFolderLocation)