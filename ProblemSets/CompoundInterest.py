def calcInterest(Balance, AnnRate, MinPay):
    minMonthPay = round(Balance * MinPay,2)
    paidPrinciple = round(minMonthPay - (Balance * (AnnRate/12)),2)
    Balance = round(Balance - paidPrinciple,2)
    print ('minMonthPay', minMonthPay)
    print ("paidPrinciple", paidPrinciple)
    print ("Balance", Balance)
    return Balance

        

def getVariables():
    inpBalance = float(input("Tell me your balance"))
    inpAnnRate = float(input("Annual Rate"))
    inpMinPay = float(input("Minimal Payment"))
    Balance = inpBalance

    for i in range(1,13):
        print ("Month",i)
        Balance = calcInterest(Balance, inpAnnRate, inpMinPay)
        
getVariables()




    
    
