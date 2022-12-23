#pragma once

#include <QMainWindow>

namespace Ui
{
    class MainWindow;
}

class MainWindow : public QMainWindow
{
public:
    MainWindow( QWidget* parent = nullptr );
    ~MainWindow();

private:
    Ui::MainWindow* mUi;
};

