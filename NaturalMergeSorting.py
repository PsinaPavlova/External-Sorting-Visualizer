import os
from Animate import readAndAnimate
import time

def read_next_number(file):

    num_str = file.readline()
    if num_str != "`\n" and num_str != '':
        num = int(num_str.replace("\n", ""))
        return num
    return None


def listSplit():
    Switch = True
    with open('buf1.txt', 'w') as firstBuffer, open('buf2.txt', 'w') as secondBuffer, open('mainLine.txt', 'r') as mainLine:
        num = read_next_number(mainLine)
        temp = num

        while num is not None:
            num = read_next_number(mainLine)
            if num is None:
                if Switch:
                    firstBuffer.write('%s\n' % temp)
                else:
                    secondBuffer.write('%s\n' % temp)
                break

            if Switch:
                firstBuffer.write('%s\n' % temp)
                if temp > num:
                    Switch = False
            else:
                secondBuffer.write('%s\n' % temp)
                if temp > num:
                    Switch = True
            temp = num


def Merge():

    with open('buf1.txt', 'r') as firstBuffer, open('buf2.txt', 'r') as secondBuffer, open('mainLine.txt', 'w') as mainLine:
        bufNum1 = read_next_number(firstBuffer)
        bufNum2 = read_next_number(secondBuffer)

        while bufNum1 is not None and bufNum2 is not None:
            if bufNum1 <= bufNum2:
                mainLine.write('%s\n' % bufNum1)
                bufNum1 = read_next_number(firstBuffer)
            else:
                mainLine.write('%s\n' % bufNum2)
                bufNum2 = read_next_number(secondBuffer)

        while bufNum1 is not None:
            mainLine.write('%s\n' % bufNum1)
            bufNum1 = read_next_number(firstBuffer)

        while bufNum2 is not None:
            mainLine.write('%s\n' % bufNum2)
            bufNum2 = read_next_number(secondBuffer)


def Natural_Merge_Sort():
    start = time.time()
    while True:
        listSplit()
        if os.stat("buf2.txt").st_size == 0:
            break
        Merge()
    return time.time() - start

#-----------------------------------------------------------------Animate


def Natural_Merge_Sort_Animate():
    while True:
        listSplit_Animate()
        if os.stat("buf2.txt").st_size == 0:
            break
        Merge_Animate()

def listSplit_Animate():
    Switch = True
    with open('buf1.txt', 'w') as firstBuffer, open('buf2.txt', 'w') as secondBuffer, open('mainLine.txt', 'r') as mainLine:
        num = read_next_number(mainLine)
        temp = num

        while num is not None:
            num = read_next_number(mainLine)
            if num is None:
                if Switch:
                    firstBuffer.write('%s\n' % temp)
                else:
                    secondBuffer.write('%s\n' % temp)
                break

            if Switch:
                firstBuffer.write('%s\n' % temp)
                if temp > num:
                    Switch = False
            else:
                secondBuffer.write('%s\n' % temp)
                if temp > num:
                    Switch = True
            temp = num
    readAndAnimate("mainLine.txt",'buf1.txt', 'buf2.txt')


def Merge_Animate():

    with open('buf1.txt', 'r') as firstBuffer, open('buf2.txt', 'r') as secondBuffer, open('mainLine.txt', 'w') as mainLine:
        bufNum1 = read_next_number(firstBuffer)
        bufNum2 = read_next_number(secondBuffer)

        while bufNum1 is not None and bufNum2 is not None:
            if bufNum1 <= bufNum2:
                mainLine.write('%s\n' % bufNum1)
                bufNum1 = read_next_number(firstBuffer)
            else:
                mainLine.write('%s\n' % bufNum2)
                bufNum2 = read_next_number(secondBuffer)

        while bufNum1 is not None:
            mainLine.write('%s\n' % bufNum1)
            bufNum1 = read_next_number(firstBuffer)

        while bufNum2 is not None:
            mainLine.write('%s\n' % bufNum2)
            bufNum2 = read_next_number(secondBuffer)
    readAndAnimate("mainLine.txt",'buf1.txt', 'buf2.txt')