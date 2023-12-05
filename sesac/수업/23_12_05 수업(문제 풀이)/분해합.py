num = int()

start = num - max(1, (9 * len(str(num))))

for n in range(start, N+1):
    disassemble_sum = num + sum(map(int, str(num)))

    if disassemble_sum == N:
        print(num)
        break

else:
    print(0)


# 제공된 코드에서 `else` 키워드는 `for` 루프에 해당합니다. 이 코드는 `for` 루프가 완전히 실행된 후에 실행됩니다. `for` 루프가 `break` 문에 의해 중단되지 않으면 `else` 블록이 실행됩니다.
# 여기서 주의해야 할 점은 `else` 블록이 `for` 루프와 함께 사용될 때는 "루프가 정상적으로 완료되었을 때" 실행된다는 것입니다. 즉, `break` 문에 의해 루프가 중단되면 `else` 블록은 실행되지 않습니다.
# 따라서 제공된 코드에서는 `for` 루프가 `break` 문에 의해 중단되지 않으면 `else` 블록이 실행되어 `print(0)`이 출력됩니다.