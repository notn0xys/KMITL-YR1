#include <iostream>
#include <string>
using namespace std;
class Wheel {
    public:
        Wheel(double r, string b): radius(r), brand(b) {}
        double radius;
        string brand;
};
class Car {
    public:
    Car(pair<int, string> w1, pair<int, string> w2, pair<int, string> w3, pair<int, string> w4 ): wheel1(w1.first(),w1.second()) {}
        Wheel wheel1;
        Wheel wheel2;
        Wheel wheel3;
        Wheel wheel4;
        void displayCar() {
            cout << wheel1.brand << " R: " << wheel1.radius << endl;
            cout << wheel2.brand << " R: " << wheel2.radius << endl;
            cout << wheel3.brand << " R: " << wheel3.radius << endl;
            cout << wheel4.brand << " R: " << wheel4.radius << endl;
            return;
        }
};