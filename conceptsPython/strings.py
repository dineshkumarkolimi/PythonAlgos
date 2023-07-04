#string functions and examples

s = "hello world"
print(s[2])
print(s[2:5])
len(s)

#extracting multiple fields from a line based on delimiter - split, splitlines
#Case conversion functions - lower, upper, swapcase, capitalize
#Validation functions - isdigit, isalpha, isalnum, isprint, islower, isupper
#Trim functions - lstrip, rstrip, strip
#padding functions - ljust, rjust
str = "1, 2030, Jan, open, welldone, finish"
splitList = str.split(',')
print(str.split(',')[2])
print(str.split(',')[2].isalpha())
a = int(str.split(',')[0]) if(str.split(',')[0].isdigit()) else 0
print(a)


#pass upper and lower bound to the function and get sum of range of numbers between them. passing a function as an argument
def sum(lb, ub, f):
    total = 0
    for i in range(lb,ub+1):
        total += f(i)
    return total
sum(5, 10, lambda i: i)
sum(5, 10, lambda i: i*i)
sum(5, 10, lambda i: i*2)

def checkEven(i){
        return i if(i%2==0) else 0
}

sum(5,10, lambda i: checkEven(i))

#Reading from a file and File IO
filePath = "/Desktop/Dinesh/dataFile.txt"
filePointer = open(filePath)
fileData = filePointer.read()
lines = fileData.splitlines()
for line in lines[:10]:
    print(line)

#lists and its functions
#search - count(item) gives the number of occurances of item in the list
#extend(), insert(), pop(), remove(), append(), copy(), clear(), reverse(), sort()
l = [1,2,3,1,3,4,,5,6,2,7]
s = [1,2,3,1,3,4,,5,6,2,7]

#Pandas
import pandas as pd
filePath = "/Desktop/Dinesh/dataFile.txt"
dataItems = pd.read_csv(filePath,name=["list of all column names"])
dataItems
dataItems.groupby([orderItemId])['order_item_sub_total'].sum()












