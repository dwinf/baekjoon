# A+B - 3
count = int(input())
for i in range(count):
    a, b = map(int, input().split())
    print(a+b)

import sys

for _ in range(int(sys.stdin.readline())):
    print(sum(map(int, sys.stdin.readline().rstrip().split())))

# input()은 개행문자를 제거하여 리턴, prompt message를 출력
# sys.stdin.readline()는 개행문자를 포함한 값을 리턴하고 prompt message를 출력하지 않기 때문에 실행시간이 빠르다