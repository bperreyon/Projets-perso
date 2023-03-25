#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QWidget>
#include "gamewidget.h"

class MainWindow : public QWidget
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);

public slots:
    /// Terminates the app, for now ...
    void onEndGame();

private:
    GameWidget* gameWidget;




};
#endif // MAINWINDOW_H
