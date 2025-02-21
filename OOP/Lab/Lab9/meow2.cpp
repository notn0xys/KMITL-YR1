#include <iostream>
#include <vector>
using namespace std;
class polynomial {
    public:
    polynomial() {
    }

    polynomial(const vector<pair<int, int>>& values) {
        data = values;
    }

    ~polynomial() {
    }
        vector<pair<int,int>> data;
    int getCofficent(int exponent) {
        for (auto pairs:this->data) {
            if (pairs.second == exponent) {
                return pairs.first;
            }
        }
        cout << "No Number associated with that exponent" << endl;
        return 0;
    }
    void setCofficent(int exponent, int newCofficent) {
        for (int i = 0; i < this->data.size(); i++) {
            if (this->data[i].second == exponent) {
                this->data[i].first == newCofficent;
                cout << "Changed sucessfully to " << newCofficent << endl;
                return;
            }
        }
        cout << "No Number associated with that exponent" << endl;
        return;
    }
    void operator=(const polynomial &meow) {
        this->data = meow.data;
        return;
    }
    void operator+=(const polynomial &meow) {
        polynomial value = *this + meow;
        this->data = value.data;
        return;
    } 
    void operator*=(const polynomial &meow) {
        polynomial value = *this * meow;
        this->data = value.data;
        return;
    }
    void operator-=(const polynomial &meow) {
        polynomial value = *this - meow;
        this->data = value.data;
        return;
    }
    polynomial operator-(const polynomial &meow) {
        polynomial temp;
        int first = 0;
        int second = 0;
        while (true) {
            if (first >= this->data.size() || second >= meow.data.size()) {
                if (first >= this->data.size()) {
                    for (second; second < meow.data.size(); second++) {
                        int number = meow.data[second].first * -1;
                        pair<int,int> new_val = make_pair(number,meow.data[second].second);
                        temp.data.push_back(new_val);
                    }
                    break;
                }
                else if (second >= meow.data.size()) {
                    for (first; first < this->data.size(); first++) {
                        temp.data.push_back(this->data[first]);
                    }
                    break;
                }
                else {
                    break;
                }
            }
            else {
                if (this->data[first].second > meow.data[second].second) {
                    temp.data.push_back(this->data[first]);
                    first++;
                }
                else if (this->data[first].second < meow.data[second].second) {
                    int number = meow.data[second].first * -1;
                    pair<int,int> new_val = make_pair(number,meow.data[second].second);
                    temp.data.push_back(new_val);
                    second++;
                }
                else {
                    int value = this->data[first].first - meow.data[second].first;
                    pair<int,int> meow = make_pair(value,this->data[first].second);
                    temp.data.push_back(meow);
                    first++;
                    second++;
                }
            }
        }
        return temp;
    }
    polynomial operator*(const polynomial &meow) {
        polynomial temp = {};
        for (auto first:this->data) {
            polynomial  current_row;
            for (auto second:meow.data) {
                int number = first.first * second.first;
                int power = first.second + second.second;
                pair<int,int> nums = make_pair(number,power);
                current_row.data.push_back(nums);
            }
            temp = temp + current_row;
        }
        return temp;
    }
    polynomial operator+(const polynomial &meow) {
        polynomial temp;
        int first = 0;
        int second = 0;
        while (true) {
            if (first >= this->data.size() || second >= meow.data.size()) {
                if (first < this->data.size() ) {
                    for (first; first < data.size(); first++) {
                        temp.data.push_back(this->data[first]);
                    }
                    break;
                }
                else if (second < meow.data.size() ) {
                    for (second; second < meow.data.size(); second++) {
                        temp.data.push_back(meow.data[second]);
                    }
                    break;
                }
                else {
                    break;
                }
            }
            if (this->data[first].second > meow.data[second].second) {
                temp.data.push_back(this->data[first]);
                first++;
            }
            else if (this->data[first].second < meow.data[second].second) {
                temp.data.push_back(meow.data[second]);
                second++;
            }
            else {
                int value = this->data[first].first + meow.data[second].first;
                pair<int,int> meow = make_pair(value,this->data[first].second);
                temp.data.push_back(meow);
                first++;
                second++;
            }
        }
        return temp;
    }
        friend ostream& operator<<(ostream& output, polynomial c) {
            bool first = true;
            for (auto pair: c.data) {
                if(pair.second == 0) {
                    if (!first) {
                        if (pair.first > 0) {
                            cout << " + ";
                        }
                        else {
                            cout << " ";
                        }
                    }
                    cout << pair.first;
                    first = false;
                }
                else {
                    if (!first) {
                        if (pair.first > 0) {
                            cout << " + ";
                        }
                        else {
                            cout << " ";
                        }
                    }
                    cout << pair.first << "x^" << pair.second;
                    first = false;

                }
            }
            cout << endl;
            return cout;
    }
};

int main() {
    polynomial hawk;
    polynomial tuah;
    hawk.data = {{1,2},{3,1},{2,0}};
    cout << hawk;
    tuah.data = {{4,4},{3,3}, {2,2},{1,1}};
    cout <<tuah;
    cout << hawk + tuah;
    cout << "Hawk after += tuah" << endl;
    hawk += tuah;
    cout <<hawk;
    polynomial hawk2;
    polynomial ts_pmo;
    hawk2.data = {{2,1},{3,0}};
    ts_pmo.data = {{1,1},{1,0}};
    cout << "Multiplication" << endl;
    cout << hawk2;
    cout <<ts_pmo;
    cout << hawk2 * ts_pmo;
    cout << "hawk2 after *= ts_pmo" << endl;
    hawk2 *= ts_pmo;
    cout << hawk2;
    cout << "Subtraction" << endl;
    polynomial meow1;
    polynomial meow2;
    meow1.data = {{2,2},{3,1}};
    meow2.data = {{1,1},{1,0}};
    cout << meow1;
    cout << meow2;
    cout << meow2 - meow1;
    cout << "meow1 after -= meow2" << endl;
    meow1 -= meow2;
    cout << meow1;

}