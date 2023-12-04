T = int(input())
palindrome = []
def find_palindrome(arr):
    for i in range(1, len(arr)):
        for j in range(i, len(arr)):
            test_word = arr[i-1] + arr[j]
            test_word2 = arr[j] + arr[i-1]
            if test_word == test_word[::-1]:
                return test_word
            if test_word2 == test_word2[::-1]:
                return test_word2
    return 0

for _ in range(T):
    len_words = int(input())
    words = [input().strip() for _ in range(len_words)]
    palindrome.append(find_palindrome(words))

for p in palindrome:
    print(p)