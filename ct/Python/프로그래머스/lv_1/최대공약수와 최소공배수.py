def find_gcd_lcd(n,m):
    gcd = find_gcd(n,m)
    return gcd, (n * m)/gcd

def find_gcd(n,m):
    while m > 0:
        n, m = m, n%m
    return n

def solution(n, m):
    return list(find_gcd_lcd(n, m))