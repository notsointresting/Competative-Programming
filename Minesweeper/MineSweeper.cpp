#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    int N, M;
    vector<string> lst;
    
    while (true) {
        // N - Number of lines, M - Number of Columns
        cout << "Enter N and M---> ";
        cin >> N >> M;
        if (N == 0 && M == 0) {
            break;
        }
        
        // Getting input from user as string and storing it into list.
        lst.clear();
        for (int i = 0; i < N; i++) {
            string s;
            cin >> s;
            lst.push_back(s);
        }
        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                // Check if the cell is a safe cell ( means not mine *)
                if (lst[i][j] == '.') {
                    // Initialize a counter to count the number of adjacent mines
                    int cnt = 0;

                    // i-1 to i+2 means previous row, current row and current row+1
                    for (int r = i-1; r <= i+1; r++) {
                        // j-1 to j+2 means previous col of previous row, current col of current row and current col +1 of current col +1
                        for (int c = j-1; c <= j+1; c++) {
                            // If the adjacent cell is a mine, increment the counter
                            if (r >= 0 && r < N && c >= 0 && c < M && lst[r][c] == '*') {
                                cnt++;
                            }
                        }
                    }
                    
                    // Update the current cell with the count of adjacent mines
                    lst[i][j] = cnt + '0';
                }
            }
        }
        
        cout << endl;
        for (int i = 0; i < N; i++) {
            cout << lst[i] << endl;
        }
    }
    
    return 0;
}
