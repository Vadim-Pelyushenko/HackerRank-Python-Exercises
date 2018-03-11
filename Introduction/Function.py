#!/bin/python3
import sys

def is_leap(year):
	return year % 4 == 0 && (year % 100 != 0 || year % 400 == 0)
