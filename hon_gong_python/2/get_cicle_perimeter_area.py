pi = 3.14
def get_perimeter(radius):
    perimeter = 2 * radius * pi
    return perimeter
def get_area(radius):
    area = (radius ** 2) * pi
    return area

input_radius = int(input('원의 반지름을 입력하세요 :'))
perimeter = get_perimeter(input_radius)
area = get_area(input_radius)

print(f"입력한 반지름 : {input_radius}\n원의 둘레 : {perimeter}\n원의 넓이 : {area}")


# -------------------------
r = input('반지름 : ')
r = float(r)

#처리
pi = 3.14
perimeter_ = 2 * pi * r
area_ = pi * ( r ** 2 )

#출력
print(f" 둘레 : {perimeter_}")
print(f" 넓이 : {area_}")