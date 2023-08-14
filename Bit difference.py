class Solution:
    def countBitsFlip(self, a, b):
        a = bin(a)[:1:-1]
        b = bin(b)[:1:-1]
        out = 0
        if len(a) < len(b):
            a = a + ("0" * (len(b) - len(a)))
        elif len(b) < len(a):
            b = b + ("0" * (len(a) - len(b)))
        for i in range(len(a)):
            if a[i] != b[i]:
                out += 1
        return out


a = 34
b = 7
ob = Solution()
print(ob.countBitsFlip(a, b))
