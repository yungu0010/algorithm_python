# 25501 - 재귀의 귀재

import sys
input = sys.stdin.readline

TC = int(input())
count = 0

def recursion(s, left, right):
    global count
    count += 1
    if left >= right: return 1
    elif s[left] != s[right]: return 0
    else: return recursion(s, left+1, right-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

for _ in range(TC):
    count = 0
    string = input().rstrip()
    print(isPalindrome(string), count)
    