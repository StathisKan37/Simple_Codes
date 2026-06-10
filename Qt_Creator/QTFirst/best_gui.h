#ifndef BEST_GUI_H
#define BEST_GUI_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class Best_GUI; }
QT_END_NAMESPACE

class Best_GUI : public QMainWindow
{
    Q_OBJECT

public:
    Best_GUI(QWidget *parent = nullptr);
    ~Best_GUI();

private slots:
    void on_Button1_clicked(bool checked);

    void on_Button1_clicked();

    void on_style_button_clicked();

private:
    Ui::Best_GUI *ui;
};
#endif // BEST_GUI_H
