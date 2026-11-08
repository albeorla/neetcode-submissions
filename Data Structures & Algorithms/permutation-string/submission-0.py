# LC 0567 Permutation In String (Medium, Sliding Window). Rep 6 under the Coding Interview Driver.
# Google medium rules: nothing runs until the Prove beat declares this correct.


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """LC 0567 Permutation In String.

        Problem (as on LeetCode): Given two strings s1 and s2, return true if s2
        contains a permutation of s1, or false otherwise. In other words, return
        true if one of s1's permutations is a substring of s2.

        Example 1: s1 = "ab", s2 = "eidbaooo" -> true  ("ba" is in s2)
        Example 2: s1 = "ab", s2 = "eidboaoo" -> false

        Constraints: 1 <= len(s1), len(s2) <= 10,000. Only lowercase English letters.

        Steps: (write them here, in your own words, before any code)
        1. Set m = len(s1) and n = len(s2). If m > n, return false (no window fits).
        2. Count the letters of s1. Count the letters of the first window (the
           first m letters of s2, indexes 0 to m - 1). If the two counts are
           equal, return true. If not, go on to the loop.
        3. Loop over the starts s from 1 up to but not including n - m + 1
           (so s runs from 1 to n - m).
        4. At each start s, slide the window: the letter at index s - 1 leaves
           (its count goes down by 1), and the letter at index s + m - 1 enters
           (its count goes up by 1). Then compare the counts. If they are equal,
           return true.
        5. Return false if none of the windows matched.
        """
        m, n = len(s1), len(s2)
        if m > n: return False

        s1_counts = [0] * 26
        window_counts = [0] * 26

        for i in range(m):
            s1_counts[ord(s1[i]) - ord("a")] += 1
            window_counts[ord(s2[i]) - ord("a")] += 1

        if s1_counts == window_counts:
            return True

        for i in range(1, n - m + 1):
            window_counts[ord(s2[i-1]) - ord("a")] -= 1
            window_counts[ord(s2[i+m-1]) - ord("a")] += 1
            if s1_counts == window_counts:
                return True

        return False