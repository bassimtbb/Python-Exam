def plusOne(digits):
    for i in range(len(digits) - 1, -1, -1):
        digits[i] += 1
        if digits[i] < 10:
            return digits
        digits[i] = 0
    return [1] + digits


print(plusOne([1, 2, 3]))  
print(plusOne([4, 3, 2, 1]))  
print(plusOne([9]))            
print(plusOne([9, 9, 9]))       