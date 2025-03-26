#include <iostream>
using namespace std;
class Shape {
    public:
    
    virtual ~Shape() {
        cout << "Deleting shape part";
    }
};
class Rectangle: public Shape {
    public:
        Rectangle(int w, int h): width(w) , height(h) {}
        int width;
        int height;
        
};

int main() {
    Shape* meow = new Rectangle(10,5);
    delete meow;
}