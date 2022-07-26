def PrimeNum(num):
    number = 0
    #prime = True
    PrimeNumber = 2
    while number != num:
        PrimeNumber +=1
        prime = True
        for i in range(2, PrimeNumber):
            if (PrimeNumber % i) == 0:
                prime = False
                break
        if prime == True:
            number += 1
        print(number,num,prime,PrimeNumber)
    return PrimeNumber
print(PrimeNum(455))
        
