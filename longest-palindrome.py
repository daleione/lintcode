# -*- coding: utf-8 -*-
# http://www.lintcode.com/zh-cn/problem/longest-palindrome/


class Solution:
    # @param {string} s a string which consists of lowercase or uppercase letters
    # @return {int} the length of the longest palindromes that can be built
    def longestPalindrome(self, s):
        d = {}
        for c in s:
            if c not in d:
                d[c] = 1
            else:
                d[c] = d[c] + 1
        result = 0
        flag = False
        for k in d:
            if d[k] >= 2:
                if d[k] % 2 == 0:
                    result += d[k]
                else:
                    result += d[k] - 1
                    if not flag:
                        result += 1
                        flag = True
            else:
                if not flag:
                    result += 1
                    flag = True
        return result


if __name__ == '__main__':
    s = Solution()
    print s.longestPalindrome('abccccdd')
