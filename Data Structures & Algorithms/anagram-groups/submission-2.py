class Solution:

    def _get_char_count(self, s: str) -> Tuple[int, ...]:
        counts = [0] * 26
        for char in s:
            counts[ord(char) - ord('a')] += 1
        return tuple(counts)


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        for s in strs:
            char_count = self._get_char_count(s)
            anagrams[char_count].append(s)
        return list(anagrams.values())
