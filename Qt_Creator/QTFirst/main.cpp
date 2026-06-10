#include "best_gui.h"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    Best_GUI w;
    w.show();
    return a.exec();
}
