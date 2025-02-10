#include <iostream>
#include <string>
#include <vector>
#include <cmath>
using namespace std;
//2 will be used to display the solution path 
// 1 will be used to display the paths that are not part of the solution
// 0 will be used to display the walls
void print_maze(int (&matrix)[15][15]) {
    for (int i = 0; i < 15; i++) {
        for (int j = 0; j < 15; j++) {
            if (matrix[i][j] == 0) {
                std::cout << " # ";
            } else  {
                std::cout << " . ";
            } 
        }
        std::cout << std::endl;
    }
}
void print_solution(int (&matrix)[15][15]) {
    for (int i = 0; i < 15; i++) {
        for (int j = 0; j < 15; j++) {
            if (matrix[i][j] == 0) {
                std::cout << " # ";
            } else if (matrix[i][j] == 1) {
                std::cout << " . ";
            } else {
                std::cout << " | ";
            }
        }
        std::cout << std::endl;
    }
}

void generate_entry_exit(int (&matrix)[15][15], int &entry, int &exit) {
    entry = rand() % 13 + 1;
    matrix[0][entry] = 2;
    exit = rand() % 13 + 1;
    matrix[14][exit] = 2;

}
void generate_solution(int (&matrix)[15][15], int entry, int exit) {
    vector<int> core_path; 
    core_path.push_back(entry);


    for (int i = 1; i < 14; i++) {
        int next_col = rand() % 13 + 1;
        core_path.push_back(next_col);
    }
    int prev_col = entry;
    core_path.push_back(exit); 
    for (int i = 1; i <= 13; i++) {
        int current_col = core_path[i];
        prev_col = core_path[i - 1];
        int start = min(prev_col, current_col);
        int end = max(prev_col, current_col);
        if (i == 13) {
            start = min(prev_col, exit);
            end = max(prev_col, exit);
        }
        if (i % 2 == 0) {
            current_col = prev_col;
            core_path[i] = prev_col;
            matrix[i][current_col] = 2;
        }
        else {
            for (int j = start; j <= end; j++) {
                matrix[i][j] = 2;
            }
        }

    }
}

void generate_decoys(int (&matrix)[15][15]) {
    for (int i = 1; i < 14; i++) {
        for (int j = 1; j < 14; j++) {
            if (matrix[i][j] == 0 && rand() % 4 == 0) { // 25% chance to create a decoy path
                
                // Check if placing a decoy would block a solution path
                bool is_near_solution = false;
                if ((i > 0 && matrix[i - 1][j] == 2) || (i < 14 && matrix[i + 1][j] == 2) ||
                    (j > 0 && matrix[i][j - 1] == 2) || (j < 14 && matrix[i][j + 1] == 2)) {
                    is_near_solution = true;
                }
                
                if (!is_near_solution) {
                    matrix[i][j] = 1;
                    
                    // Randomly extend the path in one direction
                    int direction = rand() % 4;
                    int length = rand() % 3 + 1; // Length of 1 to 3
                    for (int k = 1; k <= length; k++) {
                        int ni = i, nj = j;
                        if (direction == 0) ni -= k; // Up
                        else if (direction == 1) ni += k; // Down
                        else if (direction == 2) nj -= k; // Left
                        else if (direction == 3) nj += k; // Right;
                        
                        if (ni > 0 && ni < 14 && nj > 0 && nj < 14 && matrix[ni][nj] == 0) {
                            matrix[ni][nj] = 1;
                        } else if (matrix[ni][nj] == 2) { // Avoid replacing solution path
                            break;
                        }
                    }
                }
            }
        }
    }
}


using namespace std;
int main() {
    srand(time(0));
    int matrix[15][15] = {0};
    int entry, exit;
    generate_entry_exit(matrix, entry, exit);
    generate_solution(matrix, entry, exit);
    generate_decoys(matrix);
    cout << "Generated maze:" << endl;
    print_maze(matrix);
    cout << endl << "Solution:" << endl;
    print_solution(matrix);

}