import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **balls):
        
        self.contents = list()

        for ball, quantity in balls.items():
            while quantity > 0:
                self.contents.append(ball)
                quantity -= 1
        

    def draw(self, number_of_draws):
        # print("Entered draw function!")
        # print(self.contents)
        newList = self.contents.copy()
        balls_drawn = list()

        if number_of_draws > len(self.contents):
            balls_drawn = newList.copy()
            newList.clear()
            return balls_drawn
        
        while number_of_draws > 0:
            random_num = random.randint(0, (len(newList) - 1))
            balls_drawn.append(newList[random_num])
            del newList[random_num]
            number_of_draws -= 1
        
        # print("Balls drawn = " + str(balls_drawn))
        return balls_drawn
    


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    balls_needed = list()
    balls_drawn = list()
    matches = 0
    total_experiments = num_experiments

    for ball, quantity in expected_balls.items():
        while quantity > 0:
            balls_needed.append(ball)
            quantity -= 1
    
    length_expected = len(balls_needed)

    # print("Needed = " + str(balls_needed))
    
    while num_experiments > 0:
        # print("\nExperiment = " + str(num_experiments))
        # print("Number of draws = " + str(num_balls_drawn))
        balls_drawn = hat.draw(num_balls_drawn)

        i = 0
        hit = 0
        while i < length_expected:
            # print("i = " + str(i) + "          Needed = " + str(balls_needed) + "          Balls drawn = " + str(balls_drawn))
            if balls_needed[i] in balls_drawn:
                balls_drawn.remove(balls_needed[i])
                hit += 1
            i += 1
        
        if hit == len(balls_needed):
            matches += 1
        
        num_experiments -= 1
    
    return matches / total_experiments
            

