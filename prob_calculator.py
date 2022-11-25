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
        balls_drawn = list()

        if number_of_draws > len(self.contents):
            balls_drawn = self.contents.copy()
            self.contents.clear()
            return balls_drawn
        
        while number_of_draws > 0:
            random_num = random.randint(0, (number_of_draws - 1))
            balls_drawn.append(self.contents[random_num])
            del self.contents[random_num]
            number_of_draws -= 1
        
        return balls_drawn
    


#def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
