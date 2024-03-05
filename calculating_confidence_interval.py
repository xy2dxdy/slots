from math import sqrt

from main import generate_slots, calculate_slots_win, print_slot, count_scatters, FreeSpins, SymbolsCost

if __name__ == '__main__':
    FreeSpinsCount = 0
    TotalMoney = 0
    corner = int(input("Введите количество спинов: "))
    stdDev = float(input("Введите среднеквадратичное отклонение: "))
    for i in range(0, corner):
        if FreeSpinsCount > 0:
            FreeSpinsCount -= 1
        generate_slots()
        CurrentRollMoney, WinningLines = calculate_slots_win()
        print_slot(WinningLines)
        count_scat = count_scatters()
        FreeSpinsCount += FreeSpins[count_scat]
        CurrentRollMoney += SymbolsCost['MAP'][count_scat]
        TotalMoney += CurrentRollMoney
    left = float(TotalMoney) / float(corner) - 1.95 * stdDev/sqrt(corner)
    right = float(TotalMoney) / float(corner) + 1.95 * stdDev/sqrt(corner)
    print("[" + str("%.10f" % left) + " , " + str("%.10f" % right) + "]")
