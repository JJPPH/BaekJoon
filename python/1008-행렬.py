import sys

input = sys.stdin.readline
N, M = map(int, input().split())

A = [list(map(int, input().rstrip())) for j in range(N)]
B = [list(map(int, input().rstrip())) for j in range(N)]


def flip(i, j):
    for x in range(i, i + 3):
        for y in range(j, j + 3):
            A[x][y] = 1 - A[x][y]


result = 0
for i in range(N - 2):  # 줄바꿈 가능 횟수
    for j in range(M - 2):  # 가로 줄 이동 가능 횟수
        if A[i][j] != B[i][j]:
            flip(i, j)
            result += 1

        if A == B:
            break
    if A == B:
        break

if A != B:
    print(-1)
else:
    print(result)
