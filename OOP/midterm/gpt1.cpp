#include <iostream>
#include <list>
#include <vector>
#include <string>

using namespace std;

int main() {
    vector<string> p1 = {"Red", "Green", "Blue"};
    vector<string> p2 = {"Black", "Yellow"};
    vector<string> p3 = {"Red", "Orange", "Pink", "Purple"};
    vector<string> p4 = {"Yellow", "Grey", "Red"};
    vector<vector<string>> data = {p1, p2, p3, p4};

    list<list<string>> output;
    list<string> output_list;
    vector<string> current_target;
    bool first = true;
    string input;

    cout << "Enter Pallet (e.g., 12 for p1 and p2): ";
    cin >> input;

    // Input validation
    for (char ch : input) {
        if (ch < '1' || ch > '4') {
            cerr << "Invalid input! Please enter numbers between 1 and 4." << endl;
            return 1;
        }
    }

    for (char ch : input) {
        int index = ch - '1'; // Convert char to 0-based index
        current_target = data[index];

        if (first) {
            // Initialize output with the first palette
            for (const auto& color : current_target) {
                output_list.push_back(color);
                output.push_back(output_list);
                output_list.clear();
            }
            first = false;
        } else {
            // Combine with subsequent palettes
            list<list<string>> new_output;
            for (const auto& combination : output) {
                for (const auto& color : current_target) {
                    list<string> new_combination = combination;
                    new_combination.push_back(color);
                    new_output.push_back(new_combination);
                }
            }
            output = move(new_output); // Replace old output with new combinations
        }

        // Debug: Print the current size of output
        cout << "Combinations so far: " << output.size() << endl;

        // Limit the size of the output to prevent memory overload
        if (output.size() > 100000) { // Adjust this limit as needed
            cerr << "Too many combinations! Limiting output." << endl;
            return 1;
        }
    }

    // Print the output
    for (const auto& combination : output) {
        for (const auto& color : combination) {
            cout << color << " ";
        }
        cout << endl;
    }

    return 0;
}
