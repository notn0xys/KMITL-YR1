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
        QMessageBox::warning(nullptr, "Warning", "Please only Enter Intergers");
        return;
    }
    int amount_num = amount.toInt(&ok);
    if (!ok) {
        QMessageBox::warning(nullptr, "Warning", "Please only Enter Intergers");
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
}

