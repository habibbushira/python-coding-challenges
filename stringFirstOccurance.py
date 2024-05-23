
def firstOccurance(haystack, needle):
    h = len(haystack)
    n = len(needle)
    for i in range(h):
        # k = i
        for j in range(n):
            if (haystack[i+j] == needle[j]):
                if j == n-1:
                    return i
            else:
                continue
    return -1
    
print(firstOccurance("sasadutsad", "sad"))
