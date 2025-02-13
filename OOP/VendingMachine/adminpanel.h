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
    QVector<Item*> AdminWidgets;
    explicit AdminPanel(MainWindow *parent = nullptr);
    ~AdminPanel();
protected:
    void populateItems();
private slots:
    void on_Back_clicked();

    void on_updateStock_clicked();

private:
    Ui::AdminPanel *ui;
    MainWindow *mainWin;
};

#endif // ADMINPANEL_H
