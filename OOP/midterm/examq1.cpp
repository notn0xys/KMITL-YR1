#include <iostream>
#include <list>
#include <vector>
#include <string>

using namespace std;
int main() {
    vector<string> p1 = {"Red" , "Green", "Blue"};
    vector<string> p2 = {"Black", "Yellow"};
    vector<string> p3 = {"Red" , "Orange", "Pink","Purple"};
    vector<string> p4 = {"Yellow", "Grey", "Red"};
    vector<vector<string>> data = {p1,p2,p3,p4};
    list<list<string>> output;
    list<string> output_list;
    vector<string> current_target;
    int current_size;
    bool first = true;
    list<string> current_var;
    int current_no;
    vector<int> target;
    string input;
    cout << "Enter Pallet: ";
    cin >> input;
    for (auto i: input) {
        target.push_back(int(i));
    }
    for (auto i: target) {
        if (first) {
            current_target = data[i - 1];
            for (auto j : current_target) {
                output_list.push_back(j);
                output.push_back(output_list);
                output_list.clear();
            }
            first = false;
        }
        else {
            current_target = data[i - 1];
            current_size = output.size();
            for (int j = 0; j < current_size; j++) {
                current_var = output.front();
                output.pop_front();
                for (int l = 0; l < current_target.size(); l++) {
                    list<string>add = current_var;
                    add.push_back(current_target[l]);
                    output.push_back(add);
                }
            }
        }
    }
    for (auto i: output) {
        for (auto j: i) {
            cout << j << " ";
        }
        cout << endl;
    }

}