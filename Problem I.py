# Problem I - Gold Balloon - Drive the car

from sys import stdin, stdout

s, n = tuple(map(int, stdin.readline().split()))
changes = [tuple(map(int, stdin.readline().split()) for _ in range(n)]

current = (0, 0)
speed = 0
distance = 0



