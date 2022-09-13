# 15829 - Hashing

import sys
input = sys.stdin.readline

index = [0] * 27
ASCII = 97
r = 31
hash = 0

# 알파벳 소문자에 대응되는 값 저장
for i in range(26):
    index[i+1] = chr(ASCII)
    ASCII += 1

length = int(input().rstrip())
string = input().rstrip()

for s in range(len(string)):
    hash += index.index(string[s]) * 31 ** s

print(hash % 1234567891)