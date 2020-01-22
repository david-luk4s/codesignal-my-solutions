def firstNotRepeatingCharacter(s):
    li = []
    cs = {}
    for c in s:
        if c in li:
            cs[c] += 1    
        else:
            cs[c] = 1
            li.append(c)
    for c in li:
        if cs[c] == 1:
            return c
    return '_'
