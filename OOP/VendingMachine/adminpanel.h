#ifndef ADMINPANEL_H
#define ADMINPANEL_H
#include "item.h"
#include <QMainWindow>
namespace Ui {
class AdminPanel;
}
class MainWindow;
class AdminPanel : public QMainWindow
{
    Q_OBJECT

public:
    void addItemToAdminPanel(const QString &name, int stock, int price);
    QVector<Item*> AdminWidgets;
    explicit AdminPanel(MainWindow *parent = nullptr);
    ~AdminPanel();
protected:
    int get_amount();
    void populateItems();
    void loadlogs();

private slots:
    void on_Back_clicked();

    void on_updateStock_clicked();

    void on_CollectionBtn_clicked();

    void on_ChangeBtn_clicked();

    void on_Empt_Collection_clicked();

    void on_refill100_clicked();

    void on_refill20_clicked();

    void on_refill10_clicked();

    void on_refill5_clicked();

    void on_refill1_clicked();

    void on_pushButton_clicked();

    void on_AddItemButton_clicked();

private:
    Ui::AdminPanel *ui;
    MainWindow *mainWin;
};

#endif // ADMINPANEL_H
