n = int(input())
meeting_room_timelines = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: [x[1], x[0]])
end_time = meeting_room_timelines[0][1]
cnt = 1

for i in range(1, n):
    if end_time <= meeting_room_timelines[i][0]:
        end_time = meeting_room_timelines[i][1]
        cnt += 1

print(cnt)