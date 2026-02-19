from typing import List, Optional

from bintree import Tree, TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        middle = len(nums) // 2
        node = TreeNode(nums[middle])
        node.left = self.sortedArrayToBST(nums[0:middle])
        node.right = self.sortedArrayToBST(nums[middle+1:])

        return node





nums = [-10,-3,0,5,9]

print(f"{nums=}")
t = Tree(root=Solution().sortedArrayToBST(nums))
t.draw()
print("--------------------------------------------------")

nums = [1,3]
print(f"{nums=}")
t = Tree(root=Solution().sortedArrayToBST(nums))
t.draw()
