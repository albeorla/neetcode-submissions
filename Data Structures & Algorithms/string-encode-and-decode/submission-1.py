class Solution:

    def encode(self, strs: List[str]) -> str:
       
        res = []
        
        for s in strs:
            chunk = str(len(s)) + "#" + s
            res.append(chunk)

        return "".join(res)

    def decode(self, s: str) -> List[str]:
        
        i = 0
        res = []

        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            word_start = j + 1
            word_end = j + 1 + length
            word = s[word_start : word_end]
            res.append(word)
            i = word_end

        return res
            