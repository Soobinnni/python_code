# 파이썬 입출력 알아보기

## print()

> 터미널에 데이터를 **출력**합니다.
> 

<aside>
💡 콘솔 창이 아닌 환경에서 파이썬 파일을 실행하는 경우, print문이 있어야 터미널에 출력 결과를 볼 수 있습니다. print는 보통 알고리즘 문제풀이에서 디버깅 용도로 자주 활용합니다.

</aside>

기본적으로 print 함수 안에 인자를 콤마( , )로 구분하면 공백을 기준으로 여러개를 출력할 수 있습니다.

```python
nums = [3, 1, 2, 4, 5]
print(3) # 3
print('3') # 3 (그런데 스트링이 출력됩니다.)
print(nums[0]) # 3
print(type(3)) # int
print(3, 6) # 3 6
```

또한, print는 기본적으로 한 줄 한 줄 세로로 출력되는데, 가로 출력을 원한다면 끝 부분 옵션(end)을 디폴트값인 줄바꿈이 아닌 것으로 지정하면 됩니다.

```python
print(3, end=' ')
print(5)
# 3 5 => 한 줄에 붙여서 출력됨 => 3 뒤에 공백 뒤에 5 출력
```

## input()

> 사용자의 **입력**을 받습니다.
> 

<aside>
💡 기본적으로 파이썬 인터프리터가 input() 함수를 만나게 되는 순간 그 줄에서 다음 줄의 코드를 실행하지 않고 **멈추며**, 사용자의 입력을 기다립니다. 특이한 점은 input만 사용하게 되면 사용자 인풋을 어떻게 하든지 전부 스트링으로 변환하고, 이 값을 할당하여 type함수 안에 넣어 타입을 확인해볼 수 있습니다.

</aside>

```python
num = input() # 키보드 키패드로 숫자를 입력해 보세요.
# 실제로 프린트문은 입력이 끝나고 실행되어 터미널에 결과가 출력됩니다.
print(num, type(num)) # 3 <class 'str'> => 그렇지만 스트링으로 변환됩니다.

# 만약 터미널에 아무것도 안 떠서 뭘 입력해야 할 지 모르겠다면, 안내 문구를 삽입 가능합니다.
num2 = input('여기에 입력해주세요:')
```

그러면 실제로 파이썬 알고리즘 문제에서 공백을 기준으로 여러 입력이 주어지면 어떻게 처리해야 할까요?

int(), map(함수, iterable)을 활용해 변환합니다.

```python
# 만약 인풋이 => 1 2 3 4 5 6일 때, 
# 결과적으로 [1, 2, 3, 4, 5, 6] 이라는 리스트 안의 int자료형으로 변환하고 싶다면?
nums = list(map(int, input().split()))
print(nums) # [1, 2, 3, 4, 5, 6]
```

이 과정을 쪼개서 살펴보면 다음과 같습니다.

> 인풋은 1 2 3 4 5 6을 공백을 포함하여 터미널에 입력해봅니다.
> 

`1` input을 단일로 쓴 경우

```python
nums = input() 
print(nums, type(nums)) # 1 2 3 4 5 6 <class 'str'>
# 사실은 nums에는 '1 2 3 4 5 6'의 스트링이 공백까지 포함한 상태로 들어가 버렸습니다.
```

`2` input과 split을 섞어서 쓴 경우 

⇒ 리스트로 쪼개는 데 까지는 성공했으나, 안의 원소들이 모두 스트링인 문제가 있습니다.

```python
nums = input().split()
print(nums, type(nums)) # ['1', '2', '3', '4', '5', '6'] <class 'list'>
```

`3` map(int, input().split()) 을 쓴 경우

```python
nums = map(int, input().split())
print(nums, type(nums)) # <map object at 0x00000208B2D9F400> <class 'map'>
```

`4` list(map(int, input().split())) 으로 리스트 변환까지 해준 경우 ⇒ 성공!

```python
nums = list(map(int, input().split()))
print(nums, type(nums)) # [1, 2, 3, 4, 5, 6] <class 'list'> ****
```

<aside>
💡 2차원 리스트 받기 ⇒ 리스트내포를 이용합니다. 행렬을 인풋받을 수 있습니다.

</aside>

```python
# 1 2 3 => 1 2 3 을 입력후 엔터
# 4 5 6 => 그다음 4 5 6 입력후 엔터
# 7 8 9 => 그다음 7 8 9 입력후 엔터

nums_matrix = [list(map(int, input().split())) for _ in range(3)]
print(nums_matrix, type(nums_matrix))
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]] <class 'list'>
```