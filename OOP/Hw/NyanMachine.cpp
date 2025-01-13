#include <sqlite3.h>
#include <iostream>
#include <cstdlib>
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
    sqlite3* db;
    char* errMsg = nullptr;
    int rc;
    bool admin_mode = false;
    int Charge = 0;
    int moneybox = 0;
    bool exit = false;


    vector<VendingMachineObject> get_update_information() {
        vector<VendingMachineObject> stockItems;

        auto callback = [](void* data, int argc, char** argv, char** azColName) -> int {
            vector<VendingMachineObject>* items = static_cast<vector<VendingMachineObject>*>(data); 
            VendingMachineObject item;

            for (int i = 0; i < argc; i++) {
                string columnName = azColName[i];
                if (columnName == "id") {
                    item.id = argv[i] ? stoi(argv[i]) : 0;
                } else if (columnName == "name") {
                    item.name = argv[i] ? argv[i] : "NULL";
                } else if (columnName == "stock") {
                    item.stock = argv[i] ? stoi(argv[i]) : 0;
                } else if (columnName == "price") {
                    item.price = argv[i] ? stoi(argv[i]) : 0;
                }
            }
            items->push_back(item);
            return 0;
        };

        const char* sql = "SELECT id, name, stock, price FROM stock_67011177;";
        if (sqlite3_exec(db, sql, callback, &stockItems, nullptr) != SQLITE_OK) {
            cerr << "SQL error: " << sqlite3_errmsg(db) << endl;
        }

        return stockItems;
    }

    void usermode() {
        int items;
        bool found;
        int input;
        while (true) {
            found = false;
            VendingMachineObject targetedItem; 
            system("cls");
            vector<VendingMachineObject> list_of_goods = get_update_information();
            cout << "Items available in the vending machine:\n";
            for (const auto& item : list_of_goods) {
                cout << "ID: " << item.id << ", Name: " << item.name
                     << ", Stock: " << item.stock << ", Price: " << item.price << endl;
            }
            cout << "Choose which item you would like to purchase from the id" << endl;
            cin >> input;
            for (const auto& item: list_of_goods) {
                if (input = item.id) {
                    targetedItem = item;
                    found = true;
                    break;
                }
            }
            if (!found){
                cout << "Item Not found" << endl;
                continue;
            }
            else {
                cout << "ID: " << targetedItem.id << ", Name: " << targetedItem.name << ", Stock: " << targetedItem.stock << ", Price: " << targetedItem.price << endl;
                cout << "How many items you wish to buy" << endl;
                cin >> items;
                if (items > targetedItem.stock) {
                    cout << ""
                }
            }
            

        }       
    }

    void adminmode() {
        cout << "Admin mode activated.\n";
        return;
    }

    int onstart() {
        rc = sqlite3_open("Stock_67011177.db", &db);
        if (rc) {
            cerr << "Can't open database: " << sqlite3_errmsg(db) << endl;
            return rc;
        } else {
            cout << "Opened database successfully!" << endl;
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
            cerr << "SQL error: " << errMsg << endl;
            sqlite3_free(errMsg);
        } else {
            cout << "Table created successfully!" << endl;
        }
        const char* CreateCollectionBox = R"(
        CREATE TABLE IF NOT EXISTS collectionbox (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Bill_100 INTEGER NOT NULL,
        Bill_20 INTEGER NOT NULL,
        Coin_10 INTEGER NOT NULL,
        Coin_5 INTEGER NOT NULL,
        Coin_1 INTEGER NOT NULL
        );
        )";
        rc = sqlite3_exec(db, CreateCollectionBox, nullptr, nullptr, &errMsg);
        if (rc != SQLITE_OK) {
            cerr << "SQL error: " << errMsg << endl;
            sqlite3_free(errMsg);
        } else {
            cout << "Table created successfully!" << endl;
        }
        const char* CreateChangeBox = R"(
        CREATE TABLE IF NOT EXISTS changebox (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Bill_100 INTEGER NOT NULL,
        Bill_20 INTEGER NOT NULL,
        Coin_10 INTEGER NOT NULL,
        Coin_5 INTEGER NOT NULL,
        Coin_1 INTEGER NOT NULL
        );
        )";
        rc = sqlite3_exec(db, CreateChangeBox, nullptr, nullptr, &errMsg);
        if (rc != SQLITE_OK) {
            cerr << "SQL error: " << errMsg << endl;
            sqlite3_free(errMsg);
        } else {
            cout << "Table created successfully!" << endl;
        }
        return 0;
    }

public:
    VendingMachine() {
        onstart();
    }

    void run() {
        while (true) {
            int choice;
            cout << "Welcome to the vending machine \n";
            cout << "Please choose from these options: \n";
            cout << "1: User Mode\n2: Admin Mode\n3: Exit\n";
            cout << "Enter your choice: ";
            cin >> choice;

            switch (choice) {
            case 1:
                usermode();
                break;
            case 2:
                adminmode();
                break;
            case 3:
                cout << "Exiting the vending machine. Goodbye!\n";
                return;
            default:
                cout << "Invalid choice. Please try again.\n";
                break;
            }
        }
    }

    ~VendingMachine() {
        sqlite3_close(db);
    }
};

int main() {
    VendingMachine machine;
    machine.run();
    return 0;
}
