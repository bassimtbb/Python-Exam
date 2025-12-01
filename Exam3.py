def roman_to_int(s: str):
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    i = 0
    
    while i < len(s):
        if i + 1 < len(s) and roman_values[s[i]] < roman_values[s[i + 1]]:
            total += roman_values[s[i + 1]] - roman_values[s[i]]
            i += 2
        else:
            total += roman_values[s[i]]
            i += 1
    
    return total


print(roman_to_int("III"))   
print(roman_to_int("LVIII"))    
print(roman_to_int("MCMXCIV"))  