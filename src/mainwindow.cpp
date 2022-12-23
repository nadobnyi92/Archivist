#include <src/mainwindow.h>

#include <ui_mainwindow.h>

MainWindow::MainWindow( QWidget* parent )
    : QMainWindow( parent )
    , mUi( new Ui::MainWindow )
{
    mUi->setupUi( this );
}

MainWindow::~MainWindow()
{
    delete mUi;
}

