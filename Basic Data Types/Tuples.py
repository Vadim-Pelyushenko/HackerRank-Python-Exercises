#!/bin/python3

import sys

if __name__ == '__main__':
	N = int(input())
	integer_list = map(int, input().split())
	t = tuple(integer_list)
	print(hash(t))
