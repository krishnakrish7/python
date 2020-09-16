def compound_interest(principle,rate,time):
    Amount= principle * (pow((1 + rate / 100),time))
    CI = Amount - principle
    print('The compound interest is: ', CI)
    
compound_interest(1000,10.25,5)
