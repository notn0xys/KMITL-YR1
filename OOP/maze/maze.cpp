#include <iostream>
#include <string>
#include <vector>
#include <cmath>
using namespace std;
// 2 will be used to display the solution path 
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
    //generate all the core path that the app will go through
    int prev_col = entry;
    core_path.push_back(exit); 
    for (int i = 1; i <= 13; i++) {
        int current_col = core_path[i];
        prev_col = core_path[i - 1];
        //from where to loop changing from 0 to 2
        int start = min(prev_col, current_col);
        int end = max(prev_col, current_col);
        if (i == 13) {
            start = min(prev_col, exit);
            end = max(prev_col, exit);
        }
        //every other line will have 1 main path
        if (i % 2 == 0) {
            //if it is the core path will be the same as the end path of the line above
            current_col = prev_col;
            core_path[i] = prev_col;
            matrix[i][current_col] = 2;
        }
        else {
            //otherwise just go from previous core path to the current core path
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
                
                //  check to see if the decoy path is near the solution path
                bool is_near_solution = false;
                if ((i > 0 && matrix[i - 1][j] == 2) || (i < 14 && matrix[i + 1][j] == 2) ||
                    (j > 0 && matrix[i][j - 1] == 2) || (j < 14 && matrix[i][j + 1] == 2)) {
                    is_near_solution = true;
                }
                // if not near a solution path create a decoy path
                if (!is_near_solution) {
                    matrix[i][j] = 1;
                    //to make like a room everytime a decoy path spawn it can increase up to 3 in any direction
                    int direction = rand() % 4;
                    int length = rand() % 3 + 1;
                    for (int k = 1; k <= length; k++) {
                        int verticle = i, horizontal = j;
                        if (direction == 0) {
                            verticle -= k; // go up
                        }
                        else if (direction == 1){
                            verticle += k; // go down
                        } 
                        else if (direction == 2) {
                            horizontal -= k; // go left
                        } 
                        else if (direction == 3) {
                            horizontal += k; // go right
                        } 
                        //check to see if the decoy is in the maze and not the solution path
                        if (verticle > 0 && verticle < 14 && horizontal > 0 && horizontal < 14 && matrix[verticle][horizontal] == 0) {
                            matrix[verticle][horizontal] = 1;
                        }
                        else {
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