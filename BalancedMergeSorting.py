import os


def read_next_number(file):

    num_str = file.readline()
    if num_str != "`\n" and num_str != '':
        num = int(num_str.replace("\n", ""))
        return num
    return None


def listSplit(n):
    Switch = True
    with open('buf3.txt', 'a') as thirdBuffer, open('mainLine.txt', 'r') as mainLine:
        for i in range(n):
            num = read_next_number(mainLine)
            thirdBuffer.write('%s\n' % num)

    with open('buf1.txt', 'w') as firstBuffer, open('buf2.txt', 'w') as secondBuffer, open('buf3.txt', 'r') as thirdBuffer:
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


def Balanced_Merge_Sort(length):
    i = 2
    while i < length/2:
        listSplit(i)
        if os.stat("buf2.txt").st_size == 0:
            break
        Merge()
        i = i*2
