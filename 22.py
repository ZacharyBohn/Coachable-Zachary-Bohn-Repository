class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return self.genParanths(n, 0, 0)
    
    def genParanths(self, n: int, used_opens: int, used_closes: int, prefix="") -> List[str]:
        available_opens = n - used_opens
        available_closes = min(used_opens - used_closes, (n - used_closes))
        if available_opens == 0 and available_closes == 0:
            return [prefix]
        res = []
        if available_opens > 0:
            res += self.genParanths(n, used_opens + 1, used_closes, prefix + "(")
        if available_closes > 0:
            res += self.genParanths(n, used_opens, used_closes + 1, prefix + ")")
        return res