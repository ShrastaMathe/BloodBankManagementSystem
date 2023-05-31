def twice(s):
    for i in range(0, len(s)): #S
        for j in range(1, len(s)): #hrasta

            if s[i].lower() == s[j].lower():
                return s[j]





print(twice("Shrasta"))
print(twice("Suong"))
print(twice("hhhtyyy"))
print(twice("htyyy"))