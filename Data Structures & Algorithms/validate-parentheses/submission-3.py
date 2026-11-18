class Solution:
    def isValid(self, s: str) -> bool:
        obj = {')': '(', '}': '{', ']': '['}
        stack = []
        for b in s:
            if b in obj:
                if stack and obj[b] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        return not stack
        # Brute Method
        while "[]" in s or "()" in s or "{}" in s:
            s = s.replace('[]', '')
            s = s.replace('{}', '')
            s = s.replace('()', '')
        
        return s == ''
