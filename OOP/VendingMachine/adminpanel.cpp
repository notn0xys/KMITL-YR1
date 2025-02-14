#include "adminpanel.h"
#include "ui_adminpanel.h"
#include "mainwindow.h"
#include "./ui_adminpanel.h"
#include <QMessageBox>
#include <QSqlQuery>
#include <QSqlError>
#include <QDebug>
#include <QVBoxLayout>
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
}


void AdminPanel::on_ChangeBtn_clicked()
{
    int total_amount = 0;
    QSqlQuery query;
    query.exec("SELECT Bill_100 , Bill_20 ,Coin_10 ,Coin_5 ,Coin_1 FROM changebox WHERE id = 1;");
    query.next();
    int hundreds = query.value(0).toInt() * 100;
    int twenty = query.value(1).toInt() * 20;
    int ten = query.value(2).toInt() * 10;
    int five = query.value(3).toInt() * 5;
    int one = query.value(4).toInt();

    total_amount = hundreds + twenty + ten + five + one;
    query.clear();
}


void AdminPanel::on_Empt_Collection_clicked()
{
    QSqlQuery query;
    query.prepare("UPDATE collectionbox SET Bill_100 = 0, Bill_20 = 0, Coin_10 = 0, Coin_5 = 0, Coin_1 = 0 WHERE id = 1;");
    query.exec();
    QMessageBox::information(this, "Success", "The collection box has been emptied.");
    ui->CollectionLabel->setText("Amount: $0");
    query.clear();
}
int AdminPanel::get_amount() {
    QString amnt = ui->Amount_Entry->text();
    bool ok;
    int amount = amnt.toInt(&ok);
    if (!ok) {
        QMessageBox::warning(this,"Error","Invalid Data Type");
        return 0;
    }
    return amount;
}

void AdminPanel::on_refill100_clicked()
{
    int amount = get_amount();
}

