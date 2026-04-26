class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Frequency Map Phase
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
    
        # Bucket Lists Phase
        buckets = [[] for _ in range(len(nums) + 1)]
        for val, count in freq.items():
            buckets[count].append(val)

        # Top-K Extraction Phase
        top_k = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                top_k.append(num)
                if len(top_k) == k:
                    return top_k
                