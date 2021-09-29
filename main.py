"""
CMPS 2200  Recitation 1
"""

### the only imports needed are here
import tabulate
import time
###

def linear_search(mylist, key):
	""" done. """
	for i,v in enumerate(mylist):
		if v == key:
			return i
	return -1

def test_linear_search():
	""" done. """
	assert linear_search([1,2,3,4,5], 5) == 4
	assert linear_search([1,2,3,4,5], 1) == 0
	assert linear_search([1,2,3,4,5], 6) == -1

def binary_search(mylist, key):
	""" done. """
	return _binary_search(mylist, key, 0, len(mylist)-1)

def _binary_search(mylist, key, left, right):

	if left > right:
		return -1
	Mid = (left + right) // 2

	if key == mylist[Mid]:
		return Mid
	if key < mylist[Mid]:
		return _binary_search(mylist, key, left, Mid-1)
	else:
		return _binary_search(mylist, key, Mid+1, len(mylist)-1)




	### TODO


def test_binary_search():
	assert binary_search([1,2,3,4,5], 5) == 4
	assert binary_search([1,2,3,4,5], 1) == 0
	assert binary_search([1,2,3,4,5], 6) == -1
	assert binary_search([1,2,3,4,5], 3) == 2
	assert binary_search([1,2,3,4,5], 7) == -1





def time_search(search_fn, mylist, key):

	t0 = time.time() * 1000
	search_fn(mylist, key)
	t1 = time.time() * 1000
	total = t1-t0
	return total

	### TODO


def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):

	tup = []
	for i in sizes:
		t1 = []
		l1 = []
		for k in range(int(i)):
			l1.append(i)
		linear_search_time = time_search(linear_search, l1, -1)
		binary_search_time = time_search(binary_search, l1, -1)

		t1.append(int(i))
		t1.append(linear_search_time)
		t1.append(binary_search_time)
		tup.append(t1)

	return tup




	### TODO

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
		headers=['n', 'linear', 'binary'],
		floatfmt=".3f",
		tablefmt="github"))

def test_compare_search():
	res = compare_search(sizes=[10, 100])
	print(res)
	assert res[0][0] == 10
	assert res[1][0] == 100
	assert res[0][1] < 1
	assert res[1][1] < 1

print_results(compare_search())
