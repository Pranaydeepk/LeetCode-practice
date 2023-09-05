# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Morris Traversal
        # answer, curr = [], root
        # while curr:
        #     if not curr.left:
        #         answer.append(curr.val)
        #         curr = curr.right
        #     else:
        #         last = curr.left
        #         while last.right and last.right != curr:
        #             last = last.right
        #         if not last.right:
        #             answer.append(curr.val)
        #             last.right = curr
        #             curr = curr.left
        #         else:
        #             last.right = None
        #             curr = curr.right
        # return answer
        # # Iteration ------------------
        # T - O(n) 
        # S - O(n)
        # ----------------------------
        answer, stack = [], [root]
        while stack:
            curr = stack.pop()
            if curr:
                answer.append(curr.val)
                stack.append(curr.right)
                stack.append(curr.left)
        return answer
        # Recursion ------------------
        # T - O(n) 
        # S - O(n)
        # ----------------------------
        # answer = []
        # def dfs(node):
        #     if node is None:
        #         return
        #     answer.append(node.val)
        #     dfs(node.left)
        #     dfs(node.right)
        # dfs(root)
        # return answer
        # ----------------------------