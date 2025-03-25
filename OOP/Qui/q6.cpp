#include <iostream>
using namespace std;

class Book {
    public:
        string getTitle() {
            return title;
        }
        Book(string name):title(name) {};
    private:
        string title;
};
class TextBook : public Book{
    public:
        TextBook(string t) : Book(t){};
        void printTitle() {
            cout << getTitle() << endl;
        }
};

int main() {
    TextBook book("C++ Basics");
    cout << book.getTitle() << endl;
    return 0;
}