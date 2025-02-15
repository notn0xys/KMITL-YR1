#ifndef MAINWINDOW_H
#define MAINWINDOW_H
#include <QMainWindow>
#include <QSqlDatabase>
#include <QSqlQuery>
#include <QSqlError>
#include <QDebug>
#include "adminpanel.h"
#include "item.h"
#include <QVector>

QT_BEGIN_NAMESPACE
namespace Ui {
class MainWindow;
}
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    void addlogs(QString action, QString doneby);
    QSqlDatabase& getDatabase();
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();
    void showMainWindow();
    void buyItem(int index);
    QVector<Item*> itemWidgets;
    void insertMoney(int amount);


private slots:
    void on_AdminToggle_clicked();

    void on_btn1_clicked();

    void on_btn0_clicked();

    void on_btn2_clicked();

    void on_btn3_clicked();

    void on_btn4_clicked();

    void on_btn5_clicked();

    void on_btn6_clicked();

    void on_btn7_clicked();

    void on_btn8_clicked();

    void on_btn9_clicked();

    void on_Delete_clicked();

    void on_Enter_clicked();

    void on_Buy_clicked();

    void on_add100_clicked();

    void on_add20_clicked();

    void on_add10_clicked();

    void on_add5_clicked();

    void on_add1_clicked();
protected:
    void checkStockAndDisableMachine();
    void disableMachine();
    void enableMachine();
    void calculateChangeAndUpdateDatabase();
private:
    QString DisplaySelected = "";
    int Selected_id;
    int Return_amount;
    int insertedMoney = 0;
    int Amount_due;
    void additems();
    QSqlDatabase db;
    void setupDatabase();
    Ui::MainWindow *ui;
    AdminPanel *adminPanel = nullptr;
};
#endif // MAINWINDOW_H
