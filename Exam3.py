def romanToInt(s :str) :
    valeurs = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    prec_val = 0
        
    for char in reversed(s):
        val = valeurs[char]            
        if val < prec_val:
            total -= val
        else:
            total += val
            
        prec_val = val
            
    return total

print(romanToInt("III"))   
print(romanToInt("LVIII"))    
print(romanToInt("MCMXCIV"))  