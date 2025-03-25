#include <iostream>
#include <string>

class Student {
private:
    std::string name;
    int age;

public:
    // Constructor
    Student(std::string n = "", int a = 0) : name(n), age(a) {}

    // Overloaded << operator for output
    friend std::ostream& operator<<(std::ostream& output, const Student& student) {
        output << "Name: " << student.name << ", Age: " << student.age;
        return output;
    }

    // Overloaded >> operator for input
    friend std::istream& operator>>(std::istream& input, Student& student) {
        std::cout << "Enter Name: ";
        input >> student.name;
        std::cout << "Enter Age: ";
        input >> student.age;
        return input;
    }
};

int main() {
    Student s;
    std::cin >> s;  // User inputs name and age
    std::cout << "Student Details: " << s << std::endl; // Outputs student data
    return 0;
}
