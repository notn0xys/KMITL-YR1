#include <iostream>
using namespace std;

template <typename T>
class MySmartPointer {
private:
    T* ptr;  // Raw pointer to manage
public:
    // Constructor
    explicit MySmartPointer(T* p = nullptr) : ptr(p) {}

    // Overloaded Dereference Operator
    T& operator*() { return *ptr; }

    // Overloaded Arrow Operator
    T* operator->() { return ptr; }

    // Destructor (Frees memory)
    ~MySmartPointer() {
        delete ptr;
        cout << "Memory freed!\n";
    }
};

class Student {
public:
    string name;
    int age;
    Student(string n, int a) : name(n), age(a) {}
    void display() { cout << "Name: " << name << ", Age: " << age << endl; }
};

int main() {
    // Creating a smart pointer for Student
    MySmartPointer<Student> sp(new Student("Alice", 20));

    // Using overloaded operators
    sp->display();  // Calls Student's display() function
    return 0;  // Smart pointer goes out of scope, memory is freed
}
