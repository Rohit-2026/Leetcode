class Solution {
public:
    const int N=1e9+7;
    int dp[1001][1001][2];
    int numberOfStableArrays(int zero, int one, int limit) {
        for(int i=0;i<=min(limit,max(one,zero));i++){
            dp[i][0][0]=dp[0][i][1]=1;
        }
        for(int i=1;i<=zero;i++){
            for(int j=1;j<=one;j++){
                dp[i][j][0]=((long long)dp[i-1][j][0]+dp[i-1][j][1])%N;
                dp[i][j][1]=((long long)dp[i][j-1][1]+dp[i][j-1][0])%N;
                
                if(i-1-limit>=0) dp[i][j][0]=dp[i][j][0]-dp[i-1-limit][j][1];
                if(j-1-limit>=0) dp[i][j][1]=dp[i][j][1]-dp[i][j-1-limit][0];
                if(dp[i][j][0]<0) dp[i][j][0]+=N;
                if(dp[i][j][1]<0) dp[i][j][1]+=N;
            }
        }
        return ((long long)dp[zero][one][1]+dp[zero][one][0])%N;
    }
};