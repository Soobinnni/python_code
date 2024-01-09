# https://www.acmicpc.net/problem/2525

hour, minute = map(int, input().split())
taken_minute = int(input())

taken_minute = minute + taken_minute

res_hour = (hour + (taken_minute // 60)) % 24
res_minute = taken_minute % 60

print(res_hour, res_minute)