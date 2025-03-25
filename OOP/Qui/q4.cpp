#include <iostream>
using namespace std;

class Engine {
    public:
        void start() {
            cout << "Engine started" << endl;
        }
};
class Wheel {
    public:
        void roll() {
            cout << "Wheel rolling" << endl;
        }
};

class Car: public Wheel, public Engine {

};

int main() {
    Car meow;
    meow.roll();
    meow.start();
    return 0;
}