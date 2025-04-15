class Solution:
	def generateParenthesis(self, n: int) -> List[str]:
		return self.generate(n, 0, 0, "")
	
	def generate(
		self,
		n: int, 
		used_opens: int,
		used_closes: int,
		prefix,
		) -> List[str]:
		num_opens = n - used_opens
		num_closes = min(used_opens - used_closes, (n - used_closes))
		if num_opens == 0 and num_closes == 0:
			return [prefix]
		res = []
		if num_opens > 0:
			res += self.generate(n, used_opens + 1, used_closes, prefix + "(")
		if num_closes > 0:
			res += self.generate(n, used_opens, used_closes + 1, prefix + ")")
		return res