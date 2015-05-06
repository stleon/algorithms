
def selection_sort(lst):
	n = len(lst)
	i = 0

	while i < n - 1:
		smallest = i
		j = i + 1
		
		while j < n:
			if lst[j] < lst[smallest]:
				smallest = j # находим наименьшее число
			j+=1
		
		lst[i], lst[smallest] = lst[smallest], lst[i] # меняем местами, наименьшее "вначало"

		print(lst)

		i+=1
	
	return lst

if __name__ == '__main__':
	print('='*10, selection_sort([4, 2, 0, 1, 5, 3]), sep='\n')