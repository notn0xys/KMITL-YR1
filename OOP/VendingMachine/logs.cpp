#include "logs.h"

Logs::Logs(const QString &action, const QString &doneby, QWidget *parent)
    : QWidget(parent)
{
    this -> action = action;
    this -> doneby = doneby;
    frame = new QFrame(this);
    frame->setFrameShape(QFrame::Box);
    frame->setLineWidth(2);
    actionLabel = new QLabel(action);
    donebyLabel = new QLabel("Done by: "+ doneby);

    QVBoxLayout *frameLayout = new QVBoxLayout(frame);
    frameLayout->addWidget(actionLabel);
    frameLayout->addWidget(donebyLabel);

    frame->setLayout(frameLayout);
    QVBoxLayout *mainLayout = new QVBoxLayout(this);
    mainLayout->addWidget(frame);
    setLayout(mainLayout);
}
