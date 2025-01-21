#include <iostream>
#include <vector>
#include <string>
using namespace std;
int main() {
    vector<string> activity_usage = {};
    vector<float> amount = {};
    float cost_per_litre;
    float threashold;
    string input;
    float float_input;
    float total_amount = 0;
    float daily_cost = 0;
    while (true) {
        cout << "Enter 'stop' to stop or Enter another water activity: " << endl;
        cin >> input;
        if (input == "stop") {
            break;
        }
        activity_usage.push_back(input);
        cout << "Enter Amount of water used: " << endl;
        cin >> float_input;
        amount.push_back(float_input);
    }
    cout << "Enter the cost per litre of the water: "  << endl;
    cin >> cost_per_litre;
    cout << "Enter the daily water limit" << endl;
    cin >> threashold;
    for (auto i: amount) {
        total_amount += i;
    }
    daily_cost = total_amount * cost_per_litre;
    cout << "Total Daily water cost: " << daily_cost << endl;
    if (daily_cost > threashold) {
        cout << "Warning Excessive water comsumptoin" << endl;
    }
    else {
        cout << "Efficient Water consumption" << endl;
    }
}