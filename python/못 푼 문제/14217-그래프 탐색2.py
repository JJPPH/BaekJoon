import sys

input = sys.stdin.readline

n, m = map(int, input().split())
path = [list(map(int, input().split())) for _ in range(m)]

