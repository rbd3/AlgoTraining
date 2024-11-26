def fibonnacci(number):
    if number == 0:
        return 0
    elif number == 1:
     return 1
    else:
     return fibonnacci(number - 1) + fibonnacci(number - 2)
    
print(fibonnacci(24))