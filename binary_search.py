
def binary_search(lst, x):
	lst.sort()
	p = 0
	r = len(lst) - 1
	answer = None
	while p <= r:
		q = (p + r) // 2
		if lst[q] == x:
			answer = q
			break
		elif lst[q] > x:
			r = q - 1
		elif lst[q] < x:
			p = q + 1

	
	return answer

if __name__ == '__main__':
	print('='*10, binary_search([0, 1, 2, 3, 4], 2), sep='\n')