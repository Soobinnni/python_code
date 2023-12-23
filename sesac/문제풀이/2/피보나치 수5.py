# https://www.acmicpc.net/problem/10870

N = int(input())
def fibonacci(s, e, n):
    global N
    if n == N:
        print(s)
        return

    fibonacci(e, s+e, n+1)

def fibo(N):
    if N <= 1:
        return N

    return fibo(N - 1) + fibo(N - 2)

def main():
    print(fibo(N))
    fibonacci(0, 1, 0)

if __name__ == '__main__': main()