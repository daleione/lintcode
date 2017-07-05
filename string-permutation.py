# -*- coding: utf-8 -*-
# http://www.lintcode.com/zh-cn/problem/string-permutation/


class Solution:
    # @param {string} A a string
    # @param {string} B a string
    # @return {boolean} a boolean
    def stringPermutation(self, A, B):
        if len(A) != len(B):
            return False

        def h(A):
            d = {}
            for i in A:
                if i not in d:
                    d[i] = 1
                else:
                    d[i] = d[i] + 1
            return d

        if h(A) == h(B):
            return True
        else:
            return False
