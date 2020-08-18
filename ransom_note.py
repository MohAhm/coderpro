from collections import defaultdict

# Time: O(n) + O(m), Linear
# Space: O(k), Constant

class Solution(object):
    def canSpell(self, magazine, note):
        letters = defaultdict(int)

        for c in magazine:
            letters[c] += 1

        for c in note:
            if letters[c] <= 0:
                return False

            letters[c] -= 1

        return True


magazine = ['a', 'b', 'c', 'd', 'e', 'f']
note1 = 'bed'
note2 = 'cat'

print(Solution().canSpell(magazine, note1))
# True

print(Solution().canSpell(magazine, note2))
# False