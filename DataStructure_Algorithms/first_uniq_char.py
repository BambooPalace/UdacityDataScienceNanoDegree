'''
387. First Unique Character in a String
Easy

1949

117

Add to List

Share
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.
 

Note: You may assume the string contains only lowercase English letters.
'''

def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """
    
    letters='abcdefghijklmnopqrstuvwxyz'
    index=[s.index(l) for l in letters if s.count(l) == 1]
    print(index)
    return min(index) if len(index) > 0 else -1

print(firstUniqChar('loveleetcode'))
