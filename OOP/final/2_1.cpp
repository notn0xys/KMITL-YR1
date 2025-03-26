#include <iostream>
using namespace std;
class Fraction {
    private:
        int numerator;
        int denominator;
    public:
        Fraction(int n, int m): numerator(n), denominator(m) {}
        int getNumerator() {
            return numerator;
        }
        int getDenominator() {
            return denominator;
        }
    Fraction operator+(Fraction& other) {
        return Fraction(this->getDenominator() * other.getNumerator() + this->getNumerator() * other.getDenominator(), this->getDenominator() * other.getDenominator() );
    }
    friend ostream& operator<<(ostream& output, Fraction& value) {
        output << value.numerator << "/" << value.denominator << endl;
        return output;
    }
};

int main() {
    Fraction f1(1, 2), f2(2, 3);
    Fraction sum = f1 + f2;
    std::cout << sum;  // Expected output: "7/6"
}