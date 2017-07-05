# -*- coding: utf-8 -*-
# http://www.lintcode.com/zh-cn/problem/first-position-unique-character/


class Solution:
    # @param {string} s a string
    # @return {int} it's index
    def firstUniqChar(self, s):
        if not s:
            return -1
        counters = {}
        order = []
        for c in s:
            if c in counters:
                counters[c] += 1
            else:
                counters[c] = 1
                order.append(c)
        for c in order:
            if counters[c] == 1:
                print c
                return s.index(c)
        return -1


if __name__ == '__main__':
    solution = Solution()

    with open('/Users/dalei/Downloads/5.text') as f:
        s = f.read()

    print solution.firstUniqChar(s)
