#include <iostream>
using namespace std;

class Employee  {
    public:
        void setName(string x) {
            name = x;
            return;
        }
    protected:
        string name;
};

class Manager: public Employee {
    public:
        string getName() {
            return name;
        }
};
int main() {
    Manager human;
    human.setName("Alice");
    cout << "My name is: " << human.getName() << endl;
    return 0;

}