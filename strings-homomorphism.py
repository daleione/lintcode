# -*- coding: utf-8 -*-
# http://www.lintcode.com/zh-cn/problem/strings-homomorphism/


class Solution:
    # @param {string} s a string
    # @param {string} t a string
    # @return {boolean} true if the characters in s
    # can be replaced to get t or false
    def isIsomorphic(self, s, t):
        def h(string):
            l = [0] * 1000
            s = set()
            for c in string:
                i = string.index(c)
                if c not in s:
                    l[i] = 1
                    s.add(c)
                else:
                    l[i] += 1

            return l
        if h(s) == h(t):
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print s.isIsomorphic("foo", "bar")
