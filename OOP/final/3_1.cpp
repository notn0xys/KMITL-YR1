#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

class Student {
    public:
        string name;
        int age;
        double gpa;
};
void writeToFile(vector<Student>& ref) {
    ofstream file("text.txt");
    if (!file) {
        cout << "File not found" << endl;
        return;
    }
    for (auto item: ref) {
        file << item.name << ',' << item.age << ',' << item.gpa << endl;
    }
    file.close();
    return;
}
void readFile() {
    ifstream file("text.txt");
    if (!file) {
        cout << "File not found" << endl;
        return;
    }
    string line;
    string names;
    int ages;
    double gpas;
    while (getline(file,line)) {
        stringstream s(line);
        getline(s,names,',');
        s >> ages;
        s.ignore();
        s >> gpas;

        cout << "Name: " << names << " Age: " << ages << " Gpas " << gpas << endl; 
    }
}
void find(string name) {
    ifstream file("text.txt");
    if (!file) {
        cout << "File not found" << endl;
        return;
    }
    string line;
    string filename;
    int ages;
    double gpas;
    while (getline(file,line)) {
        stringstream ss(line);
        getline(ss,filename,',');
        if (filename == name) {
            ss >> ages;
            ss.ignore();
            ss >> gpas;
            cout << "Found" << endl;
            cout << "Name: " << filename << " Age: " << ages << " Gpas " << gpas << endl;
            return;
        }
    }
    cout << "Student not found" << endl;
    return;
}
int main() {
    vector<Student> students = {
        {"Alice", 20, 3.8},
        {"Bob", 22, 3.5},
        {"Charlie", 21, 3.9}
    };

    writeToFile(students);
    
    cout << "Reading from file:\n";
    readFile();

    // Search for a specific student
    cout << "\nSearching for 'Bob':\n";
    find("Bob");

    cout << "\nSearching for 'David':\n";
    find("David"); 

    return 0;
}
