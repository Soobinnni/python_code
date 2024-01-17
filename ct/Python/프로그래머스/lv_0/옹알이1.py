from itertools import permutations
possible_bubbling = ["aya", "ye", "woo", "ma"]
def find(b):
	if b in possible_bubbling:
		return 1
	if b in [w1+w2 for w1, w2 in permutations(possible_bubbling, 2)]:
		return 1
	if b in [w1+w2+w3 for w1, w2, w3 in permutations(possible_bubbling, 3)]:
		return 1
	if b in [w1+w2+w3+w4 for w1, w2, w3, w4 in permutations(possible_bubbling, 4)]:
		return 1
	return 0

def 옹알이1(bubbling):
	answer = 0
	for b in bubbling:
		answer += find(b)
	return answer

def 남이쓴_옹알이1(bubbling):
	answer = 0
	for b in bubbling:
		for p in possible_bubbling:
			b = b.replace(p, ' ')
		if not b.strip():
			answer += 1
	return answer