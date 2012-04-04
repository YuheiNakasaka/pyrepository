#isbn_check.py
# -*- coding:utf-8 -*-
import re
import sys

def check(number):
	numlist = []
	sum = 0
	i = 10
	strnumber = str(number)
	matches = re.findall("(\w+)-(\w+)-(\w+)-(\w+)",strnumber)
	#マッチした文字列のmergeとsplit
	strings = matches[0][0] + matches[0][1] + matches[0][2] + matches[0][3]
	for w in strings:
		numlist.append(w)
	#チェックサム
	for numstr in numlist:
		sum += int(numstr) * i
		i -= 1
		if i == 1:
			break
	div = sum % 11
	#余りによってisbnコードの末尾を分岐させる
	if div == 0:
		lastnum = 0
	elif div == 1:
		lastnum = int("x")
	else:
		lastnum = 11 - div
	#isbnコードの正誤チェック
	if lastnum == int(strnumber[-1]):
		result = "True"
	else:
		result = "False"
	return strnumber + " is " + result

def main():
	args = sys.argv[1:]
	for arg in args:
		ans = check(arg)
		print ans

if __name__ == "__main__":
	main()