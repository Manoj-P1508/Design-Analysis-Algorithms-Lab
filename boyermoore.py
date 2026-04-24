MAX_CHARS = 256
def badChar(pat):
    badchar = [-1] * MAX_CHARS
    for i in range(len(pat)):
        badchar[ord(pat[i])] = i
    return badchar

def search(text, pat):
    m = len(pat)
    n = len(text)
    badchar = badChar(pat)    
    s = 0   
    while s <= n - m:
        j = m - 1
        while j >= 0 and pat[j] == text[s + j]:
            j -= 1
        if j < 0:
            print("Pattern found at index", s)
            if s + m < n:
                s += m - badchar[ord(text[s + m])]
            else:
                s += 1
        else:
            s += max(1, j - badchar[ord(text[s + j])])
text = input("Enter text: ")
pat = input("Enter pattern: ")
search(text, pat)