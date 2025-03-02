class Solution:
    def mergeArrays(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        return sorted((Counter(dict(a))+Counter(dict(b))).items())