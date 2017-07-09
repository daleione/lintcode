# -*- coding: utf-8 -*-
# http://www.lintcode.com/zh-cn/problem/add-digits/


class Solution:
    # @param {int} num a non-negative integer
    # @return {int} one digit
    def addDigits(self, num):
        count = 0
        while True:
            for c in str(num):
                count += int(c)
            if count < 10:
                break
            else:
                num = count
                count = 0
        return count

    def addDigits1(self, num):
        count = 0
        while True:
            while num % 10 > 0:
                count += num % 10
                num = num/10
            if count < 10:
                break
            else:
                num, count = count, 0
        return count


if __name__ == '__main__':
    solution = Solution()
    assert solution.addDigits(38) == 2
    assert solution.addDigits1(38) == 2
