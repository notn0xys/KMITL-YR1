/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 6.8.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QFrame>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QScrollArea>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QScrollArea *ItemDisplay;
    QWidget *scrollAreaWidgetContents;
    QFrame *Sidebar;
    QFrame *Upper;
    QLabel *State;
    QLabel *Pay;
    QLabel *Amount;
    QPushButton *btn1;
    QPushButton *btn2;
    QPushButton *btn3;
    QPushButton *btn4;
    QPushButton *btn5;
    QPushButton *btn6;
    QPushButton *btn7;
    QPushButton *btn8;
    QPushButton *btn9;
    QPushButton *Delete;
    QPushButton *btn0;
    QPushButton *Enter;
    QLineEdit *Id_display;
    QPushButton *Buy;
    QPushButton *AdminToggle;
    QFrame *frame_2;
    QPushButton *add100;
    QPushButton *add20;
    QPushButton *add10;
    QPushButton *add5;
    QPushButton *add1;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName("MainWindow");
        MainWindow->resize(1110, 676);
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName("centralwidget");
        ItemDisplay = new QScrollArea(centralwidget);
        ItemDisplay->setObjectName("ItemDisplay");
        ItemDisplay->setGeometry(QRect(30, 20, 761, 551));
        ItemDisplay->setWidgetResizable(true);
        scrollAreaWidgetContents = new QWidget();
        scrollAreaWidgetContents->setObjectName("scrollAreaWidgetContents");
        scrollAreaWidgetContents->setGeometry(QRect(0, 0, 759, 549));
        ItemDisplay->setWidget(scrollAreaWidgetContents);
        Sidebar = new QFrame(centralwidget);
        Sidebar->setObjectName("Sidebar");
        Sidebar->setGeometry(QRect(800, 20, 281, 551));
        Sidebar->setFrameShape(QFrame::Shape::StyledPanel);
        Sidebar->setFrameShadow(QFrame::Shadow::Raised);
        Upper = new QFrame(Sidebar);
        Upper->setObjectName("Upper");
        Upper->setGeometry(QRect(40, 20, 211, 141));
        Upper->setFrameShape(QFrame::Shape::StyledPanel);
        Upper->setFrameShadow(QFrame::Shadow::Raised);
        State = new QLabel(Upper);
        State->setObjectName("State");
        State->setGeometry(QRect(20, 10, 141, 21));
        Pay = new QLabel(Upper);
        Pay->setObjectName("Pay");
        Pay->setGeometry(QRect(20, 50, 161, 16));
        Amount = new QLabel(Upper);
        Amount->setObjectName("Amount");
        Amount->setGeometry(QRect(20, 80, 161, 21));
        btn1 = new QPushButton(Sidebar);
        btn1->setObjectName("btn1");
        btn1->setGeometry(QRect(60, 260, 51, 31));
        btn2 = new QPushButton(Sidebar);
        btn2->setObjectName("btn2");
        btn2->setGeometry(QRect(120, 260, 51, 31));
        btn3 = new QPushButton(Sidebar);
        btn3->setObjectName("btn3");
        btn3->setGeometry(QRect(180, 260, 51, 31));
        btn4 = new QPushButton(Sidebar);
        btn4->setObjectName("btn4");
        btn4->setGeometry(QRect(60, 300, 51, 31));
        btn5 = new QPushButton(Sidebar);
        btn5->setObjectName("btn5");
        btn5->setGeometry(QRect(120, 300, 51, 31));
        btn6 = new QPushButton(Sidebar);
        btn6->setObjectName("btn6");
        btn6->setGeometry(QRect(180, 300, 51, 31));
        btn7 = new QPushButton(Sidebar);
        btn7->setObjectName("btn7");
        btn7->setGeometry(QRect(60, 340, 51, 31));
        btn8 = new QPushButton(Sidebar);
        btn8->setObjectName("btn8");
        btn8->setGeometry(QRect(120, 340, 51, 31));
        btn9 = new QPushButton(Sidebar);
        btn9->setObjectName("btn9");
        btn9->setGeometry(QRect(180, 340, 51, 31));
        Delete = new QPushButton(Sidebar);
        Delete->setObjectName("Delete");
        Delete->setGeometry(QRect(60, 380, 51, 31));
        btn0 = new QPushButton(Sidebar);
        btn0->setObjectName("btn0");
        btn0->setGeometry(QRect(120, 380, 51, 31));
        Enter = new QPushButton(Sidebar);
        Enter->setObjectName("Enter");
        Enter->setGeometry(QRect(180, 380, 51, 31));
        Id_display = new QLineEdit(Sidebar);
        Id_display->setObjectName("Id_display");
        Id_display->setGeometry(QRect(60, 210, 171, 31));
        Id_display->setReadOnly(true);
        Buy = new QPushButton(Sidebar);
        Buy->setObjectName("Buy");
        Buy->setGeometry(QRect(60, 420, 171, 31));
        AdminToggle = new QPushButton(centralwidget);
        AdminToggle->setObjectName("AdminToggle");
        AdminToggle->setGeometry(QRect(1000, 580, 81, 61));
        frame_2 = new QFrame(centralwidget);
        frame_2->setObjectName("frame_2");
        frame_2->setGeometry(QRect(50, 580, 931, 61));
        frame_2->setFrameShape(QFrame::Shape::StyledPanel);
        frame_2->setFrameShadow(QFrame::Shadow::Raised);
        add100 = new QPushButton(frame_2);
        add100->setObjectName("add100");
        add100->setGeometry(QRect(40, 10, 91, 31));
        add20 = new QPushButton(frame_2);
        add20->setObjectName("add20");
        add20->setGeometry(QRect(190, 10, 91, 31));
        add10 = new QPushButton(frame_2);
        add10->setObjectName("add10");
        add10->setGeometry(QRect(340, 10, 91, 31));
        add5 = new QPushButton(frame_2);
        add5->setObjectName("add5");
        add5->setGeometry(QRect(500, 10, 91, 31));
        add1 = new QPushButton(frame_2);
        add1->setObjectName("add1");
        add1->setGeometry(QRect(670, 10, 91, 31));
        MainWindow->setCentralWidget(centralwidget);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName("statusbar");
        MainWindow->setStatusBar(statusbar);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "MainWindow", nullptr));
        State->setText(QCoreApplication::translate("MainWindow", "task", nullptr));
        Pay->setText(QCoreApplication::translate("MainWindow", "Remaining:  ", nullptr));
        Amount->setText(QCoreApplication::translate("MainWindow", "Amount Inserted", nullptr));
        btn1->setText(QCoreApplication::translate("MainWindow", "1", nullptr));
        btn2->setText(QCoreApplication::translate("MainWindow", "2", nullptr));
        btn3->setText(QCoreApplication::translate("MainWindow", "3", nullptr));
        btn4->setText(QCoreApplication::translate("MainWindow", "4", nullptr));
        btn5->setText(QCoreApplication::translate("MainWindow", "5", nullptr));
        btn6->setText(QCoreApplication::translate("MainWindow", "6", nullptr));
        btn7->setText(QCoreApplication::translate("MainWindow", "7", nullptr));
        btn8->setText(QCoreApplication::translate("MainWindow", "8", nullptr));
        btn9->setText(QCoreApplication::translate("MainWindow", "9", nullptr));
        Delete->setText(QCoreApplication::translate("MainWindow", "del", nullptr));
        btn0->setText(QCoreApplication::translate("MainWindow", "0", nullptr));
        Enter->setText(QCoreApplication::translate("MainWindow", "Enter", nullptr));
        Buy->setText(QCoreApplication::translate("MainWindow", "Buy", nullptr));
        AdminToggle->setText(QCoreApplication::translate("MainWindow", "Admin Mode", nullptr));
        add100->setText(QCoreApplication::translate("MainWindow", "100", nullptr));
        add20->setText(QCoreApplication::translate("MainWindow", "20", nullptr));
        add10->setText(QCoreApplication::translate("MainWindow", "10", nullptr));
        add5->setText(QCoreApplication::translate("MainWindow", "5", nullptr));
        add1->setText(QCoreApplication::translate("MainWindow", "1", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
