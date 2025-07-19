import unittest

class Solution:
	def calculate(self, s: str) -> int:
		cleaned_string = ''.join(char for char in s if not char.isspace())
		OPERATORS = set(['+', '-', '*', '/'])
		stack = [0]
		cur_num = 0
		last_operator = '+'
		for i in range(len(cleaned_string)+1):
			if i == len(cleaned_string):
				char = '+'
			else:
				char = cleaned_string[i]

			if char in OPERATORS:
				if last_operator == '*':
					stack[-1] *= cur_num
					oper = '*'
				elif last_operator == '/':
					# int() truncates towards 0
					# // truncates down
					stack[-1] = int(stack[-1] / cur_num)
				elif last_operator == '+':
					stack.append(cur_num)
				else:
					stack.append(-cur_num)
				last_operator = char
				cur_num = 0
			else:
				# char is digit
				cur_num *= 10
				cur_num += int(char)
			
			if len(stack) == 3:
				stack[0] += stack[1]
				stack[1] = stack.pop()
		
		return sum(stack)
			

'''
loop through s
skip white space
track:


# 20 + 30 * 2 * 2 / 2 + 100
#           ^

answer = 0
oper = *
cur_num = 2
q = [('+', 20), ('+', 30)]

on digit:

s = '3 + 4 + 5'
              ^
q = [+3, +4]

if char is white space:
	skip
if char is oper:
	add num to q
if char is digit:
	update current number

on end:
	add current number to q
	finish processing q

last_operator  = '+'

first num for adding, second for mult
stack = [0, 0]
for c in s:
	if white space: skip
	if oper: process previous stuff
		if oper is *:
			mult last num of stack by cur num
		if oper is /:
			same as aboef
		if oper is + or -:
			just add to stack
	if digit: update cur num
	if stack is len 3:
		stack[0] += stack[1]
		stack[1] = stack.pop()

3 + 4 * 6 ^ 2 + 6

'''

class TestCases(unittest.TestCase):
	def test_case_1(self):
		sol = Solution()
		self.assertEqual(sol.calculate("3+2*2"), 7)

	def test_case_2(self):
		sol = Solution()
		self.assertEqual(sol.calculate(" 3/2 "), 1)

	def test_case_3(self):
		sol = Solution()
		self.assertEqual(sol.calculate(" 3+5 / 2 "), 5)

	def test_case_4(self):
		sol = Solution()
		self.assertEqual(sol.calculate("14-3/2"), 13)

	def test_case_5(self):
		sol = Solution()
		self.assertEqual(sol.calculate("100+200*3-50/2"), 675)

if __name__ == "__main__":
	unittest.main()
