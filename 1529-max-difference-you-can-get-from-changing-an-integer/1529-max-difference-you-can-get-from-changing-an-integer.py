class Solution:
    def maxDiff(self, num: int) -> int:
        num_str=str(num) 
        if len(num_str)==1:
                return 8
        elif str(num)[0]!="9" and str(num)[0]!="1":
            t=num_str[0]
            k=num_str.replace(t,'9')  
            min_k=num_str.replace(t,'1')  
            return int(k)-int(min_k)
        elif str(num)[0]=="1":
            t=num_str
            k=num_str
            k=k.replace('1','9')
            for i in num_str:
                if i!='1' and i!='0':
                    t=t.replace(i,'0')
                    break
            return int(k)-int(t)
        else:
            t=num_str
            for i in num_str:
                if i!="9":
                    t=t.replace(i,'9')
                    break
            k=num_str
            k=k.replace('9','1')
            return int(t)-int(k)        
                    



        