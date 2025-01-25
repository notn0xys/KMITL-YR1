#include <iostream>
#include <vector>
using namespace std;
void print_matrix(vector<vector<int>> matrix) {
    for (auto row: matrix){
        for (auto letter: row){
            cout << letter << " ";
        }
        cout << "\n";
    }
}
vector<vector<int>> transpost(const vector<vector<int>>& matrix) {
    vector<vector<int>> return_matrix = matrix;
    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix[0].size(); j++) {
            return_matrix[j][i] = matrix[i][j];
        }
    }
    return return_matrix;
}
vector<vector<int>> Multiplication(const vector<vector<int>>& matrix1, const vector<vector<int>>& matrix2) {
    vector<int> holdiong;
    vector<vector<int>> return_matrix;
    int temp_number;
    for (int i = 0; i < matrix1.size(); i++) {
        holdiong.clear();
        for (int j = 0; j < matrix2[0].size(); j++) {
            temp_number = 0;
            for (int k = 0 ; k < matrix1[0].size() ;k++) {
                temp_number += matrix1[i][k] * matrix2[k][j];
            }
            holdiong.push_back(temp_number);
        }
        return_matrix.push_back(holdiong);
    }
    return return_matrix;
}
int main() {
    vector<vector<int>> matrix;
    vector<int> row;
    int input;
    for (int i = 0; i < 3; i++) {
        cout << "Row " << i + 1 << " :" << endl;
        for (int j = 0; j < 3; j++) {
            cout << "Enter " << j + 1 << " Column: " << endl;
            cin >> input;
            row.push_back(input);
        }
        matrix.push_back(row);
        row.clear();
    }
    print_matrix(matrix);
    vector<vector<int>> matrix2 = transpost(matrix);
    print_matrix(matrix2);
    vector<vector<int>> matrix3 = Multiplication(matrix,matrix2);
    print_matrix(matrix3);
}