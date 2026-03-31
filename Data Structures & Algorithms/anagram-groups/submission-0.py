class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams: List = []
        anagramsMap = defaultdict(list)
        for string in strs:
            anagramsMap[tuple(sorted(string))].append(string)
        for ana in anagramsMap.values():
            anagrams.append(ana)

        return anagrams
