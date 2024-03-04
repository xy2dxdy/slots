from __future__ import print_function

import os
import random
import pandas

win = {'DIAMOND': [0, 0, 0, 0, 0], 'GORILLA': [0, 2, 25, 100, 1000],
       'MAN': [0, 0, 20, 100, 500], 'BIRD': [0, 0, 15, 50, 250],
       'BUTTERFLY': [0, 0, 15, 50, 250], 'A': [0, 0, 5, 25, 150],
       'K': [0, 0, 5, 25, 150], 'Q': [0, 0, 5, 20, 100],
       'J': [0, 0, 5, 20, 100], '10': [0, 0, 5, 20, 100], '9': [0, 0, 5, 20, 100], 'MAP': [0, 1, 5, 10, 500]}
excel_data_df = pandas.read_excel('Барабаны.xlsx', sheet_name='Sheet1', header=3)
reel1 = excel_data_df['Reel 1'].tolist()[0:40]
reel2 = excel_data_df['Reel 2'].tolist()[0:38]
reel3 = excel_data_df['Reel 3'].tolist()[0:41]
reel4 = excel_data_df['Reel 4'].tolist()[0:34]
reel5 = excel_data_df['Reel 5'].tolist()[0:34]
slot = [[], [], []]
colorLines = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]


def fcolorLines(lines):
    if lines[0] == True:
        colorLines[0][0] = 1
        colorLines[0][1] = 1
        colorLines[0][2] = 1
        colorLines[0][3] = 1
        colorLines[0][4] = 1
    if (lines[1]):
        colorLines[1][0] = 1
        colorLines[1][1] = 1
        colorLines[1][2] = 1
        colorLines[1][3] = 1
        colorLines[1][4] = 1
    if (lines[2]):
        colorLines[2][0] = 1
        colorLines[2][1] = 1
        colorLines[2][2] = 1
        colorLines[2][3] = 1
        colorLines[2][4] = 1
    if (lines[3]):
        colorLines[0][0] = 2
        colorLines[1][1] = 2
        colorLines[2][2] = 2
        colorLines[1][3] = 2
        colorLines[0][4] = 2
    if (lines[4]):
        colorLines[2][0] = 3
        colorLines[1][1] = 3
        colorLines[0][2] = 3
        colorLines[1][3] = 3
        colorLines[2][4] = 3
    if (lines[5]):
        colorLines[1][0] = 4
        colorLines[2][1] = 4
        colorLines[2][2] = 4
        colorLines[2][3] = 4
        colorLines[1][4] = 4
    if (lines[6]):
        colorLines[1][0] = 5
        colorLines[0][1] = 5
        colorLines[0][2] = 5
        colorLines[0][3] = 5
        colorLines[1][4] = 5
    if (lines[7]):
        colorLines[2][0] = 6
        colorLines[2][1] = 6
        colorLines[1][2] = 6
        colorLines[2][3] = 6
        colorLines[2][4] = 6
    if (lines[8]):
        colorLines[0][0] = 2
        colorLines[0][1] = 2
        colorLines[1][2] = 2
        colorLines[0][3] = 2
        colorLines[0][4] = 2
    if (lines[9]):
        colorLines[1][0] = 3
        colorLines[1][1] = 3
        colorLines[2][2] = 3
        colorLines[1][3] = 3
        colorLines[1][4] = 3


def out_white(text):
    print('%-15s' % "\033[38m{}".format(text), end='')


def out_red(text):
    print('%-15s' % "\033[31m{}".format(text), end='')


def out_green(text):
    print('%-15s' % "\033[32m{}".format(text), end='')


def out_yellow(text):
    print('%-15s' % "\033[33m{}".format(text), end='')


def out_blue(text):
    print('%-15s' % "\033[34m{}".format(text), end='')


def out_perple(text):
    print('%-15s' % "\033[35m{}".format(text), end='')


def out_turquoise(text):
    print('%-15s' % "\033[36m{}".format(text), end='')


def clearColorLines():
    colorLines[0] = [0, 0, 0, 0, 0]
    colorLines[1] = [0, 0, 0, 0, 0]
    colorLines[2] = [0, 0, 0, 0, 0]


def spin():
    r1 = random.randint(1, len(reel1) - 1)
    r2 = random.randint(1, len(reel2) - 1)
    r3 = random.randint(1, len(reel3) - 1)
    r4 = random.randint(1, len(reel4) - 1)
    r5 = random.randint(1, len(reel5) - 1)
    slot[0] = [reel1[r1], reel2[r2], reel3[r3], reel4[r4], reel5[r5]]

    if (r1 == len(reel1) - 1):
        r1 = 0
    else:
        r1 += 1
    if r2 == len(reel2) - 1:
        r2 = 0
    else:
        r2 += 1
    if (r3 == len(reel3) - 1):
        r3 = 0
    else:
        r3 += 1
    if r4 == len(reel4) - 1:
        r4 = 0
    else:
        r4 += 1
    if (r5 == len(reel5) - 1):
        r5 = 0
    else:
        r5 += 1
    slot[1] = [reel1[r1], reel2[r2], reel3[r3], reel4[r4], reel5[r5]]

    if (r1 == len(reel1) - 1):
        r1 = 0
    else:
        r1 += 1
    if (r2 == len(reel2) - 1):
        r2 = 0
    else:
        r2 += 1
    if (r3 == len(reel3) - 1):
        r3 = 0
    else:
        r3 += 1
    if (r4 == len(reel4) - 1):
        r4 = 0
    else:
        r4 += 1
    if (r5 == len(reel5) - 1):
        r5 = 0
    else:
        r5 += 1
    slot[2] = [reel1[r1], reel2[r2], reel3[r3], reel4[r4], reel5[r5]]


def printSlot(lines):
    fcolorLines(lines)
    print("\n" + "--------------------------------------------------------")
    for i in range(0, len(slot)):
        for j in range(0, len(slot[i])):
            if colorLines[i][j] == 1:
                out_red(str(slot[i][j]))
            elif colorLines[i][j] == 2:
                out_perple(slot[i][j])
            elif colorLines[i][j] == 3:
                out_blue(slot[i][j])
            elif colorLines[i][j] == 4:
                out_green(slot[i][j])
            elif colorLines[i][j] == 5:
                out_yellow(slot[i][j])
            elif colorLines[i][j] == 6:
                out_turquoise(slot[i][j])
            else:
                out_white(slot[i][j])

        print("\033[38m{}".format(''))
    print("--------------------------------------------------------")


def isNotTheSame(a, b):
    return a != b and not (
            (a == 'DIAMOND' and b != 'MAP') or (b == 'DIAMOND' and a != 'MAP'))


def calculateWin(line):
    amount = 0
    number_occurrence = 0
    for i in range(0, (len(line) - 2)):
        number_occurrence += 1
        if line[i + 1] == 'DIAMOND' and line[i] != 'MAP':
            i += 1
            if line[i] != line[i + 2]:
                amount += win[str(line[i])][i]
                break
            continue
        elif isNotTheSame(line[i], line[i + 1]):
            amount += win[str(line[i])][i]
            break

    if number_occurrence >= len(line) - 1:
        return amount
    line = line[::-1]
    for i in range(0, (len(line) - 2)):
        if line[i + 1] == 'DIAMOND' and line[i] != 'MAP':
            i += 1
            if line[i] != line[i + 2]:
                amount += win[str(line[i])][i]
                break
            continue
        elif isNotTheSame(line[i], line[i + 1]):
            amount += win[str(line[i])][i]
            break

    return amount


if __name__ == '__main__':

    while True:
        clearColorLines()
        spin()
        winnings = 0
        winningLines = [False] * 10
        lines = [slot[0], slot[1], slot[2],
                 [slot[0][0], slot[1][1], slot[2][2], slot[1][3], slot[0][4]],
                 [slot[2][0], slot[1][1], slot[0][2], slot[1][3], slot[2][4]],
                 [slot[1][0], slot[2][1], slot[2][2], slot[2][3], slot[1][4]],
                 [slot[1][0], slot[0][1], slot[0][2], slot[0][3], slot[1][4]],
                 [slot[2][0], slot[2][1], slot[1][2], slot[2][3], slot[2][4]],
                 [slot[0][0], slot[0][1], slot[1][2], slot[0][3], slot[0][4]],
                 [slot[1][0], slot[1][1], slot[2][2], slot[1][3], slot[1][4]]]
        for i in range(0, len(lines) - 1):
            win1 = calculateWin(lines[i])
            winnings += win1
            if win1 != 0:
                winningLines[i] = True
        printSlot(winningLines)
        print(winnings)
        input()
        #os.system('cls')
