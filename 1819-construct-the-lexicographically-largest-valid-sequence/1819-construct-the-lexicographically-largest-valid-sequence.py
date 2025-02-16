class Solution:
    def constructDistancedSequence(self,n:int)->List[int]:
        l=2*n-1
        seq=[0]*l
        used=set()
        def bt(idx):
            if idx==l:
                return True
            if seq[idx]:
                return bt(idx+1)

            for num in range(n,0,-1):
                if num in used:
                    continue
                nxt_idx=idx+num if num>1 else idx
                if nxt_idx>=l or seq[nxt_idx]!=0:
                    continue
                seq[idx]=seq[nxt_idx]=num
                used.add(num)
                if bt(idx+1):
                    return True
                seq[idx]=seq[nxt_idx]=0
                used.remove(num)
            return False

        bt(0)
        return seq
