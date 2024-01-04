# https://www.acmicpc.net/problem/10773

nums = []

for _ in range(int(input())):
    num = int(input())
    nums.append(num) if num != 0 else nums.pop()

print(sum(nums))
