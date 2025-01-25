#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<vector<string>> color = 
{
    {"Red" , "Green", "Blue"},
    {"Black", "Yellow"},
    {"Red" , "Orange", "Pink","Purple"},
    {"Yellow", "Grey", "Red"},
};

void recur(vector<int> vec, vector<string> k ={})
{
    


    for (auto c : color[vec[0]])
    {
        vector<int> v = vec;
        v.erase(v.begin());
        vector<string> result = k;
        result.push_back(c);

        if (v.empty())
        {
            for (auto m : result)
            {
                cout << m << " ";
            }
            cout << endl;
        }

        else
        {
            recur(v,result);
        }

    }
}


int main() {

    vector<int> num = {1,2};
    recur(num);
}