class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_stack = []
        temp_indicies = {}
        res = [0] * len(temperatures)
        for i in range(len(temperatures) - 1, -1, -1):
            temp = temperatures[i]
            while len(temp_stack) != 0 and temp >= temp_stack[-1]:
                temp_stack.pop()
            if len(temp_stack) == 0:
                res[i] = 0
            elif temp < temp_stack[-1]:
                res[i] = temp_indicies[temp_stack[-1]] - i
            temp_stack.append(temp)
            temp_indicies[temp] = i
        return res