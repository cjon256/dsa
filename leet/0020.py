class Solution:
    def isValid(self, s: str) -> bool:
        pstack = []
        try:
            for c in s:
                match c:
                    case '(' | '[' | '{':
                        pstack.append(c)
                    case ')':
                        opener = pstack.pop()
                        if opener != '(':
                            return False
                    case ']':
                        opener = pstack.pop()
                        if opener != '[':
                            return False
                    case '}':
                        opener = pstack.pop()
                        if opener != '{':
                            return False
            return not pstack
        except IndexError:
            return False
