class Solution {
public:
    int numberOfSubmatrices(vector<vector<char>>& grid) {
        int rows = grid.size(), cols = grid[0].size();
        
        vector<int> diff(cols, 0);   // stores (countX - countY)
        vector<int> hasX(cols, 0);   // whether rectangle has at least one X
        
        int ans = 0;

        for (int i = 0; i < rows; i++) {
            int rowDiff = 0;   // current row prefix diff
            int rowHasX = 0;   // whether current row prefix has X

            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 'X') {
                    rowDiff++;
                    rowHasX = 1;
                } 
                else if (grid[i][j] == 'Y') {
                    rowDiff--;
                }

                diff[j] += rowDiff;
                hasX[j] |= rowHasX;

                if (hasX[j] && diff[j] == 0) {
                    ans++;
                }
            }
        }

        return ans;
    }
};