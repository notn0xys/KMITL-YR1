#ifndef LOGS_H
#define LOGS_H


#include <QWidget>
#include <QLabel>
#include <QPushButton>
#include <QVBoxLayout>
#include <QFrame>

class Logs : public QWidget
{
    Q_OBJECT

public:
    void updateQuantity(int newQuantity);
    explicit Logs(const QString &action,const QString &doneby,QWidget *parent = nullptr);
    QString action;
    QString doneby;


private:
    QFrame *frame;
    QLabel *actionLabel;
    QLabel *donebyLabel;
};

#endif // LOGS_H
