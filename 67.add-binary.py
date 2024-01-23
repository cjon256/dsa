class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def binfmt(n):
            if n == 0:
                return "0"
            binstr = ""
            while n > 0:
                if n % 2 == 0:
                    binstr = "0" + binstr
                else:
                    binstr = "1" + binstr
                n = n // 2
            return binstr

        return binfmt(int(a, 2) + int(b, 2))
