#include <iostream>
#include <vector>
using namespace std;

class BankAccount {
    public:
        BankAccount(string name, int initbalance): AccountName(name) {
            if (initbalance > 0){
                balance = initbalance;
            }
        }
        int getBalance(){
            transaction_history.push_back("Balanced Retrieved");
            return balance;
        }
        void setName(string newname){
            if (newname.size() > 0){
                AccountName = newname;
                cout << "Name updated" << endl;
                transaction_history.push_back("Name Updated to: " + newname);
            } 
            else {
                cout << "failed to update name" << endl;
            }
        }
        void printTransactionHistory() {
            for (int i; i < transaction_history.size() ; i++) {
                cout << transaction_history[i] << endl;
            }
        }
        void printV2() {
            for (auto a:transaction_history){
                cout << a << endl;
            }
        }
        void deposit(int amount) {
            if (amount > 0) {
                balance += amount;
                transaction_history.push_back("Deposited: " + amount);
            }
            else {
                cout << "Amount deposit can not be negative" << endl;
            }
        }
        void withdraw(int amount) {
            if (amount > 0 && balance - amount > 0) {
                cout << amount << " Sucessfully deducted from the balance remaining balance is " << balance << endl;
                transaction_history.push_back("Withdrawn: " + amount);
            }
            else {
                cout << "incorrect format try agian" << endl;
            }
        }
    private:
        string AccountName;
        int balance = 0;
        vector<string> transaction_history = {};
};

int main() {
    BankAccount account1("Noxy",10);
    return 0;
}