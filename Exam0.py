def dMot(s: str) :
    words = s.strip().split()
    if words :
        return len(words[-1])
    else :
        return 0
   


print(dMot("Hello World"))  
print(dMot(" Envole-moi vers la lune ")) 
print(dMot("Luffy est toujours Joyboy"))  