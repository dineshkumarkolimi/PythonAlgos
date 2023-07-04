def buddyStrings(A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        counter=0
        x= -1
        y=-1
        s = []
        for a,b in zip(A,B):
            if a != b:
                s.append(a)
                s.append(b)
                counter+=1
                if counter > 2:
                    return False
                
        print(s)
        if(s[0] == s[3] and s[1] == s[2]):
            return True
        else:
            return False

buddyStrings("ab", "ba")
