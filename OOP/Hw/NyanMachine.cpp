#include <sqlite3.h>
#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>

using namespace std;
struct Money{
    int bill100;
    int bill20;
    int coin10;
    int coin5;
    int coin1;
};
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
    int getint() {
        int x;
        cin >> x;
        while (cin.fail()) {
            cout << "Invalid input. Please enter a number: ";
            cin.clear();
            cin.ignore(256, '\n');
            cin >> x;
        }
        return x;
    }
    Money amount_of_bills(int total) {
        Money money;
        money.bill100 = total / 100;
        total = total % 100;
        money.bill20 = total / 20;
        total = total % 20;
        money.coin10 = total / 10;
        total = total % 10;
        money.coin5 = total / 5;
        total = total % 5;
        money.coin1 = total;
        return money;
    }
    Money get_collectionbox() {
        Money collection;
        auto callback = [](void* data, int argc, char** argv, char** azColName) -> int {
            Money* collection = static_cast<Money*>(data);
            for (int i = 0; i < argc; i++) {
                string columnName = azColName[i];
                if (columnName == "Bill_100") {
                    collection->bill100 = argv[i] ? stoi(argv[i]) : 0;
                } else if (columnName == "Bill_20") {
                    collection->bill20 = argv[i] ? stoi(argv[i]) : 0;
                } else if (columnName == "Coin_10") {
                    collection->coin10 = argv[i] ? stoi(argv[i]) : 0;
                } else if (columnName == "Coin_5") {
                    collection->coin5 = argv[i] ? stoi(argv[i]) : 0;
                } else if (columnName == "Coin_1") {
                    collection->coin1 = argv[i] ? stoi(argv[i]) : 0;
                }
            }
            return 0;
        };
        const char* sql = "SELECT Bill_100, Bill_20, Coin_10, Coin_5, Coin_1 FROM collectionbox WHERE id = 1;";
        if (sqlite3_exec(db, sql, callback, &collection, nullptr) != SQLITE_OK) {
            cerr << "SQL error: " << sqlite3_errmsg(db) << endl;
        }
        return collection;
    }
    void Modify_stock(VendingMachineObject item) {
        const char* sql = "UPDATE stock_67011177 SET stock = ? WHERE id = ?;";
        sqlite3_stmt* stmt;
        rc = sqlite3_prepare_v2(db, sql, -1, &stmt, nullptr);
        if (rc != SQLITE_OK) {
            cerr << "SQL error: " << sqlite3_errmsg(db) << endl;
        }
        sqlite3_bind_int(stmt, 1, item.stock);
        sqlite3_bind_int(stmt, 2, item.id);
        rc = sqlite3_step(stmt);
        if (rc != SQLITE_DONE) {
            cerr << "SQL error: " << sqlite3_errmsg(db) << endl;
        }
        sqlite3_finalize(stmt);
    }
    Money Modify_collectionbox(Money collection) {
        const char* sql = "UPDATE collectionbox SET Bill_100 = ?, Bill_20 = ?, Coin_10 = ?, Coin_5 = ?, Coin_1 = ? WHERE id = 1;";
        sqlite3_stmt* stmt;
        rc = sqlite3_prepare_v2(db, sql, -1, &stmt, nullptr);
        if (rc != SQLITE_OK) {
            cerr << "SQL error: " << sqlite3_errmsg(db) << endl;
        }
        sqlite3_bind_int(stmt, 1, collection.bill100);
        sqlite3_bind_int(stmt, 2, collection.bill20);
        sqlite3_bind_int(stmt, 3, collection.coin10);
        sqlite3_bind_int(stmt, 4, collection.coin5);
        sqlite3_bind_int(stmt, 5, collection.coin1);
        rc = sqlite3_step(stmt);
        if (rc != SQLITE_DONE) {
            cerr << "SQL error: " << sqlite3_errmsg(db) << endl;
        }
        sqlite3_finalize(stmt);
        return collection;
    }
    Money get_changebox() {
        Money change;
        auto callback = [](void* data, int argc, char** argv, char** azColName) -> int {
            Money* change = static_cast<Money*>(data);
            for (int i = 0; i < argc; i++) {
                string columnName = azColName[i];
                if (columnName == "Bill_100") {
                    change->bill100 = argv[i] ? stoi(argv[i]) : 0;
                } else if (columnName == "Bill_20") {
                    change->bill20 = argv[i] ? stoi(argv[i]) : 0;
                } else if (columnName == "Coin_10") {
                    change->coin10 = argv[i] ? stoi(argv[i]) : 0;
                } else if (columnName == "Coin_5") {
                    change->coin5 = argv[i] ? stoi(argv[i]) : 0;
                } else if (columnName == "Coin_1") {
                    change->coin1 = argv[i] ? stoi(argv[i]) : 0;
                }
            }
            return 0;
        };
        const char* sql = "SELECT Bill_100, Bill_20, Coin_10, Coin_5, Coin_1 FROM changebox WHERE id = 1;";
        if (sqlite3_exec(db, sql, callback, &change, nullptr) != SQLITE_OK) {
            cerr << "SQL error: " << sqlite3_errmsg(db) << endl;
        }
        return change;
    }
    Money modify_changebox(Money change) {
        const char* sql = "UPDATE changebox SET Bill_100 = ?, Bill_20 = ?, Coin_10 = ?, Coin_5 = ?, Coin_1 = ? WHERE id = 1;";
        sqlite3_stmt* stmt;
        rc = sqlite3_prepare_v2(db, sql, -1, &stmt, nullptr);
        if (rc != SQLITE_OK) {
            cerr << "SQL error: " << sqlite3_errmsg(db) << endl;
        }
        sqlite3_bind_int(stmt, 1, change.bill100);
        sqlite3_bind_int(stmt, 2, change.bill20);
        sqlite3_bind_int(stmt, 3, change.coin10);
        sqlite3_bind_int(stmt, 4, change.coin5);
        sqlite3_bind_int(stmt, 5, change.coin1);
        rc = sqlite3_step(stmt);
        if (rc != SQLITE_DONE) {
            cerr << "SQL error: " << sqlite3_errmsg(db) << endl;
        }
        sqlite3_finalize(stmt);
        return change;
    }
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
    string displayStock(int amount) {
        if (amount == 0) {
            return "Out of stock";
        } else {
            return to_string(amount);
        }
    }
    void usermode() {
        int items;
        bool found;
        int input;
        int amounttopay;
        int inputmoney;
        int returnmoney;
        int x;
        Money change;
        Money collection;
        Money ChangeBox;
        Money CollectionBox;
        while (true) {
            found = false;
            VendingMachineObject targetedItem; 
            system("cls");
            vector<VendingMachineObject> list_of_goods = get_update_information();
            cout << "Items available in the vending machine:\n";
            for (const auto& item : list_of_goods) {
                cout << "ID: " << item.id << ", Name: " << item.name << ", Stock: " << displayStock(item.stock) << ", Price: " << item.price << endl;
            }
            cout << "Press " << list_of_goods.size() + 1 << " to exit" << endl;
            cout << "Choose which item you would like to purchase from the id" << endl;
            input = getint();
            if (input == list_of_goods.size() + 1){
                break;
            }
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
                items = getint();
                while (items > targetedItem.stock) {
                    cout << "Not enough stock, please enter a smaller number" << endl;
                    items = getint();
                }
                amounttopay = items * targetedItem.price;
                cout << "The total amount you need to pay is " << amounttopay << endl;
                cout << "Please insert the money" << endl;
                inputmoney = getint();
                while (inputmoney < amounttopay) {
                    cout << "Not enough money, please insert more money" << endl;
                    x = getint();
                    inputmoney += x;
                }
                cout << "You have inserted " << inputmoney << endl;
                cout << "your change is" << inputmoney - amounttopay << endl;
                collection = amount_of_bills(inputmoney);
                returnmoney = inputmoney - amounttopay;
                change = amount_of_bills(returnmoney);
                ChangeBox = get_changebox();
                CollectionBox = get_collectionbox();
                CollectionBox.bill100 += collection.bill100;
                CollectionBox.bill20 += collection.bill20;
                CollectionBox.coin10 += collection.coin10;
                CollectionBox.coin5 += collection.coin5;
                CollectionBox.coin1 += collection.coin1;
                Modify_collectionbox(CollectionBox);
                ChangeBox.bill100 -= change.bill100;
                ChangeBox.bill20 -= change.bill20;
                ChangeBox.coin10 -= change.coin10;
                ChangeBox.coin5 -= change.coin5;
                ChangeBox.coin1 -= change.coin1;
                modify_changebox(ChangeBox);
                cout << "You have successfully purchased " << items << " " << targetedItem.name << endl;
                targetedItem.stock -= items;
                Modify_stock(targetedItem);
            }
            

        }       
    }

    void adminmode() {
        cout << "Admin mode activated.\n";
        return;
    }
    void onexit() {
        cout << "Exiting the vending machine. Goodbye!\n";
        sqlite3_close(db);
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
            choice = getint();

            switch (choice) {
            case 1:
                usermode();
                break;
            case 2:
                adminmode();
                break;
            case 3:
                onexit();
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
