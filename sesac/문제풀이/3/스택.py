# https://www.acmicpc.net/problem/10828
requires = [input() for _ in range(int(input()))]
stack = []
def first():
    for require in requires:
        r = require.split()

        if r[0] == 'push': stack.append(int(r[1]))

        elif r[0] == 'pop': print(stack.pop() if stack else -1)

        elif r[0] == 'size':print(len(stack))

        elif r[0] == 'empty':print(int(bool(not stack)))

        else: print(stack[len(stack)-1] if stack else -1)

def second():
    for require in requires:
        r = require.split()
        if r[0] == 'push':
            stack.append(r[1])
        elif r[0] == 'pop':
            print(stack.pop() if stack else -1)
        elif r[0] == 'size':
            print(len(stack))
        elif r[0] == 'empty':
            print(int(bool(not stack)))
        else:
            print(stack[-1] if stack else -1)

