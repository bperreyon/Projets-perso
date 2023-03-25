#include "mainwindow.h"

#include <QVBoxLayout>
#include <QLabel>
#include <QString>
#include <QThread>

MainWindow::MainWindow(QWidget *parent): QWidget(parent)  
{
    setStyleSheet("background-color:black;"); // blue ?

    QVBoxLayout* vbox = new QVBoxLayout(this);
    vbox->setSpacing(5);

    QString title = "PacAI";
    QFont font("Courier",15,QFont::DemiBold);
    QLabel* titleLabel = new QLabel(title);
    titleLabel->setStyleSheet("QLabel {background-color:blue; color:yellow;}");
    titleLabel->setFont(font);
    titleLabel->setAlignment(Qt::AlignCenter);



    gameWidget = new GameWidget(this);


    vbox->addWidget(titleLabel);
    vbox->addWidget(gameWidget);

    setLayout(vbox);


    QObject::connect(gameWidget,&GameWidget::endGame,this,&MainWindow::onEndGame);
}

void MainWindow::onEndGame() {
    QThread::sleep(2);

    close();
}

