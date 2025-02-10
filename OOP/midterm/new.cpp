#include <iostream>
using namespace std;
int main() {
    int i = 5;
    int j = 5;
    int *p = &i;
    int &newp = j;
    cout << p << endl;
    *p = 20;
    cout << p << endl;
    cout << j << endl;

}