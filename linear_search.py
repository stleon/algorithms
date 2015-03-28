
def linear_search_1(lst, x):
	result = None
	for index, string in enumerate(lst):
		#print(index, string)
		if string == x:
			result = index
	return result

def linear_search_2(lst, x):
	i = 0
	while i < len(lst) and lst[i] != x:
		#print(i)
		i += 1
	return i if i < len(lst) else None

def linear_search_3(lst, x):
	lst.append(x)
	i = 0
	while lst[i] != x:
		#print(i)
		i += 1
	return i if i < len(lst) - 1 else None

if __name__ == '__main__':
	a = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
	print('='*10, linear_search_3(a, 'y'), sep='\n')