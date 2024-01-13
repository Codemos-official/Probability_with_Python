'''
Probability Event:- A probability event refers to a specific outcome or set of outcomes that can occur in a random experiment or situation. In probability theory, an event is typically denoted by a set of possible outcomes, and the probability of an event is a measure of the likelihood that the event will occur.
'''

# Program to calculate the probability of the event of a specific outcome on rolling a dice and choosing a ball from the box.

import random

# PEC = Probability Event Class
class PEC:
    def __init__(self):
        pass

    def roll_dice(self):
        return random.randint(1,6)

    def probability_event_dice(self, event, total_throw=1000):
        favorable_outcomes = 0

        for i in range(total_throw):
            outcome = self.roll_dice()
            if outcome in event:
                favorable_outcomes += 1

        # Calculate and display the probability of the event
        probability = favorable_outcomes / total_throw
        
        print("Number of favorable outcomes: ", favorable_outcomes)
        print("Total number of trials: ",total_throw)
        print("Probability of the event: ",probability)

    # Function to choose a random ball from a box
    def draw_ball(self):
        colors = ['black', 'red', 'white']
        return random.choice(colors)
        
    def probability_event_ball(self,event,total_throw = 1000):
        favorable_outcomes_ball = 0
        
        for _ in range(total_throw):
            ball_color = self.draw_ball()
            if ball_color in event_ball:
                favorable_outcomes_ball += 1
        
        # Calculate and display the probability of the event
        probability = favorable_outcomes_ball / total_throw
        
        print("Number of favorable outcomes: ",favorable_outcomes_ball)
        print(f"Total number of trials: ", total_throw)
        print(f"Probability of the event :", probability)        


# main function
if __name__ == "__main__":
    obj = PEC()

    # Event 1: Rolling an even number in dice
    event_dice = [2, 4, 6]
    print("Event 1: Rolling an even number from dice")
    obj.probability_event_dice(event_dice)

    # Event 2: Choosing a red ball from the box
    event_ball = ['red']
    print("\nEvent 2: Choosing a red ball from the box")
    obj.probability_event_ball(event_ball)
    

