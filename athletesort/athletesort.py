p, q = map(int, input().split())
numbers_as_input = [list(map(int, input().split())) for n in range(p)]
a = int(input())

numbers_as_input.sort(key=lambda x: x[a])

for line in numbers_as_input:
    print(*line, sep=' ')
