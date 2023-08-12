import sys
input=sys.stdin.readline


def fsort(a, max: int):
    """도수 정렬(배열 원솟값은 0 이상 max 이하)"""
    n = len(a)           # 정렬할 배열 a
    f = [0] * (max + 1)  # 누적 도수 분포표 배열 f
    b = [0] * n          # 작업용 배열 b

    for i in range(n):              f[a[i]] += 1                     # [1단계]
    for i in range(1, max + 1):     f[i] += f[i - 1]                 # [2단계]
    for i in range(n - 1, -1, -1):  f[a[i]] -= 1; b[f[a[i]]] = a[i]  # [3단계]
    for i in range(n):              a[i] = b[i]                      # [4단계]

def counting_sort(a):
    """도수 정렬"""
    fsort(a, max(a))

N = int(input())

unsorted = []
for _ in range(N):
    unsorted.append(int(input()))

counting_sort(unsorted)
for i in unsorted:
    print(i)