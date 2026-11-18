class Solution:
    def isValid(self, s: str) -> bool:
        # obj = {
        #     '(': ')',
        #     '{': '}',
        #     '[': ']'
        # }
        # half_length = int(len(s)/2)
        # for n in range(half_length):
        #     if not (s[n] in obj and s[-1-n] == obj[s[n]]):
        #         return False
        #     elif not (s[n+1] in obj and s[n+1] == obj[s[n]]):
        #         return False

        while "[]" in s or "()" in s or "{}" in s:
            s = s.replace('[]', '')
            s = s.replace('{}', '')
            s = s.replace('()', '')
        
        return True if s == '' else False
        # return True if half_length > 0 else False
