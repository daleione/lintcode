class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    # @param {TreeNode} root the root of binary tree
    # @param {int} target an integer
    # @return {int[][]} all valid paths
    def binaryTreePathSum(self, root, target):
        result = []
        if root is None:
            return result
        stack = []
        Solution.helper(result, stack, root, 0, target)
        return result

    @staticmethod
    def helper(result, stack, root, sum_, target):
        sum_ += root.val
        stack.append(root.val)
        if sum_ == target and root.left is None and root.right is None:
            result.append(stack[:])
            stack.pop()
            return
        else:
            if root.left is not None:
                Solution.helper(result, stack, root.left, sum_, target)
            if root.right is not None:
                Solution.helper(result, stack, root.right, sum_, target)
            stack.pop()


def main():
    t = TreeNode(1)
    l1 = TreeNode(2)
    r1 = TreeNode(4)
    t.left = l1
    t.right = r1
    l21 = TreeNode(2)
    l22 = TreeNode(3)
    l1.left = l21
    l1.right = l22

    s = Solution()
    result = s.binaryTreePathSum(t, 5)
    print result


if __name__ == '__main__':
    main()
