from main import generate_slots, calculate_slots_win, count_scatters, FreeSpins, SymbolsCost
if __name__ == '__main__':
    FreeSpinsCount = 0
    SpentMoney = 0
    TotalMoney = 0
    number = int(input("Input count of spins: "))
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
        CurrentRollMoney *= factor
        TotalMoney += CurrentRollMoney
    print("Got: " + str(TotalMoney))
    print("Spent: " + str(SpentMoney))
    print("RTP= " + str(float(TotalMoney) / SpentMoney * 100))
