import random
class RandomizedSet(object):

    def __init__(self):
        self.randomizedset = []

    def insert(self, val):
        if val in self.randomizedset:
            return False
        else:
            self.randomizedset.append(val)
            return True
        

    def remove(self, val):
        if val in self.randomizedset:
            self.randomizedset.remove(val)
            return True
        else:
            return False
        

    def getRandom(self):
        return random.choice(self.randomizedset)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()