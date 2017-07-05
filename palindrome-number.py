# -*- coding: utf-8 -*-
# http://www.lintcode.com/zh-cn/problem/palindrome-number/


class Solution:
    # @param {int} num a positive number
    # @return {boolean} true if it's a palindrome or false
    def palindromeNumber(self, num):
        s = str(num)
        l = list(s)
        l.reverse()
        rs = "".join(l)
        if s == rs:
            return True
        else:
            return False
