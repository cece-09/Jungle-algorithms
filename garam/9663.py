# 먼소리야 다시보자~
import sys

input = sys.stdin.readline
n = int(input().rstrip())
row = [0] * n
ans = 0


def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True


def n_queens(x):
    global ans
    if x == n:
        ans += 1
    else:
        for i in range(n):
            row[x] = i
            if is_promising(x)
            n_queens(x+1)


