from collections import Counter
import math
import matplotlib
import random
import statistics

#%matplotlib inline

class Coin:

    def __init__(self):
        self.side = side

class FlipSet:

    def __init__(self, n):
        self.flip_list = []
        self.total_number_of_flips = 2 ** n


    def flip_coin(self):
        total_number_of_flips = 2**10
        for n in range(self.total_number_of_flips):
            self.flip_list.append(random.choice(['heads','tails']))
        print(len(self.flip_list))


    def find_diff_heads_tails(self):
        print("******")
        print(self.flip_list)
        ht_counter = Counter(self.flip_list)
        print(ht_counter)
        ht_diff = ht_counter['heads'] - ht_counter['tails']
        return ht_diff

    def find_ratio_heads_tails(self):
        ht_counter = Counter(self.flip_list)
        ht_ratio = ht_counter['heads'] / ht_counter['tails']


if __name__ == '__main__':
    flipset = FlipSet(3)
    flipset.flip_coin()
    ht_diff = flipset.find_diff_heads_tails()
    ht_ratio = flipset.find_ratio_heads_tails()
    print(ht_diff)
    print(ht_ratio)





