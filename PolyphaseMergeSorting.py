

def read_next_number(file):

    num_str = file.readline()
    if num_str != "`\n" and num_str != '':
        num = int(num_str.replace("\n", ""))
        return num
    return None


def skipToLastEntry(file, condition):
    num = read_next_number(file)
    while int(num) != condition:
        num = read_next_number(file)
    return num


def DataPrepare(B, C):

    B1 = []
    B2 = []
    CurrentB1 = True
    temp = B[0]

    while B != []:
        B.pop(0)
        if B == []:
            if CurrentB1:
                B1.append(temp)
            else:
                B2.append(temp)
            break
        if CurrentB1:
            B1.append(temp)
            if temp > B[0]:
                CurrentB1 == False
        else:
            B2.append(temp)
            if temp > B[0]:
                CurrentB1 == True
        temp = B[0]

    B = B1+B2
    C1 = []
    C2 = []
    CurrentC1 = True
    while C != []:
        C.pop(0)
        if C == []:
            if CurrentC1:
                C1.append(temp)
            else:
                C2.append(temp)
            break
        if CurrentC1:
            C1.append(temp)
            if temp > C[0]:
                CurrentC1 == False
        else:
            C2.append(temp)
            if temp > C[0]:
                CurrentC1 == True
        temp = C[0]

    C = C1+C2
    i = 0
    length = len(B)-1
    while i < length:
        if B[i] > B[i+1]:
            B.insert(i+1, -1)
            i += 1
            length += 1
        i += 1
    i = 0
    length = len(C)-1
    while i < length:
        if C[i] > C[i+1]:
            C.insert(i+1, -1)
            i += 1
            length += 1
        i += 1
    B.append(-1)
    C.append(-1)
    print(B, C)

    with open('buf1.txt', 'w') as firstBuffer, open('mainLine.txt', 'w') as mainLine:
        for i in B:
            mainLine.write('%s\n' % i)
        for i in C:
            firstBuffer.write('%s\n' % i)


def makeDummyRuns(B, C):
    FIBONACCI = [2, 3, 5, 8, 13, 21, 34, 55, 89, 144,
                 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946]
    countB = B.count(-1)
    countC = C.count(-1)
    if countB > countC:
        for i in range(FIBONACCI)-1:
            if countB == FIBONACCI[i]:
                break
            if countB > FIBONACCI[i] and countB < FIBONACCI[i+1]:
                for k in range(FIBONACCI[i+1]-countB):
                    B.append


def PolyphaseMergeSort():
    A = []
    with open('mainLine.txt', 'r') as mainLine:
        num = read_next_number(mainLine)
        while num is not None:
            A.append(num)
            num = read_next_number(mainLine)
    B = A[:len(A)//2]
    C = A[len(A)//2:]
    print(B, C)
    DataPrepare(B, C)
    runMin = 2
    runMax = 4
    input1 = "mainLine.txt"
    input2 = "buf1.txt"
    output = "buf2.txt"
    lastEntry = None

    lastEntry = Merge(runMax, runMin, input1, input2, output, lastEntry)
    runMax = runMax+runMin

    while runMax <= len(A):

        if output == "buf2.txt":

            input1 = "buf2.txt"
            input2 = "mainLine.txt"
            output = "buf1.txt"

        elif output == "buf1.txt":

            input1 = "buf1.txt"
            input2 = "buf2.txt"
            output = "mainLine.txt"

        elif output == "mainline.txt":

            input1 = "mainLine.txt"
            input2 = "buf1.txt"
            output = "buf2.txt"

        lastEntry = Merge(runMin, runMax, input1, input2, output, lastEntry)
        runMax = runMin+runMax
        runMin = runMax-runMin
    lastEntry = Merge(runMin, runMax, input1, input2, output, lastEntry)


def Merge(runMin, runMax, input1, input2, output, lastEntry):
    with open(input1, 'r') as firstBuffer, open(input2, 'r') as secondBuffer, open(output, 'w') as mainLine:
        bufNum1 = read_next_number(firstBuffer)
        bufNum2 = None
        if lastEntry is not None:
            bufNum2 = skipToLastEntry(secondBuffer, lastEntry)
        else:
            bufNum2 = read_next_number(secondBuffer)

        while bufNum1 is not None and bufNum2 is not None:
            bufCount1 = 0
            bufCount2 = 0
            while bufNum1 != -1 and bufNum2 != -1 and bufNum1 is not None and bufNum2 is not None:
                if bufNum1 <= bufNum2:
                    mainLine.write('%s\n' % bufNum1)
                    bufNum1 = read_next_number(firstBuffer)

                else:
                    mainLine.write('%s\n' % bufNum2)
                    bufNum2 = read_next_number(secondBuffer)

            while bufNum1 != -1 and bufNum1 is not None:
                mainLine.write('%s\n' % bufNum1)
                bufNum1 = read_next_number(firstBuffer)
                if bufNum1 == -1:
                    mainLine.write('%s\n' % bufNum1)
                    break

            while bufNum2 != -1 and bufNum2 is not None:
                mainLine.write('%s\n' % bufNum2)
                bufNum2 = read_next_number(secondBuffer)
                if bufNum2 == -1:
                    mainLine.write('%s\n' % bufNum2)
                    break

        # while bufNum1 is not None:
        #     mainLine.write('%s\n' % bufNum1)
        #     bufNum1 = read_next_number(firstBuffer)

        while bufNum2 is not None:
            mainLine.write('%s\n' % bufNum2)
            bufNum2 = read_next_number(secondBuffer)
        return bufNum1
