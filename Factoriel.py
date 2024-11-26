def Factoriel(number):
    # 1*1 + 2*2 + 3*3
    if number == 0 or number == 1:
        return 1
    else:
        return number * Factoriel(number - 1)
    
print(Factoriel(5))