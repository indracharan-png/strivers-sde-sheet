from typing import List, Optional


class TrieNode:
    def __init__(self):
        self.children: List[Optional['TrieNode']] = [None, None]  # For bit 0 and bit 1

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = TrieNode()

        # Build Trie
        for num in nums:
            node = root
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                if not node.children[bit]:
                    node.children[bit] = TrieNode()
                node = node.children[bit]

        max_xor = 0

        # Find max XOR
        for num in nums:
            node = root
            curr_xor = 0
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                toggled_bit = 1 - bit
                if node.children[toggled_bit]:
                    curr_xor |= (1 << i)
                    node = node.children[toggled_bit]
                else:
                    node = node.children[bit]
            max_xor = max(max_xor, curr_xor)

        return max_xor
