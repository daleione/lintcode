# -*- coding: utf-8 -*-
# http://www.lintcode.com/zh-cn/problem/guess-number-game/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# you can call Guess.guess(num)


class Solution:
    # @param {int} n an integer
    # @return {int} the number you guess
    def guessNumber(self, n):
        left, right = 1, n
        guss = (left + right)/2
        guss_ret = Guess.guess(guss)
        while guss_ret != 0:
            if guss_ret < 0:
                right = guss - 1  # must -1 + 1, because (6+7)/2 = 6
            else:
                left = guss + 1
            guss = (left + right) / 2
            guss_ret = Guess.guess(guss)
        return guss


if __name__ == '__main__':
    solution = Solution()
    print solution.guessNumber(10)
