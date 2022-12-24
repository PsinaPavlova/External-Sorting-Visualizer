import random
from NaturalMergeSorting import Natural_Merge_Sort
from BalancedMergeSorting import Balanced_Merge_Sort
from PolyphaseMergeSorting import PolyphaseMergeSort
import matplotlib.pyplot as plt

def AvgTime(func, x, data):

    data = random.sample(range(x), x)
    sum = 0
    for i in range(10):
        with open('mainLine.txt', 'w') as mainLine:
            for j in data:
                mainLine.write('%s\n' % j)
        if func==Balanced_Merge_Sort:
            sum += func(x)
        else:
            sum += func()
    return sum/10


def AlgoritmSortingComaparasion(data):
    plt.clf()
    Length = [100, 300, 500, 800, 1000]#, 2000, 5000, 10000]

    Natural_Merge_SortTimes = [AvgTime(Natural_Merge_Sort, x, data) for x in Length]
    Balanced_Merge_SortTimes = [AvgTime(Balanced_Merge_Sort, x, data) for x in Length]
    # BuiltInSortTimes = [AvgTime(measurebuiltInSortTime, x) for x in Length]

    plt.plot(Length, Natural_Merge_SortTimes, color='r')
    plt.plot(Length, Balanced_Merge_SortTimes, color='b')
    # plt.plot(Length, BuiltInSortTimes, color='g')

    plt.title(label="Sort algoritms comparasion\nNatural_Merge_Sort - red | Balanced_Merge_Sort - blue", fontsize=12)
    plt.xlabel("List length")
    plt.ylabel("Time (seconds)")

    # plt.annotate("max BuiltInSort Time = " + str(float("{0:.6f}".format(BuiltInSortTimes[4]))), xy=(
    #     0, Natural_Merge_SortTimes[4]+0.3))
    # plt.annotate("max Natural_Merge_Sort Time = " + str(float("{0:.6f}".format(Natural_Merge_SortTimes[4]))), xy=(
    #     0, Natural_Merge_SortTimes[4]+0.4))
    # plt.annotate("max Balanced_Merge_Sort Time = " + str(float("{0:.6f}".format(Balanced_Merge_SortTimes[4]))), xy=(
    #     0, Natural_Merge_SortTimes[4]+0.5))

    plt.show()