# 회문검사 함수

def check_palindrome(w):
    l = 0
    r = len(w) - 1

    while l < r:
        if w[l] != w[r]:
            return False
        
        l += 1
        r -= 1

    return True