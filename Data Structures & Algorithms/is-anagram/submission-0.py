class Solution:
    
    def isAnagram(self, s: str, t: str) -> bool:

        # Length check
        if len(s) != len(t):
            return False

        # Populate the string frequency dictionaries 
        freq_s, freq_t = {}, {}
        for i in range(len(s)):
            freq_s[s[i]] = freq_s.get(s[i], 0) + 1
            freq_t[t[i]] = freq_t.get(t[i], 0) + 1

        # Using freq_s to iterate because lengths have been verified 
        for letter in freq_s:

            # If, for any letter, thee frequency doesn't match,
            # it's not an anagram, return false.
            if freq_t.get(letter, 0) != freq_s[letter]:
                return False
        
        # If you process the entire dictionary, 
        # and each letter has the same frequency, 
        # you have an anagram.
        return True
        
