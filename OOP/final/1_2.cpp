#include <iostream>
#include <vector>
using namespace std;

class Vehicle {
    protected:
        int speed;
    public:
        void display() {
            cout << speed << endl;
        }
        Vehicle(int speeds): speed(speeds){}
        virtual void drive() {
            cout << "Vehicle is moving\n";
        }
};
class Car : public Vehicle {
    public:
        Car(int speed): Vehicle(speed) {}
        void drive() override {
            cout << "Car is driving at "<< speed <<" km/h\n";
        }
};
class Bike : public Vehicle {
    public:
        Bike(int speed): Vehicle(speed) {}
        void drive() override {
            cout << "Bike is riding at "<< speed <<" km/h\n";
        }
};
int main() {
    vector<Vehicle*> vehicles;
    Vehicle* vehicleptr;
    Bike bike(20);
    Car car(100);
    vehicleptr = &bike;
    vehicles.push_back(vehicleptr);
    vehicleptr = &car;
    vehicles.push_back(vehicleptr);
    for (auto vehicle: vehicles) {
        vehicle->display();
    }
    return 0;
}