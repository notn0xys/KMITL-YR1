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
    QPushButton *CollectionBtn;
    QPushButton *refill100;
    QPushButton *refill20;
    QPushButton *refill5;
    QPushButton *refill1;
    QPushButton *refill10;
    QPushButton *Empt_Collection;
    QFrame *frame_2;
    QPushButton *ChangeBtn;
    QLabel *label_3;
    QLabel *label_6;
    QLabel *label_7;
    QLabel *label_8;
    QLabel *label_9;
    QLabel *label_10;
    QLabel *label_11;
    QLabel *label_12;
    QLabel *label_13;
    QLabel *label_14;
    QLabel *label_15;
    QLineEdit *changeEntry;
    QLabel *label_16;
    QLabel *label_17;
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
        label_5->setGeometry(QRect(200, 150, 221, 16));
        Amount_Entry = new QLineEdit(frame);
        Amount_Entry->setObjectName("Amount_Entry");
        Amount_Entry->setGeometry(QRect(200, 180, 113, 24));
        updateStock = new QPushButton(frame);
        updateStock->setObjectName("updateStock");
        updateStock->setGeometry(QRect(200, 220, 111, 24));
        CollectionLabel = new QLabel(frame);
        CollectionLabel->setObjectName("CollectionLabel");
        CollectionLabel->setGeometry(QRect(480, 70, 101, 31));
        CollectionBtn = new QPushButton(frame);
        CollectionBtn->setObjectName("CollectionBtn");
        CollectionBtn->setGeometry(QRect(590, 70, 91, 31));
        refill100 = new QPushButton(frame);
        refill100->setObjectName("refill100");
        refill100->setGeometry(QRect(200, 400, 111, 24));
        refill20 = new QPushButton(frame);
        refill20->setObjectName("refill20");
        refill20->setGeometry(QRect(200, 440, 111, 24));
        refill5 = new QPushButton(frame);
        refill5->setObjectName("refill5");
        refill5->setGeometry(QRect(200, 520, 111, 24));
        refill1 = new QPushButton(frame);
        refill1->setObjectName("refill1");
        refill1->setGeometry(QRect(200, 560, 111, 24));
        refill10 = new QPushButton(frame);
        refill10->setObjectName("refill10");
        refill10->setGeometry(QRect(200, 480, 111, 24));
        Empt_Collection = new QPushButton(frame);
        Empt_Collection->setObjectName("Empt_Collection");
        Empt_Collection->setGeometry(QRect(510, 640, 181, 31));
        frame_2 = new QFrame(frame);
        frame_2->setObjectName("frame_2");
        frame_2->setGeometry(QRect(370, 110, 311, 281));
        frame_2->setFrameShape(QFrame::Shape::StyledPanel);
        frame_2->setFrameShadow(QFrame::Shadow::Raised);
        ChangeBtn = new QPushButton(frame_2);
        ChangeBtn->setObjectName("ChangeBtn");
        ChangeBtn->setGeometry(QRect(210, 240, 91, 31));
        label_3 = new QLabel(frame_2);
        label_3->setObjectName("label_3");
        label_3->setGeometry(QRect(30, 40, 71, 51));
        label_6 = new QLabel(frame_2);
        label_6->setObjectName("label_6");
        label_6->setGeometry(QRect(30, 90, 91, 31));
        label_7 = new QLabel(frame_2);
        label_7->setObjectName("label_7");
        label_7->setGeometry(QRect(30, 130, 91, 41));
        label_8 = new QLabel(frame_2);
        label_8->setObjectName("label_8");
        label_8->setGeometry(QRect(30, 180, 63, 20));
        label_9 = new QLabel(frame_2);
        label_9->setObjectName("label_9");
        label_9->setGeometry(QRect(30, 220, 63, 20));
        label_10 = new QLabel(frame_2);
        label_10->setObjectName("label_10");
        label_10->setGeometry(QRect(80, 0, 171, 41));
        label_11 = new QLabel(frame_2);
        label_11->setObjectName("label_11");
        label_11->setGeometry(QRect(90, 60, 63, 20));
        label_12 = new QLabel(frame_2);
        label_12->setObjectName("label_12");
        label_12->setGeometry(QRect(90, 100, 63, 20));
        label_13 = new QLabel(frame_2);
        label_13->setObjectName("label_13");
        label_13->setGeometry(QRect(90, 140, 63, 20));
        label_14 = new QLabel(frame_2);
        label_14->setObjectName("label_14");
        label_14->setGeometry(QRect(90, 180, 63, 20));
        label_15 = new QLabel(frame_2);
        label_15->setObjectName("label_15");
        label_15->setGeometry(QRect(90, 220, 63, 20));
        changeEntry = new QLineEdit(frame);
        changeEntry->setObjectName("changeEntry");
        changeEntry->setGeometry(QRect(200, 350, 111, 28));
        label_16 = new QLabel(frame);
        label_16->setObjectName("label_16");
        label_16->setGeometry(QRect(200, 310, 111, 20));
        label_17 = new QLabel(frame);
        label_17->setObjectName("label_17");
        label_17->setGeometry(QRect(200, 270, 121, 20));
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
        CollectionBtn->setText(QCoreApplication::translate("AdminPanel", "Check Money", nullptr));
        refill100->setText(QCoreApplication::translate("AdminPanel", "Refill: 100", nullptr));
        refill20->setText(QCoreApplication::translate("AdminPanel", "Refill 20", nullptr));
        refill5->setText(QCoreApplication::translate("AdminPanel", "Refill 5", nullptr));
        refill1->setText(QCoreApplication::translate("AdminPanel", "Refill 1", nullptr));
        refill10->setText(QCoreApplication::translate("AdminPanel", "Refill 10", nullptr));
        Empt_Collection->setText(QCoreApplication::translate("AdminPanel", "Empty Collection Box", nullptr));
        ChangeBtn->setText(QCoreApplication::translate("AdminPanel", "Check Change", nullptr));
        label_3->setText(QCoreApplication::translate("AdminPanel", "$100 :", nullptr));
        label_6->setText(QCoreApplication::translate("AdminPanel", "$20 : ", nullptr));
        label_7->setText(QCoreApplication::translate("AdminPanel", "$10 :", nullptr));
        label_8->setText(QCoreApplication::translate("AdminPanel", "$5 :", nullptr));
        label_9->setText(QCoreApplication::translate("AdminPanel", "$1 :", nullptr));
        label_10->setText(QCoreApplication::translate("AdminPanel", "Change Remaining", nullptr));
        label_11->setText(QCoreApplication::translate("AdminPanel", "TextLabel", nullptr));
        label_12->setText(QCoreApplication::translate("AdminPanel", "TextLabel", nullptr));
        label_13->setText(QCoreApplication::translate("AdminPanel", "TextLabel", nullptr));
        label_14->setText(QCoreApplication::translate("AdminPanel", "TextLabel", nullptr));
        label_15->setText(QCoreApplication::translate("AdminPanel", "TextLabel", nullptr));
        label_16->setText(QCoreApplication::translate("AdminPanel", "Enter Amount", nullptr));
        label_17->setText(QCoreApplication::translate("AdminPanel", "Restock Change", nullptr));
    } // retranslateUi

};

namespace Ui {
    class AdminPanel: public Ui_AdminPanel {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_ADMINPANEL_H
