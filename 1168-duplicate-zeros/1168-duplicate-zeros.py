class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        z=arr.count(0)
        n=len(arr)
        for i in range(n-1,-1,-1):
            if i+z<n:
                arr[i+z]=arr[i]
            if arr[i]==0:
                z-=1
                if i+z<n:
                    arr[i+z] = 0
