#include <iostream>
using namespace std;
class Bankaccount {
    private:
        int accountNumber;
        double balance;
    public:
        Bankaccount(int acc, double bal): accountNumber(acc), balance(bal)  {}
        void deposit(double amount) {
            if (amount <= 0) {
                cout << "Cant deposit less than 0 \n";
                return;
            }
            balance += amount;
            return;
        }
        void withdraw(double amount) {
            if (amount >= balance) {
                cout << "Not enough funds returning \n";
                return;
            }
            balance -= amount;
            return;
        }
        void display() {
            cout << accountNumber <<  endl;
            cout << balance << endl;
        }

};
int main() {
    Bankaccount account(1,10000);
    account.deposit(200);
    account.withdraw(500);
    account.display();
    return 0;
}