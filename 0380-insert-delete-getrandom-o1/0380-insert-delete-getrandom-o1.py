class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.numToIdx = {}

    def insert(self, val: int) -> bool:
        if val in self.numToIdx:
            return False
        self.nums.append(val)
        self.numToIdx[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.numToIdx:
            return False
        idx = self.numToIdx[val]
        lastVal = self.nums[-1]
        self.nums[idx] = lastVal
        self.numToIdx[lastVal] = idx
        self.nums.pop()
        del self.numToIdx[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()