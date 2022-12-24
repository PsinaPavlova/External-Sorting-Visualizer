from random import sample
from NaturalMergeSorting import Natural_Merge_Sort
from BalancedMergeSorting import Balanced_Merge_Sort
from PolyphaseMergeSorting import PolyphaseMergeSort
from NaturalMergeSorting import Natural_Merge_Sort_Animate
from BalancedMergeSorting import Balanced_Merge_Sort_Animate
from Animate import Show_Animation
from Test import AlgoritmSortingComaparasion
algorithms = {'1','2'}



try:
    data_size = int(input('Data size(defaut 20):'))
except ValueError:
    data_size = 20

data = sample(range(data_size), data_size)


with open('mainLine.txt', 'w') as mainLine:
    for i in data:
        mainLine.write('%s\n' % i)

print("Time spent on Natural_Merge_Sort: ", Natural_Merge_Sort())
with open('mainLine.txt', 'w') as mainLine:
    for i in data:
        mainLine.write('%s\n' % i)
print("Time spent on Balanced_Merge_Sort: ", Balanced_Merge_Sort(data_size))

DoShow = input("Do u want to see Animation? [y/n]")

if DoShow != 'y' or DoShow != 'n':
    DoShow=='n'
with open('mainLine.txt', 'w') as mainLine:
    for i in data:
        mainLine.write('%s\n' % i)
if DoShow == 'y':
    alg = input(
        'Select the algorithm(1 for Natural_Merge_Sort, 2 for Balanced_Merge_Sort):')
    if alg not in algorithms:
        alg = '1'
    if alg=='1':
        Natural_Merge_Sort_Animate()
    else:
        Balanced_Merge_Sort_Animate(data_size)
    Show_Animation(500)

DoShow = input("Do u want to see Graphs? [y/n]")
if DoShow != 'y' or DoShow != 'n':
    DoShow=='n'
if DoShow:
    AlgoritmSortingComaparasion(data)



