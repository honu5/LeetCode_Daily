class Solution {
public:
    int bitwiseComplement(int num) {
        if(num == 0) return 1;
        if(num == 1) return 0;
        int ans=0;
        int cnt=0;
        while(num>0){
            if(num%2 == 0 && num/2!=0){
                ans+=pow(2, cnt);
            }
            cnt++;
            num/=2;
        }
        return ans;
    }
};