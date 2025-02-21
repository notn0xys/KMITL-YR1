#include "adminpanel.h"
#include "ui_adminpanel.h"
#include "mainwindow.h"
#include "./ui_adminpanel.h"
#include <QMessageBox>
#include <QSqlQuery>
#include <QSqlError>
#include <QDebug>
#include <QVBoxLayout>
#include "logs.h"
AdminPanel::AdminPanel(MainWindow *parent)
    : QMainWindow(parent)
    , ui(new Ui::AdminPanel)
    , mainWin(parent)
{
    ui->setupUi(this);
    setAttribute(Qt::WA_DeleteOnClose);
    populateItems();
}

AdminPanel::~AdminPanel()
{
    this->hide();
    mainWin->showMainWindow();
    mainWin->activateWindow();
    mainWin->raise();
    QCoreApplication::processEvents();
}

void AdminPanel::on_Back_clicked()
{
    this->hide();
    mainWin->showMainWindow();
    mainWin->activateWindow();
    mainWin->raise();
    QCoreApplication::processEvents();
}
void AdminPanel::populateItems(){
    QWidget *container = new QWidget;
    QVBoxLayout *layout = new QVBoxLayout(container);
    container->setLayout(layout);
    ui->ItemArea->setWidget(container);
    ui->ItemArea->setWidgetResizable(true);
    int i = 0;
    for (auto originalItem:mainWin->itemWidgets) {
        QString name = originalItem->name;
        Item *newItem = new Item(name, originalItem->price, originalItem->quantity);
        AdminWidgets.append(newItem);
        layout->addWidget(newItem);
        i++;
    }
    container->setLayout(layout);
    ui->ItemArea->setWidget(container);
    ui->ItemArea->setWidgetResizable(true);
}

void AdminPanel::on_updateStock_clicked()
{
    bool ok;
    QString id = ui->ID_Entry->text();
    QString amount = ui->Amount_Entry->text();
    int id_num = id.toInt(&ok);
    if (!ok) {
        QMessageBox::warning(this, "Warning", "Please only Enter Intergers");
        return;
    }
    int amount_num = amount.toInt(&ok);
    if (!ok) {
        QMessageBox::warning(this, "Warning", "Please only Enter Intergers");
        return;
    }
    QSqlQuery query;
    query.prepare("UPDATE stock_67011177 SET stock = :stock WHERE id = :id;");
    query.bindValue(":stock", amount_num);
    query.bindValue(":id", id_num);

    if (!query.exec()) {
        qDebug() << "Update failed:" << query.lastError().text();
    }
    mainWin->itemWidgets[id_num-1]->updateQuantity(amount_num);
    AdminWidgets[id_num - 1]->updateQuantity(amount_num);
    query.clear();
    mainWin->addlogs("Updated Stock for ID " + QString::number(id_num), "Admin");
    mainWin->checkStockAndDisableMachine();

}


void AdminPanel::on_CollectionBtn_clicked()
{
    int total_amount = 0;
    QSqlQuery query;
    query.exec("SELECT Bill_100 , Bill_20 ,Coin_10 ,Coin_5 ,Coin_1 FROM collectionbox WHERE id = 1;");
    query.next();
    int hundreds = query.value(0).toInt() * 100;
    int twenty = query.value(1).toInt() * 20;
    int ten = query.value(2).toInt() * 10;
    int five = query.value(3).toInt() * 5;
    int one = query.value(4).toInt();

    total_amount = hundreds + twenty + ten + five + one;
    ui -> CollectionLabel->setText("Amount: $" + QString::number(total_amount));
    query.clear();
    mainWin->addlogs("Checked Collection Box", "Admin");

}


void AdminPanel::on_ChangeBtn_clicked()
{
    int total_amount = 0;
    QSqlQuery query;
    query.exec("SELECT Bill_100 , Bill_20 ,Coin_10 ,Coin_5 ,Coin_1 FROM changebox WHERE id = 1;");
    query.next();
    int hundreds = query.value(0).toInt();
    int twenty = query.value(1).toInt();
    int ten = query.value(2).toInt();
    int five = query.value(3).toInt();
    int one = query.value(4).toInt();

    ui->change1->setText(QString::number(one));
    ui->change5->setText(QString::number(five));
    ui->change10->setText(QString::number(ten));
    ui->change20->setText(QString::number(twenty));
    ui->change100->setText(QString::number(hundreds));
    query.clear();
    mainWin->addlogs("Checked Change Box", "Admin");


}


void AdminPanel::on_Empt_Collection_clicked()
{
    QSqlQuery query;
    query.prepare("UPDATE collectionbox SET Bill_100 = 0, Bill_20 = 0, Coin_10 = 0, Coin_5 = 0, Coin_1 = 0 WHERE id = 1;");
    query.exec();
    QMessageBox::information(this, "Success", "The collection box has been emptied.");
    ui->CollectionLabel->setText("Amount: $0");
    query.clear();
    mainWin->addlogs("Emptied Collection Box", "Admin");
    mainWin->checkCollectionboxAndDisableMachine();


}
int AdminPanel::get_amount() {
    QString amnt = ui->changeEntry->text().trimmed();
    bool ok;
    int amount = amnt.toInt(&ok);
    if (!ok) {
        QMessageBox::warning(this, "Error", "Invalid Data Type");
        return 0;
    }
    return amount;
}

void AdminPanel::on_refill100_clicked()
{
    int amount = get_amount();
    QSqlQuery query;
    query.exec("SELECT Bill_100 FROM changebox WHERE id = 1;");
    query.next();
    int original = query.value(0).toInt();
    original += amount;
    query.prepare("UPDATE changebox SET Bill_100 = :bill WHERE id = 1;");
    query.bindValue(":bill",original);
    query.exec();
    ui->change100->setText(QString::number(original));
    mainWin->addlogs("Refilled 100$ bills in the changebox", "Admin");
    mainWin->checkChangeboxAndDisableMachine();

}


void AdminPanel::on_refill20_clicked()
{
    int amount = get_amount();
    QSqlQuery query;
    query.exec("SELECT Bill_20 FROM changebox WHERE id = 1;");
    query.next();
    int original = query.value(0).toInt();
    original += amount;
    query.prepare("UPDATE changebox SET Bill_20 = :bill WHERE id = 1;");
    query.bindValue(":bill",original);
    query.exec();
    ui->change20->setText(QString::number(original));
    mainWin->addlogs("Refilled 20$ bills in the changebox", "Admin");
    mainWin->checkChangeboxAndDisableMachine();


}


void AdminPanel::on_refill10_clicked()
{
    int amount = get_amount();
    QSqlQuery query;
    query.exec("SELECT Coin_10 FROM changebox WHERE id = 1;");
    query.next();
    int original = query.value(0).toInt();
    original += amount;
    query.prepare("UPDATE changebox SET Coin_10 = :bill WHERE id = 1;");
    query.bindValue(":bill",original);
    query.exec();
    ui->change10->setText(QString::number(original));
    mainWin->addlogs("Refilled 10$ coins in the changebox", "Admin");
    mainWin->checkChangeboxAndDisableMachine();


}


void AdminPanel::on_refill5_clicked()
{
    int amount = get_amount();
    QSqlQuery query;
    query.exec("SELECT Coin_5 FROM changebox WHERE id = 1;");
    query.next();
    int original = query.value(0).toInt();
    original += amount;
    query.prepare("UPDATE changebox SET Coin_5 = :bill WHERE id = 1;");
    query.bindValue(":bill",original);
    query.exec();
    ui->change5->setText(QString::number(original));
    mainWin->addlogs("Refilled 5$ coins in the changebox", "Admin");
    mainWin->checkChangeboxAndDisableMachine();


}


void AdminPanel::on_refill1_clicked()
{
    int amount = get_amount();
    QSqlQuery query;
    query.exec("SELECT Coin_1 FROM changebox WHERE id = 1;");
    query.next();
    int original = query.value(0).toInt();
    original += amount;
    query.prepare("UPDATE changebox SET Coin_1 = :bill WHERE id = 1;");
    query.bindValue(":bill",original);
    query.exec();
    ui->change1->setText(QString::number(original));
    mainWin->addlogs("Refilled 1$ bills in the changebox", "Admin");
    mainWin->checkChangeboxAndDisableMachine();


}
void AdminPanel::loadlogs() {
    QWidget *container = new QWidget;
    QVBoxLayout *layout = new QVBoxLayout(container);
    container->setLayout(layout);
    QSqlQuery query;
    query.exec("SELECT action, doneby FROM logs ORDER BY id DESC");
    while (query.next()) {
        QString action = query.value(0).toString();
        QString doneby = query.value(1).toString();

        Logs *logEntry = new Logs(action, doneby);
        layout->addWidget(logEntry);
    }
    ui->LogsArea->setWidget(container);
    ui->LogsArea->setWidgetResizable(true);
}
//Logs btn forgot to rename
void AdminPanel::on_pushButton_clicked()
{
    loadlogs();
}

void AdminPanel::addItemToAdminPanel(const QString &name, int stock, int price)
{
    // Create a new item widget for the Admin Panel
    Item *adminItem = new Item(name, price, stock);
    AdminWidgets.append(adminItem);

    // Get the layout from `ItemArea` and add the new item
    QVBoxLayout *adminLayout = qobject_cast<QVBoxLayout*>(ui->ItemArea->widget()->layout());
    if (adminLayout) {
        adminLayout->addWidget(adminItem);
    }

    qDebug() << "Item added to Admin Panel:" << name;
}
void AdminPanel::on_AddItemButton_clicked()
{
    bool ok;
    QString name = ui->ItemNameEntry->text();
    int price = ui->ItemPriceEntry->text().toInt(&ok);
    if (!ok) {
        return;
    }
    int stock;
    bool okStock;
    if (ui->UseDefaultStockCheckBox->isChecked()) {
        stock = mainWin->default_stock;
    } else {
        stock = ui->ItemStockEntry->text().toInt(&okStock);
        if (!okStock) {
            QMessageBox::warning(this, "Invalid Input", "Please enter a valid stock quantity.");
            return;
        }
    }

    if (name.isEmpty() || stock <= 0 || price <= 0) {
        QMessageBox::warning(this, "Invalid Input", "Please enter valid item details.");
        return;
    }

    mainWin->addItem(name, stock, price);
}



void AdminPanel::on_pushButton_2_clicked()
{
    ui->DefaultStock->setText(QString::number(mainWin->default_stock));
}


void AdminPanel::on_UpdateDefaultStock_clicked()
{
    bool ok;
    QString amounts = ui->NewStockEntry->text();
    int amount = amounts.toInt(&ok);
    if (!ok) {
        QMessageBox::warning(this, "Invalid Input", "Please enter valid item details.");
        return;
    }
    mainWin->default_stock = amount;
}

