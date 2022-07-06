import sys

n = int(sys.stdin.readline())
num_list = [0] * 10000

for _ in range(n):
    input_num = int(sys.stdin.readline())

    num_list[input_num - 1] += 1

for i in range(10000):
    if num_list[i] != 0:
        for _ in range(num_list[i]):
            print(i + 1)