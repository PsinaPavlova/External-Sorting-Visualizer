# import os


def read_next_number(file):

    num_str = file.readline()
    if num_str != "`\n" and num_str != '':
        num = int(num_str.replace("\n", ""))
        return num
    return None


def listSplit(length):
    # with open('buf3.txt', 'a') as thirdBuffer, open('mainLine.txt', 'r') as mainLine:
    #     for i in range(n):
    #         num = read_next_number(mainLine)
    #         thirdBuffer.write('%s\n' % num)

    with open('buf1.txt', 'w') as firstBuffer, open('buf2.txt', 'w') as secondBuffer, open('mainLine.txt', 'r') as mainLine:
        num = read_next_number(mainLine)
        while num is not None:
            for i in range(length):
                if num is None:
                    break
                firstBuffer.write('%s\n' % num)
                num = read_next_number(mainLine)
            for i in range(length):
                if num is None:
                    break
                secondBuffer.write('%s\n' % num)
                num = read_next_number(mainLine)


def Merge(run):

    with open('buf1.txt', 'r') as firstBuffer, open('buf2.txt', 'r') as secondBuffer, open('mainLine.txt', 'w') as mainLine:
        bufNum1 = read_next_number(firstBuffer)
        bufNum2 = read_next_number(secondBuffer)

        while bufNum1 is not None and bufNum2 is not None:
            bufCount1 = 0
            bufCount2 = 0
            while bufCount1 < run and bufCount2 < run and bufNum1 is not None and bufNum2 is not None:
                if bufNum1 <= bufNum2:
                    mainLine.write('%s\n' % bufNum1)
                    bufNum1 = read_next_number(firstBuffer)
                    bufCount1 += 1
                else:
                    mainLine.write('%s\n' % bufNum2)
                    bufNum2 = read_next_number(secondBuffer)
                    bufCount2 += 1

            while bufCount1 < run and bufNum1 is not None:
                mainLine.write('%s\n' % bufNum1)
                bufNum1 = read_next_number(firstBuffer)
                bufCount1 += 1
            while bufCount2 < run and bufNum2 is not None:
                mainLine.write('%s\n' % bufNum2)
                bufNum2 = read_next_number(secondBuffer)
                bufCount2 += 1

        while bufNum1 is not None:
            mainLine.write('%s\n' % bufNum1)
            bufNum1 = read_next_number(firstBuffer)
        while bufNum2 is not None:
            mainLine.write('%s\n' % bufNum2)
            bufNum2 = read_next_number(secondBuffer)


def Balanced_Merge_Sort(length):
    run = 1
    while run <= length//2:
        listSplit(run)
        # if os.stat("buf2.txt").st_size == 0:
        #     break
        Merge(run)
        run = run*2
    listSplit(run)
    # if os.stat("buf2.txt").st_size == 0:
    #     break
    Merge(run)
