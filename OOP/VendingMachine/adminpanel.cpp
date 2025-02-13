#include "adminpanel.h"
#include "ui_adminpanel.h"
#include "mainwindow.h"
AdminPanel::AdminPanel(MainWindow *parent)
    : QMainWindow(parent)
    , ui(new Ui::AdminPanel)
    , mainWin(parent)
{
    ui->setupUi(this);
    setAttribute(Qt::WA_DeleteOnClose);
}

AdminPanel::~AdminPanel()
{
    mainWin->showMainWindow();
}

void AdminPanel::on_Back_clicked()
{
    this->hide();
    mainWin->showMainWindow();
}

