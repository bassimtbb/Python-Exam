class Solution :
    def scoreOfString(self, s :str) :
        s_longueur = len(s)
        score = 0
        
        for i in range(s_longueur - 1):
            valeur_adjacente = abs(ord(s[i]) - ord(s[i+1]))
            score += valeur_adjacente
            
        return score