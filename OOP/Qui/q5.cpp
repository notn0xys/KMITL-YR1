#include <iostream>
using namespace std;

class Shape {
    public:
        virtual void draw() = 0;
};

class Circle: public Shape {
    public:
        void draw() {
            cout << "Drawing a Circle" << endl;
        }
};

class Square: public Shape {
    public:
        void draw() {
            cout << "Drawing a Square" << endl;
        }
};

int main() {
    Shape* shapeptr;
    Circle circle;
    Square square;
    shapeptr = &circle; 
    shapeptr->draw();
    shapeptr = &square; 
    shapeptr->draw();
    return 0;
}