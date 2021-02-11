#include <QApplication>
#include <QMainWindow>

#include <kddockwidgets/DockWidget.h>
#include <kddockwidgets/MainWindow.h>

int main(int argc, char **argv)
{
    /* Initalize Qt Application. */
    QApplication app(argc, argv);

    KDDockWidgets::MainWindow window("myWindow");
    app.setActiveWindow(&window);

    window.show();

    return app.exec();
}
