#include "mainwindow.h"
#include "./ui_mainwindow.h"
#include <QtSql>
#include <QSqlQuery>
#include <QSqlError>
#include <QDebug>
#include <QLabel>
#include <QGridLayout>
#include <QMessageBox>
#include "item.h"


MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    setupDatabase();
    additems();
    ui->Id_display->setText(DisplaySelected);
    checkStockAndDisableMachine();
    ui->State->setText("Current Status: Waiting: ");
    adminPanel = new AdminPanel(this);

}

MainWindow::~MainWindow()
{
    delete ui;

    if (db.isOpen()) {
        db.close();
    }
    QString connectionName = db.connectionName();
    db = QSqlDatabase();
    QSqlDatabase::removeDatabase(connectionName);

    if (adminPanel) {
        delete adminPanel;
        adminPanel = nullptr;
    }

    for (Item* item : itemWidgets) {
        delete item;
    }
    itemWidgets.clear();
}
QSqlDatabase& MainWindow::getDatabase() {
    return db;
}
void MainWindow::on_AdminToggle_clicked()
{
    if (!adminPanel) {
        adminPanel = new AdminPanel(this);
    }
    this->hide();
    adminPanel->show();
}

void MainWindow::showMainWindow() {
    this -> show();
}
void MainWindow::setupDatabase()
{
    db = QSqlDatabase::addDatabase("QSQLITE");
    db.setDatabaseName("stock_67011177.db");

    if (!db.open()) {
        qDebug() << "Error: Failed to open database!" << db.lastError().text();
    } else {
        qDebug() << "Database connected successfully!";
    }

    QSqlQuery query;
    query.exec("CREATE TABLE IF NOT EXISTS stock_67011177 (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, stock INTEGER NOT NULL, price INTEGER NOT NULL);");
    query.exec("CREATE TABLE IF NOT EXISTS collectionbox (id INTEGER PRIMARY KEY CHECK (id = 1), Bill_100 INTEGER NOT NULL, Bill_20 INTEGER NOT NULL, Coin_10 INTEGER NOT NULL, Coin_5 INTEGER NOT NULL, Coin_1 INTEGER NOT NULL,  Max_Capacity INTEGER NOT NULL);");
    query.exec("CREATE TABLE IF NOT EXISTS changebox (id INTEGER PRIMARY KEY CHECK (id = 1), Bill_100 INTEGER NOT NULL, Bill_20 INTEGER NOT NULL, Coin_10 INTEGER NOT NULL, Coin_5 INTEGER NOT NULL, Coin_1 INTEGER NOT NULL);");
    query.exec("CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY AUTOINCREMENT, action TEXT NOT NULL, doneby TEXT NOT NULL);");
    query.exec("INSERT INTO collectionbox (id, Bill_100, Bill_20, Coin_10, Coin_5, Coin_1, Max_Capacity) VALUES (1, 0, 0, 0, 0, 0, 1000) ON CONFLICT(id) DO NOTHING;");
    query.exec("INSERT INTO changebox (id, Bill_100, Bill_20, Coin_10, Coin_5, Coin_1) VALUES (1, 100, 100, 100, 100, 100) ON CONFLICT(id) DO NOTHING;");
    query.exec("SELECT COUNT(*) FROM stock_67011177;");
    query.next();
    int count = query.value(0).toInt();

    if (count == 0) {
        query.exec("INSERT INTO stock_67011177 (name, stock, price) VALUES ('Soda', 20, 50);");
        query.exec("INSERT INTO stock_67011177 (name, stock, price) VALUES ('Chips', 15, 30);");
        query.exec("INSERT INTO stock_67011177 (name, stock, price) VALUES ('Candy Bar', 25, 20);");
        query.exec("INSERT INTO stock_67011177 (name, stock, price) VALUES ('Water Bottle', 30, 15);");
        query.exec("INSERT INTO stock_67011177 (name, stock, price) VALUES ('Gum Pack', 40, 10);");
        query.exec("INSERT INTO stock_67011177 (name, stock, price) VALUES ('Cookies', 10, 40);");
        query.exec("INSERT INTO stock_67011177 (name, stock, price) VALUES ('Energy Drink', 12, 60);");
        query.exec("INSERT INTO stock_67011177 (name, stock, price) VALUES ('Granola Bar', 18, 25);");
        query.exec("INSERT INTO stock_67011177 (name, stock, price) VALUES ('Crackers', 20, 35);");
        query.exec("INSERT INTO stock_67011177 (name, stock, price) VALUES ('Juice Box', 22, 45);");
        query.exec("INSERT INTO stock_67011177 (name, stock, price) VALUES ('Milk Carton', 15, 50);");
        query.exec("INSERT INTO stock_67011177 (name, stock, price) VALUES ('Fruit Snacks', 30, 20);");
        query.exec("INSERT INTO stock_67011177 (name, stock, price) VALUES ('Trail Mix', 12, 55);");
        query.exec("INSERT INTO stock_67011177 (name, stock, price) VALUES ('Pretzels', 18, 25);");
        query.exec("INSERT INTO stock_67011177 (name, stock, price) VALUES ('Popcorn', 20, 30);");
        query.exec("INSERT INTO stock_67011177 (name, stock, price) VALUES ('Chocolate Bar', 25, 45);");
        query.exec("INSERT INTO stock_67011177 (name, stock, price) VALUES ('Ice Tea', 10, 50);");
        query.exec("INSERT INTO stock_67011177 (name, stock, price) VALUES ('Yogurt Cup', 8, 60);");
        query.exec("INSERT INTO stock_67011177 (name, stock, price) VALUES ('Bagel', 10, 40);");
        query.exec("INSERT INTO stock_67011177 (name, stock, price) VALUES ('Donut', 15, 35);");

        qDebug() << "Default items inserted into stock table.";
    } else {
        qDebug() << "Stock table already contains items.";
    }
}

void MainWindow::additems() {
    QWidget *container = new QWidget;
    QGridLayout *layout = new QGridLayout(container);
    container->setLayout(layout);
    ui->ItemDisplay->setWidget(container);
    ui->ItemDisplay->setWidgetResizable(true);
    QSqlQuery query;
    query.exec("SELECT id, name, stock, price FROM stock_67011177;");
    int row = 0;
    int col = 0;
    const int per = 3;
    while (query.next()) {
        QString id = query.value(0).toString();
        QString name = query.value(1).toString();
        QString Names = id + " " + name;
        int price = query.value(3).toInt();
        int stock = query.value(2).toInt();
        Item *item = new Item(Names,price,stock);
        layout->addWidget(item, row, col);
        itemWidgets.append(item);
        col++;
        if (col >= per) {
            col = 0;
            row++;
        }
    }
    container->setLayout(layout);
    ui->ItemDisplay->setWidget(container);
    ui->ItemDisplay->setWidgetResizable(true);
}

void MainWindow::on_btn1_clicked()
{
    DisplaySelected += "1";
    ui->Id_display->setText(DisplaySelected);

}


void MainWindow::on_btn0_clicked()
{
    DisplaySelected += "0";
    ui->Id_display->setText(DisplaySelected);
}


void MainWindow::on_btn2_clicked()
{
    DisplaySelected += "2";
    ui->Id_display->setText(DisplaySelected);
}


void MainWindow::on_btn3_clicked()
{
    DisplaySelected += "3";
    ui->Id_display->setText(DisplaySelected);
}


void MainWindow::on_btn4_clicked()
{
    DisplaySelected += "4";
    ui->Id_display->setText(DisplaySelected);
}


void MainWindow::on_btn5_clicked()
{
    DisplaySelected += "5";
    ui->Id_display->setText(DisplaySelected);
}


void MainWindow::on_btn6_clicked()
{
    DisplaySelected += "6";
    ui->Id_display->setText(DisplaySelected);
}


void MainWindow::on_btn7_clicked()
{
    DisplaySelected += "7";
    ui->Id_display->setText(DisplaySelected);
}


void MainWindow::on_btn8_clicked()
{
    DisplaySelected += "8";
    ui->Id_display->setText(DisplaySelected);
}


void MainWindow::on_btn9_clicked()
{
    DisplaySelected += "9";
    ui->Id_display->setText(DisplaySelected);
}


void MainWindow::on_Delete_clicked()
{
    DisplaySelected.chop(1);
    ui->Id_display->setText(DisplaySelected);

}


void MainWindow::on_Enter_clicked()
{
    int selected_id = DisplaySelected.toInt();
    if (selected_id > itemWidgets.size()) {
        QMessageBox::warning(nullptr, "Warning", "ID not found");
        return;
    }
    Selected_id = DisplaySelected.toInt() - 1;
    ui->State->setText("Purchasing Id: " + QString::number(Selected_id + 1));
    Amount_due = itemWidgets[Selected_id]->price;
    ui->Pay->setText("Total To Pay: " + QString::number(Amount_due));
    DisplaySelected = "";
    ui->Id_display->setText(DisplaySelected);

}
void MainWindow::buyItem(int index)
{
    if (index < 0) {
        QMessageBox::warning(nullptr, "Warning", "Invalid ID");
        return;
    }
    QSqlQuery query;

    query.prepare("SELECT price, stock FROM stock_67011177 WHERE id = :id");
    query.bindValue(":id", index + 1);

    if (!query.exec() || !query.next()) {
        qDebug() << "Item not found or query failed:" << query.lastError().text();
        return;
    }

    int currentStock = query.value(1).toInt();
    int price = query.value(0).toInt();
    if (insertedMoney < price) {
        QMessageBox::warning(nullptr, "Warning", "Not Enough Money please add more");
        return;
    }
    if (currentStock <= 0) {
        qDebug() << "Item out of stock!";
        QMessageBox::warning(nullptr, "Warning", "This item is out of stock!");
        return;
    }
    calculateChangeAndUpdateDatabase();
    query.prepare("UPDATE stock_67011177 SET stock = stock - 1 WHERE id = :id");
    query.bindValue(":id", index + 1);

    if (!query.exec()) {
        qDebug() << "Error updating stock:" << query.lastError().text();
        return;
    }

    // Fetch updated stock value
    query.prepare("SELECT stock FROM stock_67011177 WHERE id = :id");
    query.bindValue(":id", index + 1);

    if (!query.exec() || !query.next()) {
        qDebug() << "Error fetching updated stock:" << query.lastError().text();
        return;
    }
    Selected_id = -1;
    ui->State->setText("Waiting for next purchase: ");
    int newQuantity = query.value(0).toInt();
    Amount_due = 0;
    ui->Pay->setText("Total To Pay: ");
    itemWidgets[index]->updateQuantity(newQuantity);
    adminPanel->AdminWidgets[index]->updateQuantity(newQuantity);
    checkStockAndDisableMachine();
}

void MainWindow::insertMoney(int amount)
{
    insertedMoney += amount;

    QString columnName;

    if (amount == 100) columnName = "Bill_100";
    else if (amount == 20) columnName = "Bill_20";
    else if (amount == 10) columnName = "Coin_10";
    else if (amount == 5) columnName = "Coin_5";
    else if (amount == 1) columnName = "Coin_1";

    if (!columnName.isEmpty()) {
        QSqlQuery query;
        query.prepare("UPDATE collectionbox SET " + columnName + " = " + columnName + " + 1 WHERE id = 1");

        if (!query.exec()) {
            qDebug() << "Error updating" << columnName << ":" << query.lastError().text();
        }
    }

    ui->Amount->setText("Inserted: " + QString::number(insertedMoney));
}

void MainWindow::on_Buy_clicked()
{
    if(Selected_id < itemWidgets.size()) {
        buyItem(Selected_id);
    }
    else {
        QMessageBox::warning(nullptr, "Warning", "ID not found");
    }
    addlogs("Bought item ID " + QString::number(Selected_id + 1), "user");

}


void MainWindow::on_add100_clicked()
{
    insertMoney(100);
    addlogs("Inserted 100$", "user");

}


void MainWindow::on_add20_clicked()
{
    insertMoney(20);
    addlogs("Inserted 20$", "user");

}


void MainWindow::on_add10_clicked()
{
    insertMoney(10);
    addlogs("Inserted 10$", "user");

}


void MainWindow::on_add5_clicked()
{
    insertMoney(5);
    addlogs("Inserted 5$", "user");


}
void MainWindow::calculateChangeAndUpdateDatabase() {
    int change = insertedMoney - Amount_due;
    if (change < 0) {
        QMessageBox::warning(nullptr, "Error", "Not enough money inserted!");
        return;
    }
    QSqlQuery query;
    int remainingChange = change;
    int bills100 = remainingChange / 100;
    remainingChange %= 100;
    query.prepare("UPDATE changebox SET Bill_100 = Bill_100 - :bills100 WHERE id = 1");
    query.bindValue(":bills100", bills100);
    if (!query.exec()) {
        qDebug() << "Error updating Bill_100:" << query.lastError().text();
        return;
    }

    // Deduct Bill 20
    int bills20 = remainingChange / 20;
    remainingChange %= 20;
    query.prepare("UPDATE changebox SET Bill_20 = Bill_20 - :bills20 WHERE id = 1");
    query.bindValue(":bills20", bills20);
    if (!query.exec()) {
        qDebug() << "Error updating Bill_20:" << query.lastError().text();
        return;
    }

    // Deduct Coin 10
    int coin10 = remainingChange / 10;
    remainingChange %= 10;
    query.prepare("UPDATE changebox SET Coin_10 = Coin_10 - :coin10 WHERE id = 1");
    query.bindValue(":coin10", coin10);
    if (!query.exec()) {
        qDebug() << "Error updating Coin_10:" << query.lastError().text();
        return;
    }

    // Deduct Coin 5
    int coin5 = remainingChange / 5;
    remainingChange %= 5;
    query.prepare("UPDATE changebox SET Coin_5 = Coin_5 - :coin5 WHERE id = 1");
    query.bindValue(":coin5", coin5);
    if (!query.exec()) {
        qDebug() << "Error updating Coin_5:" << query.lastError().text();
        return;
    }

    // Deduct Coin 1
    int coin1 = remainingChange / 1;
    remainingChange %= 1;
    query.prepare("UPDATE changebox SET Coin_1 = Coin_1 - :coin1 WHERE id = 1");
    query.bindValue(":coin1", coin1);
    if (!query.exec()) {
        qDebug() << "Error updating Coin_1:" << query.lastError().text();
        return;
    }
    if (remainingChange > 0) {
        QMessageBox::warning(nullptr, "Error", "Unable to provide exact change.");
        return;
    }
    insertedMoney = 0;
    ui->Amount->setText("Inserted: " + QString::number(insertedMoney));
    QString changeMessage = "Change: " + QString::number(change);
    QMessageBox::information(nullptr, "Purchase Complete", changeMessage);
}

void MainWindow::on_add1_clicked()
{
    insertMoney(1);
    addlogs("Inserted 1$", "user");
}
void MainWindow::checkStockAndDisableMachine()
{
    QSqlQuery query;
    query.prepare("SELECT COUNT(*) FROM stock_67011177");
    if (!query.exec() || !query.next()) {
        qDebug() << "Error fetching total number of items:" << query.lastError().text();
        return;
    }

    int totalItems = query.value(0).toInt();
    int outOfStockCount = 0;

    query.prepare("SELECT stock FROM stock_67011177");
    if (!query.exec()) {
        qDebug() << "Error fetching item stock:" << query.lastError().text();
        return;
    }

    while (query.next()) {
        int stock = query.value(0).toInt();
        if (stock == 0) {
            outOfStockCount++;
        }
    }

    if (outOfStockCount > totalItems / 2) {
        disableMachine();
    } else {
        enableMachine();
    }
}
void MainWindow::disableMachine()
{
    ui->Buy->setEnabled(false);
    ui->Delete->setEnabled(false);
    ui->Enter->setEnabled(false);
    ui->btn0->setEnabled(false);
    ui->btn1->setEnabled(false);
    ui->btn2->setEnabled(false);
    ui->btn3->setEnabled(false);
    ui->btn4->setEnabled(false);
    ui->btn5->setEnabled(false);
    ui->btn6->setEnabled(false);
    ui->btn7->setEnabled(false);
    ui->btn8->setEnabled(false);
    ui->btn9->setEnabled(false);
    ui->add1->setEnabled(false);
    ui->add5->setEnabled(false);
    ui->add10->setEnabled(false);
    ui->add20->setEnabled(false);
    ui->add100->setEnabled(false);

    QMessageBox::warning(nullptr, "Machine Unusable", "The machine is currently unusable because more than half of the items are out of stock.");
}
void MainWindow::enableMachine()
{
    ui->Buy->setEnabled(true);
    ui->Delete->setEnabled(true);
    ui->Enter->setEnabled(true);
    ui->btn0->setEnabled(true);
    ui->btn1->setEnabled(true);
    ui->btn2->setEnabled(true);
    ui->btn3->setEnabled(true);
    ui->btn4->setEnabled(true);
    ui->btn5->setEnabled(true);
    ui->btn6->setEnabled(true);
    ui->btn7->setEnabled(true);
    ui->btn8->setEnabled(true);
    ui->btn9->setEnabled(true);
    ui->add1->setEnabled(true);
    ui->add5->setEnabled(true);
    ui->add10->setEnabled(true);
    ui->add20->setEnabled(true);
    ui->add100->setEnabled(true);
}
void MainWindow::addlogs(QString action, QString doneby) {
    QSqlQuery query;
    query.prepare("INSERT INTO logs (action, doneby) VALUES (:action, :doneby);");
    query.bindValue(":action",action);
    query.bindValue(":doneby",doneby);
    query.exec();
}

