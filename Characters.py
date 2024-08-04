from GlobalVariables import getDict

buyPrice = getDict('Item Buy Price')
sellPrice = getDict('Item Sell Price')
unlockPrice = getDict('Item Unlock Price')
itemType = getDict('Item Type')

class Character:
    def __init__(self, xGridPos, yGridPos, facingDirection='Down', balance=0, ):
        #Movement Attributes
        self.x = xGridPos
        self.y = yGridPos
        self.facing = facingDirection

        #Inventory Attributes
        self.purseBalance = balance
        self.inventory = {key: 0 for key in itemType}
        self.hotbar = {key: None for key in range(9)}
        self.heldItem = 0

        #Player Stats
        self.unlocks = {key: False for key in itemType}
        self.itemsFarmed = {key: 0 for key, value in itemType.items() if value in ['Crop', 'Tree Fruit', 'Animal Meat', 'Animal Produce']}
        self.itemsSold = {key: 0 for key in itemType}
        self.itemsBought = {key: 0 for key in itemType}

        
    
    def move(self, dx, dy, detailMap):
        if detailMap[self.x + dx, self.y + dy]%2 == 0: #Check for collision before moving player
            self.x += dx
            self.y += dy

    def pay(self, amount):
        transactionSuccess = False

        if self.purseBalance >= amount:
            self.purseBalance -= amount
            transactionSuccess = True
        
        return transactionSuccess
    
    def shopaction(self, operation, item, quantity=1):
        actionSuccess = False
        function = 'self.' + operation + '("' + item + '")'
        actionSuccess = exec(function)
                
        return actionSuccess
    
    def unlock(self, item):

        if self.unlocks[item]:
            return False
        
        else:
            transactionSuccess = self.pay(unlockPrice[item])
            if transactionSuccess:
                self.unlocks[item] = True

        return transactionSuccess
    
    def buy(self, item, quantity=1):
        transactionSuccess = False
        itemUnlockedBool = self.unlocks[item]

        if (self.purseBalance > buyPrice[item]*quantity) and (itemUnlockedBool):
            self.purseBalance -= buyPrice[item]*quantity
            self.inventory[item] += quantity
            self.itemsBought[item] += quantity
            transactionSuccess = True

        return transactionSuccess
    
    def sell(self, item, quantity=1):
        transactionSuccess = False
        itemUnlockedBool = self.unlocks[item]

        if (self.inventory[item] >= quantity) and (itemUnlockedBool):
            self.purseBalance += sellPrice[item]*quantity
            self.inventory[item] -= quantity
            self.itemsSold[item] += quantity
            transactionSuccess = True

        return transactionSuccess
    
    def loadPlayerData(self, purseState, inventoryState, unlocksState, hotbarState):
        self.purseBalance = purseState
        
        self.inventory = {key: 0 for key in itemType.keys()}
        self.inventory = {key: inventoryState[key] for key in inventoryState.keys()}

        self.unlocks = unlocksState
        self.hotbar = hotbarState