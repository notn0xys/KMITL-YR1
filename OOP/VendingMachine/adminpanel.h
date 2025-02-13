#ifndef ADMINPANEL_H
#define ADMINPANEL_H

#include <QMainWindow>
namespace Ui {
class AdminPanel;
}
class MainWindow;
class AdminPanel : public QMainWindow
{
    Q_OBJECT

public:
    explicit AdminPanel(MainWindow *parent = nullptr);
    ~AdminPanel();

private slots:
    void on_Back_clicked();

private:
    Ui::AdminPanel *ui;
    MainWindow *mainWin;
};

#endif // ADMINPANEL_H
