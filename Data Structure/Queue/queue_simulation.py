from queue import Queue
import random

class QueueSimulation:
    def __init__(self,process_rate,min_req_rate,max_req_rate,capacity):
        self.process_rate = process_rate
        self.min_req_rate = min_req_rate
        self.max_req_rate = max_req_rate
        self.queue = Queue(capacity)

    def step(self,requests):
        process = []
        lost_count = 0
        remain = self.process_rate
        while not self.queue.is_empty() and remain > 0:
            process.append(self.queue.remove())
            remain -= 1

        for item in requests:
            if remain > 0:
                process.append(item)
                remain -= 1
            else:
                if not self.queue.is_full():
                    self.queue.insert(item)
                else:
                    lost_count += 1
        return process, lost_count

    def run(self,iteration):
        lost_count = 0
        for i in range(iteration):
            requests = ["A" for i in range(random.randint(self.min_req_rate,self.max_req_rate))]
            lost_count += self.step(requests)[1]
        return lost_count/iteration

            

sim = QueueSimulation(5, 4, 7, 2)
assert(hasattr(sim, "process_rate"))
assert(hasattr(sim, "min_req_rate"))
assert(hasattr(sim, "max_req_rate"))
assert(hasattr(sim, "step"))

requests = ["A", "B", "C", "D"]
results, lost_count = sim.step(requests)
assert(results == ["A", "B", "C", "D"])
assert(lost_count == 0)

results, lost_count = sim.step(["E", "F", "G", "H", "I", "K"])
assert(results == ["E", "F", "G", "H", "I"])
assert(lost_count == 0)

results, lost_count = sim.step(["L", "M", "N", "O", "P", "Q"])
assert(results == ["K", "L", "M", "N", "O"])
assert(lost_count == 0)

results, lost_count = sim.step(["R", "S"])
assert(results == ["P", "Q", "R", "S"])
assert(lost_count == 0)

results, lost_count = sim.step(["T", "U", "V", "W", "X", "Y"])
assert(results == ["T", "U", "V", "W", "X"])
assert(lost_count == 0)

results, lost_count = sim.step(["Z", "0", "1", "2", "3", "4", "5"])
assert(results == ["Y", "Z", "0", "1", "2"])
assert(lost_count == 1)

results, lost_count = sim.step(["6", "7", "8", "9", "10", "11", "12", "13"])
assert(results == ["3", "4", "6", "7", "8"])
assert(lost_count == 3)

lost_requests_rate = sim.run(100000)
print(lost_requests_rate)
assert(lost_requests_rate < 0.6)