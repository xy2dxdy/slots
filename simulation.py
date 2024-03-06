from main import generate_slots, calculate_slots_win, count_scatters, FreeSpins, SymbolsCost
if __name__ == '__main__':
    FreeSpinsCount = 0
    SpentMoney = 0
    TotalMoney = 0
    n = int(input("Input count of spins: "))
    number = n
    LineWin = [0] * number
    for i in range(0, number):
        factor = 1
        if FreeSpinsCount > 0:
            FreeSpinsCount -= 1
            factor = 2
        else:
            factor = 1
            SpentMoney += 10

        generate_slots()
        CurrentRollMoney, WinningLines = calculate_slots_win()
        count_scat = count_scatters()
        FreeSpinsCount += FreeSpins[count_scat]
        CurrentRollMoney += SymbolsCost['MAP'][count_scat]
        TotalMoney += CurrentRollMoney * factor
        LineWin[i] += CurrentRollMoney * factor
    print("Got: " + str(TotalMoney))
    print("Spent: " + str(SpentMoney))
    print("RTP= " + str(float(TotalMoney) / SpentMoney * 100))
    print("Average win: " + str(float(TotalMoney)/number))
    disp = 0.0
    number = n
    for i in range(0, number):
        disp += (LineWin[i] - float(TotalMoney)/number)**2
    print("Dispersia:  "+str(disp/number))
