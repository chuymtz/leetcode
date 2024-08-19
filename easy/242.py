"""
Given 2 strs s and t, return true if t is an anagram of s, and false ow.
an anagram is all chars of s are contained in t. 
ex:

s = "anagram", t = "nagaram"
true

s = "rat", t = "car"
false


"""

s = "anagram"
t = "nagaram"


string = s

def make_hash(string):
    hash = {}
    
    {k:sum([k in x for x in string]) for k in set(string)}
    
    for k in set(string):
        hash[k] = sum([k in x for x in string])
    return hash

make_hash(t)
make_hash(s)
make_hash("jesus")
make_hash(t) == make_hash(s)
make_hash("anagrma") == make_hash(s)

# found sol

sorted(s)
sorted(t)

class Solution(object):
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}
        
        for i in range(len(s)):
            countS[s[i]] = s + 0
        


