N = int(input("Введите количество списков\n"))
CTPOKU = []
CUMBOJIbI = []
nOBTOPPEHU9 = []
for i in range(N):
    CTPOKU.append(input("Введите строку  " + str(i + 1) + "\n"))
for i in range(len(CTPOKU)):
    CTPOKA = CTPOKU[i]
    for j in range(len(CTPOKA)):
        ECTb = False
        for k in range(len(CUMBOJIbI)):
            if(CTPOKA[j] == CUMBOJIbI[k]):
                nOBTOPPEHU9[k] = True
                ECTb = True
        if(not(ECTb)):
            CUMBOJIbI.append(CTPOKA[j])
            nOBTOPPEHU9.append(False)
K = 0
for i in range(len(nOBTOPPEHU9)):
    if(nOBTOPPEHU9[i]): K+=1
print("Количество повторяющихся символов: " + str(K))
