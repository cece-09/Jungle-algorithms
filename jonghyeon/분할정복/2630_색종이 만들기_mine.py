N = int(input())

papers = [list(map(int, input().split())) for _ in range(N)]

result = []

def solution(x, y, N):
    color = papers[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != papers[i][j]:
                solution(x, y, N//2)            # 2사분면
                solution(x, y+N//2, N//2)       # 1사분면
                solution(x+N//2, y, N//2)       # 3사분면
                solution(x+N//2, y+N//2, N//2)  # 4사분면
                return
    if color == 0:
        result.append(0)
    else:
        result.append(1)

solution(0, 0, N)
print(result.count(0))
print(result.count(1))