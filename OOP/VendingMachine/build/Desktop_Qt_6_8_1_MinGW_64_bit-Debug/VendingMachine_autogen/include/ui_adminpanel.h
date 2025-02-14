/********************************************************************************
** Form generated from reading UI file 'adminpanel.ui'
**
** Created by: Qt User Interface Compiler version 6.8.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_ADMINPANEL_H
#define UI_ADMINPANEL_H

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

class Ui_AdminPanel
{
public:
    QWidget *centralwidget;
    QFrame *frame;
    QLabel *label;
    QPushButton *Back;
    QLabel *label_2;
    QScrollArea *LogsArea;
    QWidget *scrollAreaWidgetContents;
    QScrollArea *ItemArea;
    QWidget *scrollAreaWidgetContents_2;
    QLabel *restockText;
    QLineEdit *ID_Entry;
    QLabel *label_4;
    QLabel *label_5;
    QLineEdit *Amount_Entry;
    QPushButton *updateStock;
    QLabel *CollectionLabel;
    QLabel *ChangeLabel;
    QPushButton *CollectionBtn;
    QPushButton *ChangeBtn;
    QPushButton *pushButton_4;
    QPushButton *pushButton_5;
    QPushButton *pushButton_6;
    QPushButton *pushButton_7;
    QPushButton *pushButton_8;
    QPushButton *Empt_Collection;
    QPushButton *pushButton_10;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *AdminPanel)
    {
        if (AdminPanel->objectName().isEmpty())
            AdminPanel->setObjectName("AdminPanel");
        AdminPanel->resize(1026, 717);
        centralwidget = new QWidget(AdminPanel);
        centralwidget->setObjectName("centralwidget");
        frame = new QFrame(centralwidget);
        frame->setObjectName("frame");
        frame->setGeometry(QRect(0, 0, 1021, 691));
        frame->setFrameShape(QFrame::Shape::StyledPanel);
        frame->setFrameShadow(QFrame::Shadow::Raised);
        label = new QLabel(frame);
        label->setObjectName("label");
        label->setGeometry(QRect(20, 0, 71, 41));
        Back = new QPushButton(frame);
        Back->setObjectName("Back");
        Back->setGeometry(QRect(900, 640, 101, 31));
        label_2 = new QLabel(frame);
        label_2->setObjectName("label_2");
        label_2->setGeometry(QRect(840, 10, 49, 16));
        LogsArea = new QScrollArea(frame);
        LogsArea->setObjectName("LogsArea");
        LogsArea->setGeometry(QRect(709, 29, 301, 601));
        LogsArea->setWidgetResizable(true);
        scrollAreaWidgetContents = new QWidget();
        scrollAreaWidgetContents->setObjectName("scrollAreaWidgetContents");
        scrollAreaWidgetContents->setGeometry(QRect(0, 0, 299, 599));
        LogsArea->setWidget(scrollAreaWidgetContents);
        ItemArea = new QScrollArea(frame);
        ItemArea->setObjectName("ItemArea");
        ItemArea->setGeometry(QRect(10, 50, 181, 621));
        ItemArea->setWidgetResizable(true);
        scrollAreaWidgetContents_2 = new QWidget();
        scrollAreaWidgetContents_2->setObjectName("scrollAreaWidgetContents_2");
        scrollAreaWidgetContents_2->setGeometry(QRect(0, 0, 179, 619));
        ItemArea->setWidget(scrollAreaWidgetContents_2);
        restockText = new QLabel(frame);
        restockText->setObjectName("restockText");
        restockText->setGeometry(QRect(200, 40, 121, 41));
        ID_Entry = new QLineEdit(frame);
        ID_Entry->setObjectName("ID_Entry");
        ID_Entry->setGeometry(QRect(200, 110, 113, 24));
        label_4 = new QLabel(frame);
        label_4->setObjectName("label_4");
        label_4->setGeometry(QRect(200, 76, 81, 20));
        label_5 = new QLabel(frame);
        label_5->setObjectName("label_5");
        label_5->setGeometry(QRect(200, 150, 121, 16));
        Amount_Entry = new QLineEdit(frame);
        Amount_Entry->setObjectName("Amount_Entry");
        Amount_Entry->setGeometry(QRect(200, 180, 113, 24));
        updateStock = new QPushButton(frame);
        updateStock->setObjectName("updateStock");
        updateStock->setGeometry(QRect(200, 220, 111, 24));
        CollectionLabel = new QLabel(frame);
        CollectionLabel->setObjectName("CollectionLabel");
        CollectionLabel->setGeometry(QRect(400, 70, 101, 31));
        ChangeLabel = new QLabel(frame);
        ChangeLabel->setObjectName("ChangeLabel");
        ChangeLabel->setGeometry(QRect(540, 70, 131, 31));
        CollectionBtn = new QPushButton(frame);
        CollectionBtn->setObjectName("CollectionBtn");
        CollectionBtn->setGeometry(QRect(400, 110, 91, 31));
        ChangeBtn = new QPushButton(frame);
        ChangeBtn->setObjectName("ChangeBtn");
        ChangeBtn->setGeometry(QRect(540, 110, 91, 31));
        pushButton_4 = new QPushButton(frame);
        pushButton_4->setObjectName("pushButton_4");
        pushButton_4->setGeometry(QRect(220, 390, 80, 24));
        pushButton_5 = new QPushButton(frame);
        pushButton_5->setObjectName("pushButton_5");
        pushButton_5->setGeometry(QRect(220, 430, 80, 24));
        pushButton_6 = new QPushButton(frame);
        pushButton_6->setObjectName("pushButton_6");
        pushButton_6->setGeometry(QRect(220, 500, 80, 24));
        pushButton_7 = new QPushButton(frame);
        pushButton_7->setObjectName("pushButton_7");
        pushButton_7->setGeometry(QRect(210, 540, 80, 24));
        pushButton_8 = new QPushButton(frame);
        pushButton_8->setObjectName("pushButton_8");
        pushButton_8->setGeometry(QRect(230, 460, 80, 24));
        Empt_Collection = new QPushButton(frame);
        Empt_Collection->setObjectName("Empt_Collection");
        Empt_Collection->setGeometry(QRect(500, 580, 191, 51));
        pushButton_10 = new QPushButton(frame);
        pushButton_10->setObjectName("pushButton_10");
        pushButton_10->setGeometry(QRect(300, 580, 191, 51));
        AdminPanel->setCentralWidget(centralwidget);
        statusbar = new QStatusBar(AdminPanel);
        statusbar->setObjectName("statusbar");
        AdminPanel->setStatusBar(statusbar);

        retranslateUi(AdminPanel);

        QMetaObject::connectSlotsByName(AdminPanel);
    } // setupUi

    void retranslateUi(QMainWindow *AdminPanel)
    {
        AdminPanel->setWindowTitle(QCoreApplication::translate("AdminPanel", "MainWindow", nullptr));
        label->setText(QCoreApplication::translate("AdminPanel", "Admin Panel", nullptr));
        Back->setText(QCoreApplication::translate("AdminPanel", "Back", nullptr));
        label_2->setText(QCoreApplication::translate("AdminPanel", "Logs", nullptr));
        restockText->setText(QCoreApplication::translate("AdminPanel", "Restock Iems: ", nullptr));
        label_4->setText(QCoreApplication::translate("AdminPanel", "Enter ID: ", nullptr));
        label_5->setText(QCoreApplication::translate("AdminPanel", "Enter Amount of stock", nullptr));
        updateStock->setText(QCoreApplication::translate("AdminPanel", "Update", nullptr));
        CollectionLabel->setText(QCoreApplication::translate("AdminPanel", "Amount", nullptr));
        ChangeLabel->setText(QCoreApplication::translate("AdminPanel", "Amount: ", nullptr));
        CollectionBtn->setText(QCoreApplication::translate("AdminPanel", "Check Money", nullptr));
        ChangeBtn->setText(QCoreApplication::translate("AdminPanel", "Check Change", nullptr));
        pushButton_4->setText(QCoreApplication::translate("AdminPanel", "PushButton", nullptr));
        pushButton_5->setText(QCoreApplication::translate("AdminPanel", "PushButton", nullptr));
        pushButton_6->setText(QCoreApplication::translate("AdminPanel", "PushButton", nullptr));
        pushButton_7->setText(QCoreApplication::translate("AdminPanel", "PushButton", nullptr));
        pushButton_8->setText(QCoreApplication::translate("AdminPanel", "PushButton", nullptr));
        Empt_Collection->setText(QCoreApplication::translate("AdminPanel", "Empty Collection Box", nullptr));
        pushButton_10->setText(QCoreApplication::translate("AdminPanel", "Refill Change  Box", nullptr));
    } // retranslateUi

};

namespace Ui {
    class AdminPanel: public Ui_AdminPanel {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_ADMINPANEL_H
