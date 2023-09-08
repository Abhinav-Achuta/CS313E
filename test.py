def highest_debt(debts):
    
    for i in range(len(debts)):
        for j in range(i+1, len(debts)):
            if debts[i] > debts[j]:
                temp = debts[i]
                debts[i] = debts[j]
                debts[j] = temp
    return(debts)


list = [9,8,10,13]

print(highest_debt(list))