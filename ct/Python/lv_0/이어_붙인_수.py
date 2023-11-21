def 이어_붙인_수(num_list):
    odd = even = ""
    for num in num_list:
        if num % 2 == 0:
            even += f"{num}"
        else:
            odd += f"{num}"
    
    return int(even) + int(odd)