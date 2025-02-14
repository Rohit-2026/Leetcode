class ProductOfNumbers:
    def __init__(self):
        self.pref_prod = [1] # stores product of all previous nums

    def add(self, num: int):
        if num == 0:
            self.pref_prod = [1]
        else:
            self.pref_prod.append(self.pref_prod[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.pref_prod): 
            return 0 

        return self.pref_prod[-1] // self.pref_prod[-k - 1]