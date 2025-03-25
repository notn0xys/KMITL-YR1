#include <iostream>
using namespace std;
class animal {
    public:
    virtual void speak() {
        cout << "I am an animal" << endl;
    }
};
class dog: public animal{
    public:
    void speak() {
        cout << "Woof Woof" << endl;
    }
};
int main() {
    dog woof;
    woof.speak();
    return 0;
}