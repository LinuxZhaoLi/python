#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QDebug>
MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    uint32_t i_t = 0xFFFFFFFE;
    qDebug()<<"i_t"<<i_t;
}

MainWindow::~MainWindow()
{
    delete ui;
}
