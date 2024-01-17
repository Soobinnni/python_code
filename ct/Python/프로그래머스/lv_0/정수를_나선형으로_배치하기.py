def 정수를_나선형으로_배치하기(n):
    spiral = [[0]* n for _ in range(n)]
    r = c = d = 0
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    for num in range(1, n**2+1):
        spiral[r][c] = num
        nr, nc = r+dr[d], c+dc[d]
        if (nr<0) or (nr>=n) or (nc<0) or (nc>=n) or (spiral[nr][nc]!=0): 
            d = (d+1) % 4
            nr, nc = r+dr[d], c+dc[d]
        r, c = nr, nc
        
    return spiral