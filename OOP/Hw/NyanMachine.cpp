#include <sqlite3.h>
#include <iostream>
#include <stdlib.h>
#include <string>
#include <vector>
using namespace std;
struct VendingMachineObject {
    int id;
    string name;
    int stock;
    int price;

};
class VendingMachine {
    private:
        vector<VendingMachineObject> get_update_information() {
            vector<VendingMachineObject> stockItems;
            auto callback = [](void* data, int argc, char** argv, char** azColName) -> int {
                std::vector<VendingMachineObject>* items = static_cast<std::vector<VendingMachineObject>*>(data); 
                VendingMachineObject item;
                for (int i = 0; i < argc; i++) {
                    if (std::string(azColName[i]) == "id") {
                        item.id = argv[i] ? std::stoi(argv[i]) : 0; 
                    } else if (std::string(azColName[i]) == "name") {
                        item.name = argv[i] ? argv[i] : "NULL";
                    } else if (std::string(azColName[i]) == "stock") {
                        item.stock = argv[i] ? std::stoi(argv[i]) : 0;
                    } else if (std::string(azColName[i]) == "price") {
                        item.price = argv[i] ? std::stoi(argv[i]) : 0; 
                    }
                }
                items->push_back(item);
                return 0; 
            };
            const char* sql = "SELECT id, name, stock, price FROM stock_67011177;";
            if (sqlite3_exec(db, sql, callback, &stockItems, nullptr) != SQLITE_OK) {
                std::cerr << "SQL error: " << sqlite3_errmsg(db) << std::endl;
            }

            return stockItems;
        }
        bool admin_mode = false;
        sqlite3* db;
        char* errMsg = nullptr; 
        int rc;
        int Charge;
        int moneybox;
        void usermode() {
            while (true) {
                system("cls");
                vector<VendingMachineObject> list_of_goods = get_update_information();
                
            }
        }
        void adminmode() {
            cout << "Testing admin mode" << endl;;
            return;
        }
    public:
    bool exit = false;
    int amount_to_pay;
    VendingMachine(sqlite3* dbin, char* errMsgin, int rcin) {
        db = dbin;
        errMsg = errMsgin;
        rc = rcin;
    };
    void run() {
        exit = false;
        int choice;
        while (true) {
            cout << "Welcome to the vending machine \nPlease Choose from these options: \n1: User Mode\n2: Admin Mode\n3: Exit " << endl;
            cin >> choice;
            switch (choice)
            {
            case 1:
                usermode();
                break;
            case 2:
                adminmode();
                break;
            case 3:
                exit = true;
                break;
            default:
                cout << "Choose agian" << endl;
                break;
            }
            if (exit) {
                return;
            }
        }
    }


};
int main() {
    sqlite3* db; 
    char* errMsg = nullptr; 
    int rc;
    rc = sqlite3_open("Stock_67011177.db", &db);
    if (rc) {
        std::cerr << "Can't open database: " << sqlite3_errmsg(db) << std::endl;
        return rc;
    } else {
    std::cout << "Opened database successfully!" << std::endl;
    }
    const char* createTableSQL = R"(
    CREATE TABLE IF NOT EXISTS stock_67011177 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    stock INTEGER NOT NULL,
    price INTEGER NOT NULL
    );
    )";
    rc = sqlite3_exec(db, createTableSQL, nullptr, nullptr, &errMsg);
    if (rc != SQLITE_OK) {
        std::cerr << "SQL error: " << errMsg << std::endl;
        sqlite3_free(errMsg);
        } else {
        std::cout << "Table created successfully!" << std::endl;
    }
    VendingMachine start(db,errMsg,rc);
    start.run();
    sqlite3_close(db);
    return 0;
}