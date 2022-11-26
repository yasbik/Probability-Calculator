import copy
import random
# Consider using the modules imported above.

class Hat:

    # initialize the hat object with a variable number of arguments
    def __init__(self, **balls):
        
        # list of the contents
        self.contents = list()

        #add each ball to the list
        for ball, quantity in balls.items():
            while quantity > 0:
                self.contents.append(ball)
                quantity -= 1
        


    # method to draw a ball from the had
    def draw(self, number_of_draws):

        balls_drawn = list()

        # if there are fewer balls in the had than the number of balls needed to be drawn
        if number_of_draws > len(self.contents):
            # the entire contents of the hat is returned
            balls_drawn = self.contents.copy()
            # the hat is emptied
            self.contents.clear()
            return balls_drawn
        
        # keep drawing until the required number of draws is reached
        while number_of_draws > 0:
            # create a random number within the range of the hat contents
            random_num = random.randint(0, (len(self.contents) - 1))
            # draw a ball and add it to the list
            balls_drawn.append(self.contents[random_num])
            # remove the drawn ball from the hat
            del self.contents[random_num]
            number_of_draws -= 1
        
        return balls_drawn
    

# function to create an experiment to calculate probabilities of sets of draws
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    # the balls we are looking to get
    balls_needed = list()
    # the balls that are drawn randomly
    balls_drawn = list()

    # variables to calculate probability
    matches = 0
    total_experiments = num_experiments

    # add the balls we are looking to get to the list
    for ball, quantity in expected_balls.items():
        while quantity > 0:
            balls_needed.append(ball)
            quantity -= 1
    
    length_expected = len(balls_needed)
    
    # run the experiment as many times as required
    while num_experiments > 0:

        # create a deep copy of the hat object so that the original object is not altered
        newHat = copy.deepcopy(hat)

        # draw a random set of balls
        balls_drawn = newHat.draw(num_balls_drawn)

        i = 0
        hit = 0

        # match the set of balls needed to the set of balls drawn
        while i < length_expected:
            if balls_needed[i] in balls_drawn:
                balls_drawn.remove(balls_needed[i])
                hit += 1
            i += 1
        
        # calculate how many times they matched
        if hit == len(balls_needed):
            matches += 1
        
        num_experiments -= 1
    
    # return the probability
    return matches / total_experiments
            

