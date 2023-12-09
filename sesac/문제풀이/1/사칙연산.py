num1, num2 = map(int, input().split())
op_list = ["+", "-", "*", "//", "%"]
for op in op_list:
    print(f"""{eval(f"{num1}{op}{num2}")}""")