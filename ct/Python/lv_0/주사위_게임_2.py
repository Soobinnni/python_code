def 주사위_게임_2(a, b, c):
    answer = 0
    l = len(set([a,b,c]))
    if l == 1:
        answer = (a + b + c) * (a ** 2 + b ** 2 + c ** 2 ) * (a ** 3 + b ** 3 + c ** 3 )
    if l == 2:
        answer = (a + b + c) * (a ** 2 + b ** 2 + c ** 2 )
        
    if l == 3:
        answer = (a + b + c)
        
from math import prod

def 두번째_생각해본_답_주사위_게임_2(a, b, c):
    return prod(((a ** (i + 1)) + (b ** (i + 1)) + (c ** (i + 1))) for i in range( 4 - len(set([a,b,c]))))