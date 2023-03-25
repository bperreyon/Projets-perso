#include "mainwindow.h"


#include <QApplication>


int main(int argc, char *argv[])
{


    QApplication a(argc, argv);

    QSize screenGeometry = a.screens()[0]->size();

    MainWindow w;
    w.setWindowTitle("PacAI");

    int height = screenGeometry.height();
    int width = screenGeometry.width();
    int x=(width - w.width()) / 2.0;
    int y=(height - w.height()) / 6.0;
    w.setGeometry(x,y,w.width(),w.height());

    w.show();
    return a.exec();





    return 0;
}
