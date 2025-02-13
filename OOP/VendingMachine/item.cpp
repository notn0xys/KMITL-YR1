#include "item.h"

Item::Item(const QString &name, int price, int quantity, QWidget *parent)
    : QWidget(parent)
{
    this -> price = price;
    this -> name = name;
    this -> quantity = quantity;
    frame = new QFrame(this);
    frame->setFrameShape(QFrame::Box);
    frame->setLineWidth(2);
    nameLabel = new QLabel(name);
    priceLabel = new QLabel("Price: " + QString::number(price));
    if (quantity == 0) {
        quantityLabel = new QLabel("Stock: Out of Stock");
    }
    else {
        quantityLabel = new QLabel("Stock: " + QString::number(quantity));
    }

    QVBoxLayout *frameLayout = new QVBoxLayout(frame);
    frameLayout->addWidget(nameLabel);
    frameLayout->addWidget(priceLabel);
    frameLayout->addWidget(quantityLabel);

    frame->setLayout(frameLayout);
    QVBoxLayout *mainLayout = new QVBoxLayout(this);
    mainLayout->addWidget(frame);
    setLayout(mainLayout);
}

void Item::updateQuantity(int newQuantity) {
    qDebug() << "Updating quantity to:" << newQuantity;
    quantity = newQuantity;
    if (newQuantity == 0) {
        quantityLabel->setText("Stock: Out of Stock");
    }
    else {
        quantityLabel->setText("Stock: " + QString::number(newQuantity));
    }
    frame->update();
}

