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
    bool enoughStock(Money system, Money user) {
        if (system.bill100 < user.bill100) {
            cout << "Machine only has " << system.bill100 << " $100 bills" << "Change needed is " << user.bill100 << endl;
        }
        if (system.bill20 < user.bill20) {
            cout << "Machine only has " << system.bill20 << " $20 bills" << "Change needed is " << user.bill20 << endl;
        }
        if (system.coin10 < user.coin10) {
            cout << "Machine only has " << system.coin10 << " $10 coins" << "Change needed is " << user.coin10 << endl;
        }
        if (system.coin5 < user.coin5) {
            cout << "Machine only has " << system.coin5 << " $5 coins" << "Change needed is " << user.coin5 << endl;
        }
        if (system.coin1 < user.coin1) {
            cout << "Machine only has " << system.coin1 << " $1 coins" << "Change needed is " << user.coin1 << endl;
        }
        if (system.bill100 < user.bill100 || system.bill20 < user.bill20 || system.coin10 < user.coin10 || system.coin5 < user.coin5 || system.coin1 < user.coin1) {
            return false;
        }
        return true;
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
    int getmorethan0() {
        int x;
        cin >> x;
        while (cin.fail() || x <= 0) {
            cout << "Invalid input. Please enter a number greater than 0: ";
            cin.clear();
            cin.ignore(256, '\n');
            cin >> x;
        }
        return x;
    }
    bool isValid(vector<VendingMachineObject> list_of_goods, Money change, Money collection) {
        int total_goods = list_of_goods.size();
        int out_of_stock = 0;
        bool changeEmpty = false;
        bool collectionEmpty = false;
        for (const auto& item : list_of_goods) {
            if (item.stock == 0) {
                out_of_stock++;
            }
        }
        if (change.bill100 == 0 || change.bill20 == 0 || change.coin10 == 0 || change.coin5 == 0 || change.coin1 == 0) {
            changeEmpty = true;
        }
        if (out_of_stock * 2 >= total_goods || changeEmpty || collectionEmpty) {
            return false;
        }
        return true;

    }
    void usermode() {
        int items;
        bool found;
        int input;
        int amounttopay;
        int inputmoney;
        int returnmoney;
        int x;
        bool valid;
        string action;
        Money change;
        Money collection;
        Money ChangeBox;
        Money CollectionBox;
        while (true) {
            found = false;
            VendingMachineObject targetedItem; 
            vector<VendingMachineObject> list_of_goods = get_update_information();
            ChangeBox = get_changebox();
            CollectionBox = get_collectionbox();
            cout << "Items available in the vendng machine:\n";

            for (auto item : list_of_goods) {
                cout << "ID: " << item.id << ", Name: " << item.name << ", Stock: " << displayStock(item.stock) << ", Price: " << item.price << endl;
            }
            valid = isValid(list_of_goods,ChangeBox,CollectionBox);
            if (!valid) {
                cout << "Not enough stock to continue, please contact the admin" << endl;
                return;
            }
            cout << "Enter " << list_of_goods.size() + 1 << " to exit" << endl;
            cout << "Choose which item you would like to purchase from the id" << endl;
            input = getint();
            if (input == list_of_goods.size() + 1){
                break;
            }
            for (const auto& item: list_of_goods) {
                if (input == item.id) {
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
                while (!enoughStock(ChangeBox, change)) {
                    cout << "Not enough money in the Changebox \n Please try to enter the exact amount" << endl;
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
                }
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
                action = "Purchased " + to_string(items) + " " + targetedItem.name;
                targetedItem.stock -= items;
                Modify_stock(targetedItem);
                addlogs(action, "User");
            }
        }       
    }
    void additem(int inital_stock) {
        bool choice;
        string name;
        int stock = inital_stock;
        int price;
        char input;
        string action;
        cout << "Enter the name of the item: ";
        cin >> name;
        cout << "Do you wish to Enter a a custom amount of item stock (y/n)" << endl;
        cin >> input;
        if (input == 'y'){
            cout << "Enter the stock of the item: ";
            stock = getmorethan0();
        }
        cout << "Enter the price of the item: ";
        price = getmorethan0();
        const char* sql = "INSERT INTO stock_67011177 (name, stock, price) VALUES (?, ?, ?);";
        sqlite3_stmt* stmt;
        rc = sqlite3_prepare_v2(db, sql, -1, &stmt, nullptr);
        if (rc != SQLITE_OK) {
            cerr << "SQL error: " << sqlite3_errmsg(db) << endl;
        }
        sqlite3_bind_text(stmt, 1, name.c_str(), -1, SQLITE_STATIC);
        sqlite3_bind_int(stmt, 2, stock);
        sqlite3_bind_int(stmt, 3, price);
        rc = sqlite3_step(stmt);
        if (rc != SQLITE_DONE) {
            cerr << "SQL error: " << sqlite3_errmsg(db) << endl;
        }
        sqlite3_finalize(stmt);
        cout << "Item added successfully!" << endl;
        addlogs("Added item " + name, "Admin");
        return;
    }
    int setinitialItem() {
        cout << "Set the default values of stock that items will be added" << endl;
        int id;
        id = getmorethan0();
        addlogs("Set initial stock to " + to_string(id), "Admin");
        return id;
    }
    void restockitem(vector<VendingMachineObject> items){
        int userinput;
        bool found = false;
        int newinput;
        char quit;
        string action;
        VendingMachineObject targetedItem;
        while (true) {
            for (auto item : items) {
                cout << "ID: " << item.id << ", Name: " << item.name << ", Stock: " << displayStock(item.stock) << ", Price: " << item.price << endl;
            }
            cout << "Enter the id of the item you wish to change the amount of stock to" << endl;
            cout << "Enter " << items.size() + 1 << "To go back to the admin panel" << endl;
            userinput = getmorethan0();
            if (userinput == items.size() + 1) {
                return;
            }
            for (auto item: items) {
                if (userinput == item.id){
                    found = true;
                    targetedItem = item;
                    break;
                }
            }
            if (!found) {
                cout << "ID not found" << endl;
                continue;
            }
            else{
                cout << "Initial Stock: " << targetedItem.stock << endl;
                cout << "Set the new stock for this object" << endl;
                newinput = getmorethan0();
                targetedItem.stock = newinput;
                cout << "Stock for " << targetedItem.name << " Changed to " << targetedItem.stock << endl;
                Modify_stock(targetedItem);
                action = "Restocked item id " + to_string(targetedItem.id);
                addlogs(action, "Admin");
                cout << "Done enter q to return to menu";
                cin >> quit;
                if (quit == 'q') {
                    return;
                }
            }
        }
    }   
    void restockChangebox() {
        Money change;
        cout << "Enter the amount of $100 bills: ";
        change.bill100 = getmorethan0();
        cout << "Enter the amount of $20 bills: ";
        change.bill20 = getmorethan0();
        cout << "Enter the amount of $10 coins: ";
        change.coin10 = getmorethan0();
        cout << "Enter the amount of $5 coins: ";
        change.coin5 = getmorethan0();
        cout << "Enter the amount of $1 coins: ";
        change.coin1 = getmorethan0();
        Money old = get_changebox();
        old.bill100 += change.bill100;
        old.bill20 += change.bill20;
        old.coin10 += change.coin10;
        old.coin5 += change.coin5;
        old.coin1 += change.coin1;
        modify_changebox(old);
        cout << "Changebox restocked successfully!" << endl;
        Money newchange = get_changebox();
        cout << "New Changebox: $100 bills: " << newchange.bill100 << ", $20 bills: " << newchange.bill20 << ", $10 coins: " << newchange.coin10 << ", $5 coins: " << newchange.coin5 << ", $1 coins: " << newchange.coin1 << endl;
        addlogs("Restocked Changebox", "Admin");
        return;
    }
    void ModifyCollectbox() {
        int choice;
        Money collection;
        Money old_collection;
        Money new_collection;
        while (true) {
            cout << "Please choose 1 to add 2 to remove 3 to return \n";
            choice = getint();
            switch (choice) {
                case 1: 
                    old_collection = get_collectionbox();
                    cout << "Enter the amount of $100 bills: ";
                    collection.bill100 = getmorethan0();
                    cout << "Enter the amount of $20 bills: ";
                    collection.bill20 = getmorethan0();
                    cout << "Enter the amount of $10 coins: ";
                    collection.coin10 = getmorethan0();
                    cout << "Enter the amount of $5 coins: ";
                    collection.coin5 = getmorethan0();
                    cout << "Enter the amount of $1 coins: ";
                    collection.coin1 = getmorethan0();
                    old_collection.bill100 += collection.bill100;
                    old_collection.bill20 += collection.bill20;
                    old_collection.coin10 += collection.coin10;
                    old_collection.coin5 += collection.coin5;
                    old_collection.coin1 += collection.coin1;
                    Modify_collectionbox(old_collection);
                    cout << "Collectionbox modified successfully!" << endl;
                    new_collection = get_collectionbox();
                    cout << "New Collectionbox: $100 bills: " << new_collection.bill100 << ", $20 bills: " << new_collection.bill20 << ", $10 coins: " << new_collection.coin10 << ", $5 coins: " << new_collection.coin5 << ", $1 coins: " << new_collection.coin1 << endl;
                    addlogs("Added into Collectionbox", "Admin");
                    break;
                case 2:
                    cout << "Enter the amount of $100 bills: ";
                    collection.bill100 = getmorethan0();
                    cout << "Enter the amount of $20 bills: ";
                    collection.bill20 = getmorethan0();
                    cout << "Enter the amount of $10 coins: ";
                    collection.coin10 = getmorethan0();
                    cout << "Enter the amount of $5 coins: ";
                    collection.coin5 = getmorethan0();
                    cout << "Enter the amount of $1 coins: ";
                    collection.coin1 = getmorethan0();
                    old_collection = get_collectionbox();
                    cout << "Old Collectionbox: $100 bills: " << old_collection.bill100 << ", $20 bills: " << old_collection.bill20 << ", $10 coins: " << old_collection.coin10 << ", $5 coins: " << old_collection.coin5 << ", $1 coins: " << old_collection.coin1 << endl;
                    if (old_collection.bill100 - collection.bill100 < 0) {
                        cout << "Collection Box cant be lower than 0 setting to 0" << endl;
                        old_collection.bill100 = 0;
                    }
                    else{
                        old_collection.bill100 -= collection.bill100;
                    }
                    if (old_collection.bill20 - collection.bill20 < 0) {
                        cout << "Collection Box cant be lower than 0 setting to 0" << endl;
                        old_collection.bill20 = 0;
                    }
                    else{
                        old_collection.bill20 -= collection.bill20;
                    }
                    if (old_collection.coin10 - collection.coin10 < 0) {
                        cout << "Collection Box cant be lower than 0 setting to 0" << endl;
                        old_collection.coin10 = 0;
                    }
                    else{
                        old_collection.coin10 -= collection.coin10;
                    }
                    if (old_collection.coin5 - collection.coin5 < 0) {
                        cout << "Collection Box cant be lower than 0 setting to 0" << endl;
                        old_collection.coin5 = 0;
                    }
                    else{
                        old_collection.coin5 -= collection.coin5;
                    }
                    if (old_collection.coin1 - collection.coin1 < 0) {
                        cout << "Collection Box cant be lower than 0 setting to 0" << endl;
                        old_collection.coin1 = 0;
                    }
                    else{
                        old_collection.coin1 -= collection.coin1;
                    }
                    Modify_collectionbox(old_collection);
                    cout << "Collectionbox emptied successfully!" << endl;
                    new_collection = get_collectionbox();
                    cout << "New Collectionbox: $100 bills: " << new_collection.bill100 << ", $20 bills: " << new_collection.bill20 << ", $10 coins: " << new_collection.coin10 << ", $5 coins: " << new_collection.coin5 << ", $1 coins: " << new_collection.coin1 << endl;
                    addlogs("Removed from Collectionbox", "Admin");
                    break;
                case 3:
                    return;
                default:
                    cout << "Invalid choice. Please try again.\n";
                    break;
            }
        }
    }
    void addlogs(string action, string doneby) {
        const char* sql = "INSERT INTO logs (action, doneby) VALUES (?, ?);";
        sqlite3_stmt* stmt;
        rc = sqlite3_prepare_v2(db, sql, -1, &stmt, nullptr);
        if (rc != SQLITE_OK) {
            cerr << "SQL error: " << sqlite3_errmsg(db) << endl;
        }
        sqlite3_bind_text(stmt, 1, action.c_str(), -1, SQLITE_STATIC);
        sqlite3_bind_text(stmt, 2, doneby.c_str(), -1, SQLITE_STATIC);
        rc = sqlite3_step(stmt);
        if (rc != SQLITE_DONE) {
            cerr << "SQL error: " << sqlite3_errmsg(db) << endl;
        }
        sqlite3_finalize(stmt);
    }
    void checkChangebox() {
        Money change = get_changebox();
        cout << "Changebox: $100 bills: " << change.bill100 << ", $20 bills: " << change.bill20 << ", $10 coins: " << change.coin10 << ", $5 coins: " << change.coin5 << ", $1 coins: " << change.coin1 << endl;
        int amount = change.bill100 * 100 + change.bill20 * 20 + change.coin10 * 10 + change.coin5 * 5 + change.coin1;
        cout << "Total amount in the changebox: " << amount << endl;
        addlogs("Checked Changebox", "Admin");
        return ;
    }
    void checkCollectionbox() {
        Money collection = get_collectionbox();
        cout << "Collectionbox: $100 bills: " << collection.bill100 << ", $20 bills: " << collection.bill20 << ", $10 coins: " << collection.coin10 << ", $5 coins: " << collection.coin5 << ", $1 coins: " << collection.coin1 << endl;
        int amount = collection.bill100 * 100 + collection.bill20 * 20 + collection.coin10 * 10 + collection.coin5 * 5 + collection.coin1;
        cout << "Total amount in the collectionbox: " << amount << endl;
        addlogs("Checked Collectionbox", "Admin");
        return ;
    }
    void adminmode() {
        int inital_stock = 20;
        vector<VendingMachineObject> item;
        item = get_update_information();
        cout << "Admin mode activated.\n";
        while (true) {
            int choice;
            cout << "Please choose from these options: \n";
            cout << "1: Add item\n2: Set initial stock\n3: Restock item\n4: Check Changebox\n5: Check Collectionbox\n6: Modify Collectionbox\n7: Restock Changebox\n8: Check Logs\n9: Exit admin mode\n";
            cout << "Enter your choice: ";
            choice = getint();

            switch (choice) {
            case 1:
                additem(inital_stock);
                break;
            case 2:
                inital_stock = setinitialItem();
                break;
            case 3:
                restockitem(item);
                break;
            case 4:
                checkChangebox();
                break;
            case 5:
                checkCollectionbox();
                break;
            case 6:
                ModifyCollectbox();
                break;
            case 7:
                restockChangebox();
                break;
            case 8:
                printlogs();
                break;
            case 9:
                cout << "Exiting admin mode.\n";
                return;
            default:
                cout << "Invalid choice. Please try again.\n";
                break;
            }
        }
        return;
    }
    void onexit() {
        cout << "Exiting the vending machine. Goodbye!\n";
        sqlite3_close(db);
        return;
    }
    void printlogs() {
        auto callback = [](void* data, int argc, char** argv, char** azColName) -> int {
            for (int i = 0; i < argc; i++) {
                cout << azColName[i] << ": " << (argv[i] ? argv[i] : "NULL") << endl;
            }
            cout << endl;
            return 0;
        };
        const char* sql = "SELECT * FROM logs;";
        if (sqlite3_exec(db, sql, callback, nullptr, nullptr) != SQLITE_OK) {
            cerr << "SQL error: " << sqlite3_errmsg(db) << endl;
        }
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

        CREATE TABLE IF NOT EXISTS collectionbox (
        id INTEGER PRIMARY KEY CHECK (id = 1),
        Bill_100 INTEGER NOT NULL,
        Bill_20 INTEGER NOT NULL,
        Coin_10 INTEGER NOT NULL,
        Coin_5 INTEGER NOT NULL,
        Coin_1 INTEGER NOT NULL
        );

        CREATE TABLE IF NOT EXISTS changebox (
        id INTEGER PRIMARY KEY CHECK (id = 1),
        Bill_100 INTEGER NOT NULL,
        Bill_20 INTEGER NOT NULL,
        Coin_10 INTEGER NOT NULL,
        Coin_5 INTEGER NOT NULL,
        Coin_1 INTEGER NOT NULL
        );

        CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        action TEXT NOT NULL,
        doneby TEXT NOT NULL
        );
        )";    
        rc = sqlite3_exec(db, createTableSQL, nullptr, nullptr, &errMsg);
        if (rc != SQLITE_OK) {
            cerr << "SQL error: " << errMsg << endl;
            sqlite3_free(errMsg);
        } else {
            cout << "Table created successfully!" << endl;
        }
        const char* insertCollectionBox = R"(
        INSERT INTO collectionbox (id, Bill_100, Bill_20, Coin_10, Coin_5, Coin_1) VALUES (1, 0, 0, 0, 0, 0) ON CONFLICT(id) DO NOTHING;
        INSERT INTO changebox (id, Bill_100, Bill_20, Coin_10, Coin_5, Coin_1) VALUES (1, 100, 100, 100, 100, 100) ON CONFLICT(id) DO NOTHING;
        )";
        rc = sqlite3_exec(db, insertCollectionBox, nullptr, nullptr, &errMsg);
        if (rc != SQLITE_OK) {
            cerr << "SQL error: " << errMsg << endl;
            sqlite3_free(errMsg);
        } else {
            cout << "Line sucessfully inserted created successfully!" << endl;
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
