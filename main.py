import os
import random

import colorama
import pandas

SymbolsCost = {
    'DIAMOND': [0, 0, 0, 0, 0],
    'GORILLA': [0, 2, 25, 100, 1000],
    'MAN': [0, 0, 20, 100, 500],
    'BIRD': [0, 0, 15, 50, 250],
    'BUTTERFLY': [0, 0, 15, 50, 250],
    'A': [0, 0, 5, 25, 150],
    'K': [0, 0, 5, 25, 150],
    'Q': [0, 0, 5, 20, 100],
    'J': [0, 0, 5, 20, 100],
    '10': [0, 0, 5, 20, 100],
    '9': [0, 0, 5, 20, 100],
    'MAP': [0, 0, 1, 5, 10, 500]
}

FreeSpins = {
    0: 0,
    1: 0,
    2: 0,
    3: 10,
    4: 15,
    5: 25
}


def create_value_index_pairs(in_line_indexes):
    value_index_pairs = []
    for row_idx, row in enumerate(in_line_indexes):
        value_index_pairs.append([])
        for col_idx, value in enumerate(row):
            value_index_pairs[row_idx].append([value, col_idx])
    return value_index_pairs


LineIndexes = [
    #[0, 0, 0, 0, 0],  # Top line
     [1, 1, 1, 1, 1],  # Middle line
     #[2, 2, 2, 2, 2],  # Bottom line
    # [0, 1, 2, 1, 0],  # V line
    # [2, 1, 0, 1, 2],  # reverse V line
    # [1, 2, 2, 2, 1],  # U line,
    # [1, 0, 0, 0, 1],  # reverse, U line
    # [2, 2, 1, 2, 2],
    # [0, 0, 1, 0, 0],
    # [1, 1, 2, 1, 1],
]

LineColors = {
    0: colorama.Fore.RESET,
    1: colorama.Fore.GREEN,
    2: colorama.Fore.CYAN,
    3: colorama.Fore.YELLOW,
    4: colorama.Fore.MAGENTA,
    5: colorama.Fore.BLUE,
    6: colorama.Fore.LIGHTGREEN_EX,
    7: colorama.Fore.LIGHTYELLOW_EX,
    8: colorama.Fore.LIGHTBLUE_EX,
    9: colorama.Fore.LIGHTRED_EX
}
ExcelData = pandas.read_excel('Барабаны.xlsx', sheet_name='Sheet1', header=3)
Reels: list[list[str]] = [
    ExcelData['Reel 1'].tolist()[0:40],
    ExcelData['Reel 2'].tolist()[0:38],
    ExcelData['Reel 3'].tolist()[0:41],
    ExcelData['Reel 4'].tolist()[0:34],
    ExcelData['Reel 5'].tolist()[0:34]
]
MatrixLineIndexes = create_value_index_pairs(LineIndexes)
Slots = []
LinesColors = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]


def fcolor_lines(winning_lines):
    LinesColors[0] = [0, 0, 0, 0, 0]
    LinesColors[1] = [0, 0, 0, 0, 0]
    LinesColors[2] = [0, 0, 0, 0, 0]
    for ind, is_win in enumerate(winning_lines):
        if is_win:
            for indexes in MatrixLineIndexes[ind]:
                LinesColors[indexes[0]][indexes[1]] = ind + 1


def print_colorized(text, index):
    print(f"{LineColors[index]}{text.ljust(14, ' ')}{colorama.Style.RESET_ALL}", end='')


def generate_slots():
    Slots.clear()
    random_index_in_reels = [random.randint(0, len(reel) - 1) for reel in Reels]
    for height in range(0, 3):
        line = []
        for ind in range(0, len(Reels)):
            index = random_index_in_reels[ind]
            line.append(Reels[ind][(index + height) % len(Reels[ind])])
        Slots.append(line)


def print_slot(winning_lines):
    fcolor_lines(winning_lines)
    print()
    print("-" * 70)
    for ind_x, slot_line in enumerate(Slots):
        for ind_y, slot in enumerate(slot_line):
            print_colorized(str(slot), LinesColors[ind_x][ind_y])
        print()
    print("-" * 70)


def compare_symbols(a, b):
    return a != b and not (
            (a == 'DIAMOND' and b != 'MAP') or (b == 'DIAMOND' and a != 'MAP'))


def calculate_slots_win():
    current_roll_money = 0
    winning_lines = [False] * 10
    lines = [[Slots[y[0]][y[1]] for y in x] for x in MatrixLineIndexes]
    for i in range(0, len(lines) - 1):
        win1 = calculate_line_win(lines[i])
        current_roll_money += win1
        if win1 != 0:
            winning_lines[i] = True
    return current_roll_money, winning_lines


def calculate_line_win(line):
    amount = 0
    number_occurrence, amount = get_money_from_left(line, amount)
    if number_occurrence >= len(line) - 1:
        return amount
    line = line[::-1]
    number_occurrence, amount = get_money_from_left(line, amount)
    return amount


def get_money_from_left(line, in_amount):
    number_occurrence = 0
    for ind in range(0, (len(line) - 1)):
        number_occurrence += 1
        buf = line[ind]
        if line[ind] == 'MAP':
            break
        if line[ind + 1] == 'DIAMOND' and line[ind] != 'MAP':
            while ind + 1 < len(line) - 1 and line[ind + 1] == 'DIAMOND':
                ind += 1
                number_occurrence += 1
            if line[ind + 1] == len(line) - 1:
                number_occurrence += 1
                break
        if compare_symbols(buf, line[ind + 1]):
            in_amount += SymbolsCost[str(buf)][ind]
            break
    return number_occurrence, in_amount


def count_scatters():
    count = 0
    for a in Slots:
        for b in a:
            if b == 'MAP':
                count += 1
    return count


if __name__ == '__main__':
    FreeSpinsCount = 0
    MoneyForOneRoll = int(input("Enter the amount of money per roll: "))
    TotalMoney = 100
    print("You have " + str(TotalMoney) + " money.")
    print("Press, to roll spin for " + str(MoneyForOneRoll) + " moneys")
    input()
    os.system('cls||clear')
    while True:
        factor = 1
        if FreeSpinsCount > 0:
            FreeSpinsCount -= 1
            factor = 2
        else:
            TotalMoney -= MoneyForOneRoll
            factor = 1
        print("You have " + str(TotalMoney) + " money.")

        generate_slots()
        CurrentRollMoney, WinningLines = calculate_slots_win()
        print_slot(WinningLines)
        count_scat = count_scatters()
        FreeSpinsCount += FreeSpins[count_scat]
        CurrentRollMoney += SymbolsCost['MAP'][count_scat]
        CurrentRollMoney *= factor
        TotalMoney += CurrentRollMoney

        print("You got: " + str(CurrentRollMoney) + " from roll")

        if FreeSpinsCount > 0:
            print("You got " + str(FreeSpinsCount) + " free Spins")
            print("Press, to roll free spins")
        else:
            print("Press, to roll spin for " + str(MoneyForOneRoll) + " moneys")
        input()
        os.system('cls||clear')


