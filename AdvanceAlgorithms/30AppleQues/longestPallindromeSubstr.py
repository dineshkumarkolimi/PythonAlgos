str = "swindniwabbasjatabcicbataj"

def isPallindrome(str):
    # print(str)
    # start = 0
    # end = len(str)-1
    # while start <= end:
    #     if str[start] != str[end]:
    #         return False
    #     start = start + 1
    #     end = end - 1
    return str == str[::-1]

def longestSubStr(str):
    max_length = 0
    max_start_ind = 0
    max_end_ind = 0
    for i in range(len(str)):
        for j in range(i+1,len(str)+1):
            # print(max_length, j-i)
            if isPallindrome(str[i:j]) and (max_length <= j-i):
                max_length = j-i
                max_start_ind = i
                max_end_ind = j   
                # print(max_length)
    print(str[max_start_ind:max_end_ind])


longestSubStr(str)
# print(isPallindrome("jatabcicbataj"))