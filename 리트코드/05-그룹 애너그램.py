import collections

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = collections.defaultdict(list)

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        
        # print(anagrams)
        return list(anagrams.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution.groupAnagrams(0, strs))