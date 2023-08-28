def are_anagram(s1, s2):
    if len(s1)!=len(s2):
        print("The two strings are not equal in length")
        return
    f1 = {}
    f2 = {}
    for ch in s1.lower():
        if ch in f1:
            f1[ch]+=1
        else:
            f1[ch] = 1
    for ch in s2.lower():
        if ch in f2:
            f2[ch]+=1
        else:
            f2[ch]=1
    for key in f1:
        if key not in f2 or f1[key] != f2[key]:
            print("These strings are not anagram")
            return False 
    print("These strings are anagrams")
    return True

# are_anagram('State','taste')

def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        print("the strings are not equal in length")
        return
    return sorted(s1.lower()) == sorted(s2.lower())

are_anagrams('State', 'taste')