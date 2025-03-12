#include <fstream>
#include <iostream>
using namespace std;

int main() {
    ofstream file("meow.txt");
    file << "Moew nyan \n";
    file << "I hate n";
    file.close();
    ifstream file2("meow.txt");
    if (!file2) {
        return 1;
    }
    string line;
    while (getline(file2,line)) {
        cout << line << endl;
    }
    file2.close();
    return 0;
}