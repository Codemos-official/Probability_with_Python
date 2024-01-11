import random

class Game:

    # constructor
    def __init__(self):
        self.dice = 0
        self.coins = 0

    # add dice and coin
    def add_dice(self):
        self.dice += 1
    def add_coin(self):
        self.coins += 1
    
    # to find the current count of dice and coin
    def dice_count(self):
        return self.dice
    def coin_count(self):
        return self.coins
    
    # roll dice and get a random output
    def roll_dice(self):
        result = []
        for i in range(self.dice):
            result.append( random.randint(1, 6) )
        return result

    # toss coin and get a random output
    def toss_coins(self):
        result = []
        for j in range(self.coins):
            result.append( random.choice( ['Heads', 'Tails'] ) )
        return result
    
    # rolling dice and tossing coin at the same time
    def dice_and_coins(self):
        return self.roll_dice() + self.toss_coins()


# creating object of Game class.
game = Game()

# Add two dice and three coins
game.add_dice()
game.add_dice()

game.add_coin()
game.add_coin()
game.add_coin()


# total count of die and coin
print("die",   game.dice_count())
print( 'coin' , game.coin_count())



# Roll all dice and toss all coins
dice_results = game.roll_dice()
coin_results = game.toss_coins()
dice_and_coin = game.dice_and_coins()

# Display the results
print(f"Dice results: {dice_results}")
print(f"Coin results: {coin_results}")
print(f"both results: {dice_and_coin}")

