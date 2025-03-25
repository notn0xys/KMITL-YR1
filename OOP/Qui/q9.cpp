#include <iostream>
using namespace std;

class Bird{
    public:
        void fly() {
            cout << "Flying generally" << endl;
        }
};
class Eagle : public Bird {
    public:
        void fly() {
            cout << "Soaring High" << endl;
            Bird::fly();
        }
};

int main() {
    Eagle hawk;
    hawk.fly();
    return 0;

}