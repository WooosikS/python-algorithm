import collections
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        words = [ word for word in re.sub(('[^\w]'), ' ', paragraph).lower().split() if word not in banned ]
        counts = collections.Counter(words)

        return counts.most_common(1)[0][0]

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

print(Solution.mostCommonWord(0, paragraph, banned))