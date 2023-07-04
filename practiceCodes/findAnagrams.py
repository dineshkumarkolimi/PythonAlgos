'''
Created on 12-Feb-2020

@author: dineshkumars
'''

s = ["ate", "bat", "tan", "tea", "tab","eat", "dinesh", "akhila", "akilah"]

stringSet = []
i = 0
j = 0
k=0
counter = 0
flag = True
while (i < len(s)):
    if not any(s[i] in items for items in stringSet):
        stringSet.append([])
        stringSet[k].append(s[i])
        j = i+1
        while (j<len(s)):
            if len(s[j]) == len(s[i]):
                for letter in s[i]:
                    if letter in s[j]:
                        continue
                    else:
                        flag = False
                        break
                if flag:
                    stringSet[k].append(s[j])
            j+=1   
            flag = True
        k+=1
        counter+=1
    i+=1
        
print stringSet
print counter