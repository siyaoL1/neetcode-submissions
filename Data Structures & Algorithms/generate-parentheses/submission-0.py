class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def helper(to_open, to_close, curr):
            if to_open == 0 and to_close == 0:
                res.append(curr)
            
            if to_open:
                helper(to_open - 1, to_close + 1, curr + "(")
            if to_close:
                helper(to_open, to_close - 1, curr + ")")
        
        helper(n, 0, "")
        return res