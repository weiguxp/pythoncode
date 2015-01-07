def calcInterest(Balance, AnnRate, MinPay):
    for i in range(1,13):
        paidPrinciple = round(MinPay - (Balance * (AnnRate/12)),2)
        Balance = round(Balance - paidPrinciple,2)
        print ("Month",i)
        print ('minMonthPay', MinPay)
        print ("paidPrinciple", paidPrinciple)
        print ("Balance", Balance)
    return Balance

        

def getVariables():
    inpBalance = float(input("Tell me your balance"))
    inpAnnRate = float(input("Annual Rate"))
    Remaining = inpBalance
    inpMinPay = 0
    
    while Remaining > 0 :
        inpMinPay = inpMinPay + 10
        Remaining = calcInterest(inpBalance, inpAnnRate, inpMinPay)

    print (inpMinPay)

        
getVariables()





    
    
