import random

class Simulation:
    def __init__(self,process_rate,min_req_rate,max_req_rate):
        self.process_rate = process_rate
        self.min_req_rate = min_req_rate
        self.max_req_rate = max_req_rate

    def run(self,iteration):
        lost_count = 0
        for i in range(iteration):
            requests = random.randint(self.min_req_rate,self.max_req_rate)
            if requests > self.process_rate:
                lost_count += requests - self.process_rate
        return lost_count/iteration
