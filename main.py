from random import sample
from NaturalMergeSorting import Natural_Merge_Sort
from BalancedMergeSorting import Balanced_Merge_Sort
from PolyphaseMergeSorting import PolyphaseMergeSort
# algorithms = {'1': InsertionSort,
#               '2': quickSort}

# alg = input(
#     'Select the algorithm(1 for Natural Merge Sort, 2 for QuickSort using Random Pivoting):')
# if alg not in algorithms:
#     alg = '1'

data_size = 500
data = sample(range(data_size), data_size)


with open('mainLine.txt', 'w') as mainLine:
    for i in data:
        mainLine.write('%s\n' % i)


Natural_Merge_Sort()
