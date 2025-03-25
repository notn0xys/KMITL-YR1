#include <iostream>
using namespace std;

class Person {
    public: 
        void introduce() {
            cout << "I am a person" << endl;
        }
};

class Student: private Person{
    public:
        void greet() {
            introduce();
        }
};

int main() {
    Student noxy;
    // Noxy.introduce() wouldnt work because introduce is private so we cant acess it now
    noxy.greet();
    // Work around to call introduce since it is private
    return 0;

}