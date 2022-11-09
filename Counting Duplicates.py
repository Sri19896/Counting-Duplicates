
def duplicate_count(s):
    s = s.lower()
    t = 0
    for i in s:
        if s.count(i) > 1:
            s = s.replace(i, '')
            t = t+1
    return t


print(duplicate_count("aabbcde"))
