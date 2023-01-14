N = int(input("Введите количество списков\n"))
Lines = []
Symbols = []
Repeats = []
for i in range(N):
    Lines.append(input("Введите строку  " + str(i + 1) + "\n"))
for i in range(len(Lines)):
    CTPOKA = Lines[i]
    for j in range(len(CTPOKA)):
        ECTb = False
        for k in range(len(Symbols)):
            if(CTPOKA[j] == Symbols[k]):
                Repeats[k] = True
                ECTb = True
        if(not(ECTb)):
            Symbols.append(CTPOKA[j])
            Repeats.append(False)
K = 0
for i in range(len(Repeats)):
    if(Repeats[i]): K+=1
print("Количество повторяющихся символов: " + str(K))
