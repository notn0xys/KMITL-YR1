#include <iostream>
using namespace std;

class Vehicle {
    public:
        void setSpeed(int x){
            speed = x;
        }
    protected:
        int speed;
};
class Car: public Vehicle {
    public:
        void displaySpeed() {
            cout << "Your speed is: " << speed << endl;
        }
};

int main() {
    Car ferrari;
    ferrari.setSpeed(120);
    ferrari.displaySpeed();
    return 0;

}