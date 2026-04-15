class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            sorted_chars = sorted(word)
            anagram = ''.join(sorted_chars)
            anagrams[anagram].append(word)

        return list(anagrams.values())