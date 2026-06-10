#include "best_gui.h"
#include "./ui_best_gui.h"
#include <QDebug>

Best_GUI::Best_GUI(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::Best_GUI)
{
    ui->setupUi(this);
}

Best_GUI::~Best_GUI()
{
    delete ui;
}


void Best_GUI::on_Button1_clicked(bool checked)
{
    qDebug() << "Hello everyone!!!";
}

void Best_GUI::on_Button1_clicked()
{
    ui->Label_1->setText("Hello there!");
}


void Best_GUI::on_style_button_clicked()
{
    ui->Label_1->setText("Style Button");
}
