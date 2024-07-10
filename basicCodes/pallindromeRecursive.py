

def isPall(s, l, r):
    if s == "":
        return True
    if l >= r:
        return True
    if s[l] != s[r]:
        return False
    return isPall(s, l+1, r-1)

if __name__ == "__main__":
    s = "abcba"
    print(isPall(s, 0, len(s)-1))
    s = "dinesd"
    print(isPall(s, 0, len(s)-1))
    print(isPall("", 0, 0))

