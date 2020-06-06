def n_primos(x):
    total = 0
    while(x != 1):
        fator =2
        while x % fator != 0 and fator <= x /2:
            fator = fator + 1
        if x % fator != 0 or x == 2:
            total += 1
        else:
            pass
        
        x = x -1
    return total
