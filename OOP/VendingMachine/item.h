#ifndef ITEM_H
#define ITEM_H

#include <QWidget>
#include <QLabel>
#include <QPushButton>
#include <QVBoxLayout>
#include <QFrame>

class Item : public QWidget
{
    Q_OBJECT

public:
    void updateQuantity(int newQuantity);
    explicit Item(const QString &name, int price, int quantity, QWidget *parent = nullptr);
    QString name;
    int price;
    int quantity;

private:
    QFrame *frame;
    QLabel *nameLabel;
    QLabel *priceLabel;
    QLabel *quantityLabel;
};

#endif // ITEMWIDGET_H
