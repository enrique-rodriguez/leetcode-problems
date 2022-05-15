class Solution:
    def isHappy(self, n: int) -> bool:
        seen = dict()
        number = self.sum_square(n)
        
        while number != 1:
            if number in seen:
                return False
            seen[number] = self.sum_square(number)
            number = seen[number]
        
        return True
    
    def sum_square(self, n):
        if n < 10:
            return n*n
        
        digit = n%10
        
        return digit*digit + self.sum_square(n//10)