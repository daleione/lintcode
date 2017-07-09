class Solution:
    # @param {string} s a string
    # @param {string} p a non-empty string
    # @return {int[]} a list of index
    def findAnagrams(self, s, p):
        lp = len(p)
        result = []
        for i in range(len(s)-lp+1):
            if Solution.string_to_dic(s[i:i+lp]) == Solution.string_to_dic(p):
                result.append(i)
        return result

    @staticmethod
    def string_to_dic(s):
        if not s:
            return {}
        else:
            result = {}
            for c in s:
                if c not in result:
                    result[c] = 1
                else:
                    result[c] += 1
            return result


if __name__ == '__main__':
    solution = Solution()
    s = "cbaebabacd"
    p = "abc"
    s = "abab"
    p = "ab"
    print solution.findAnagrams(s, p)
