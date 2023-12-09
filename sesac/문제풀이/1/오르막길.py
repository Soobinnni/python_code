road = [int(input()) for _ in range(int(input()))]
uphill_roads = []
uphill_road = []
start = -1

for r in road:
    if start < r:
        uphill_road.append(r)
        start = r
    else:
