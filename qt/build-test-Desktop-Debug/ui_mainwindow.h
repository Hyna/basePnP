/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.4.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QDial>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QRadioButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QTreeWidget>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralWidget;
    QPushButton *btnLoadTst;
    QGroupBox *groupBox;
    QRadioButton *radioOrigin;
    QRadioButton *radioGeometric;
    QPushButton *btnLoadPlacement;
    QPushButton *btnLoadCCD;
    QFrame *line;
    QLabel *label_2;
    QTreeWidget *treeWidget;
    QTreeWidget *treePackages;
    QLabel *label_3;
    QComboBox *comboBox;
    QDial *dial;
    QLabel *lblAbout;
    QLabel *label;
    QLabel *lblStatus;
    QLabel *label_4;
    QPushButton *btnAlign;
    QLabel *imgCCD;
    QWidget *layoutWidget;
    QVBoxLayout *verticalLayout;
    QLabel *lblO1;
    QLabel *lblO2;
    QLabel *lblO3;
    QWidget *layoutWidget1;
    QVBoxLayout *verticalLayout_2;
    QLabel *lblP1;
    QLabel *lblP2;
    QLabel *lblP3;
    QLabel *imgCCD2;
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(1341, 939);
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        btnLoadTst = new QPushButton(centralWidget);
        btnLoadTst->setObjectName(QStringLiteral("btnLoadTst"));
        btnLoadTst->setGeometry(QRect(20, 50, 171, 31));
        groupBox = new QGroupBox(centralWidget);
        groupBox->setObjectName(QStringLiteral("groupBox"));
        groupBox->setGeometry(QRect(230, 10, 211, 111));
        radioOrigin = new QRadioButton(groupBox);
        radioOrigin->setObjectName(QStringLiteral("radioOrigin"));
        radioOrigin->setGeometry(QRect(10, 30, 110, 41));
        radioOrigin->setChecked(true);
        radioGeometric = new QRadioButton(groupBox);
        radioGeometric->setObjectName(QStringLiteral("radioGeometric"));
        radioGeometric->setGeometry(QRect(10, 70, 181, 26));
        btnLoadPlacement = new QPushButton(centralWidget);
        btnLoadPlacement->setObjectName(QStringLiteral("btnLoadPlacement"));
        btnLoadPlacement->setGeometry(QRect(20, 10, 171, 31));
        btnLoadCCD = new QPushButton(centralWidget);
        btnLoadCCD->setObjectName(QStringLiteral("btnLoadCCD"));
        btnLoadCCD->setGeometry(QRect(20, 90, 171, 31));
        line = new QFrame(centralWidget);
        line->setObjectName(QStringLiteral("line"));
        line->setGeometry(QRect(10, 130, 1071, 16));
        line->setFrameShape(QFrame::HLine);
        line->setFrameShadow(QFrame::Sunken);
        label_2 = new QLabel(centralWidget);
        label_2->setObjectName(QStringLiteral("label_2"));
        label_2->setGeometry(QRect(20, 140, 181, 21));
        treeWidget = new QTreeWidget(centralWidget);
        treeWidget->setObjectName(QStringLiteral("treeWidget"));
        treeWidget->setGeometry(QRect(20, 160, 441, 241));
        treeWidget->setAlternatingRowColors(true);
        treeWidget->setColumnCount(8);
        treeWidget->header()->setHighlightSections(false);
        treePackages = new QTreeWidget(centralWidget);
        QTreeWidgetItem *__qtreewidgetitem = new QTreeWidgetItem();
        __qtreewidgetitem->setText(0, QStringLiteral("1"));
        treePackages->setHeaderItem(__qtreewidgetitem);
        treePackages->setObjectName(QStringLiteral("treePackages"));
        treePackages->setGeometry(QRect(510, 160, 441, 241));
        treePackages->setAlternatingRowColors(true);
        label_3 = new QLabel(centralWidget);
        label_3->setObjectName(QStringLiteral("label_3"));
        label_3->setGeometry(QRect(510, 140, 181, 21));
        comboBox = new QComboBox(centralWidget);
        comboBox->setObjectName(QStringLiteral("comboBox"));
        comboBox->setGeometry(QRect(970, 240, 83, 29));
        dial = new QDial(centralWidget);
        dial->setObjectName(QStringLiteral("dial"));
        dial->setGeometry(QRect(980, 180, 50, 64));
        lblAbout = new QLabel(centralWidget);
        lblAbout->setObjectName(QStringLiteral("lblAbout"));
        lblAbout->setGeometry(QRect(830, 20, 181, 31));
        label = new QLabel(centralWidget);
        label->setObjectName(QStringLiteral("label"));
        label->setGeometry(QRect(20, 420, 201, 21));
        lblStatus = new QLabel(centralWidget);
        lblStatus->setObjectName(QStringLiteral("lblStatus"));
        lblStatus->setGeometry(QRect(810, 100, 441, 21));
        label_4 = new QLabel(centralWidget);
        label_4->setObjectName(QStringLiteral("label_4"));
        label_4->setGeometry(QRect(750, 100, 51, 21));
        btnAlign = new QPushButton(centralWidget);
        btnAlign->setObjectName(QStringLiteral("btnAlign"));
        btnAlign->setGeometry(QRect(530, 10, 111, 31));
        imgCCD = new QLabel(centralWidget);
        imgCCD->setObjectName(QStringLiteral("imgCCD"));
        imgCCD->setGeometry(QRect(20, 450, 600, 358));
        QSizePolicy sizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(imgCCD->sizePolicy().hasHeightForWidth());
        imgCCD->setSizePolicy(sizePolicy);
        imgCCD->setFrameShape(QFrame::Box);
        layoutWidget = new QWidget(centralWidget);
        layoutWidget->setObjectName(QStringLiteral("layoutWidget"));
        layoutWidget->setGeometry(QRect(490, 50, 131, 77));
        verticalLayout = new QVBoxLayout(layoutWidget);
        verticalLayout->setSpacing(6);
        verticalLayout->setContentsMargins(11, 11, 11, 11);
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        verticalLayout->setContentsMargins(0, 0, 0, 0);
        lblO1 = new QLabel(layoutWidget);
        lblO1->setObjectName(QStringLiteral("lblO1"));

        verticalLayout->addWidget(lblO1);

        lblO2 = new QLabel(layoutWidget);
        lblO2->setObjectName(QStringLiteral("lblO2"));

        verticalLayout->addWidget(lblO2);

        lblO3 = new QLabel(layoutWidget);
        lblO3->setObjectName(QStringLiteral("lblO3"));

        verticalLayout->addWidget(lblO3);

        layoutWidget1 = new QWidget(centralWidget);
        layoutWidget1->setObjectName(QStringLiteral("layoutWidget1"));
        layoutWidget1->setGeometry(QRect(620, 50, 121, 77));
        verticalLayout_2 = new QVBoxLayout(layoutWidget1);
        verticalLayout_2->setSpacing(6);
        verticalLayout_2->setContentsMargins(11, 11, 11, 11);
        verticalLayout_2->setObjectName(QStringLiteral("verticalLayout_2"));
        verticalLayout_2->setContentsMargins(0, 0, 0, 0);
        lblP1 = new QLabel(layoutWidget1);
        lblP1->setObjectName(QStringLiteral("lblP1"));

        verticalLayout_2->addWidget(lblP1);

        lblP2 = new QLabel(layoutWidget1);
        lblP2->setObjectName(QStringLiteral("lblP2"));

        verticalLayout_2->addWidget(lblP2);

        lblP3 = new QLabel(layoutWidget1);
        lblP3->setObjectName(QStringLiteral("lblP3"));

        verticalLayout_2->addWidget(lblP3);

        imgCCD2 = new QLabel(centralWidget);
        imgCCD2->setObjectName(QStringLiteral("imgCCD2"));
        imgCCD2->setGeometry(QRect(640, 410, 640, 480));
        imgCCD2->setFrameShape(QFrame::Box);
        MainWindow->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 1341, 27));
        MainWindow->setMenuBar(menuBar);
        mainToolBar = new QToolBar(MainWindow);
        mainToolBar->setObjectName(QStringLiteral("mainToolBar"));
        MainWindow->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        MainWindow->setStatusBar(statusBar);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "PnP test application", 0));
        btnLoadTst->setText(QApplication::translate("MainWindow", "Load board image", 0));
        groupBox->setTitle(QApplication::translate("MainWindow", "Origins vs geomtertic center", 0));
        radioOrigin->setText(QApplication::translate("MainWindow", "Origins", 0));
        radioGeometric->setText(QApplication::translate("MainWindow", "Pads geometric center", 0));
        btnLoadPlacement->setText(QApplication::translate("MainWindow", "Load PnP Eagle data", 0));
        btnLoadCCD->setText(QApplication::translate("MainWindow", "Take a CCD image", 0));
        label_2->setText(QApplication::translate("MainWindow", "Eagle placement data", 0));
        QTreeWidgetItem *___qtreewidgetitem = treeWidget->headerItem();
        ___qtreewidgetitem->setText(7, QApplication::translate("MainWindow", "8", 0));
        ___qtreewidgetitem->setText(6, QApplication::translate("MainWindow", "7", 0));
        ___qtreewidgetitem->setText(5, QApplication::translate("MainWindow", "6", 0));
        ___qtreewidgetitem->setText(4, QApplication::translate("MainWindow", "5", 0));
        ___qtreewidgetitem->setText(3, QApplication::translate("MainWindow", "4", 0));
        ___qtreewidgetitem->setText(2, QApplication::translate("MainWindow", "3", 0));
        ___qtreewidgetitem->setText(1, QApplication::translate("MainWindow", "2", 0));
        ___qtreewidgetitem->setText(0, QApplication::translate("MainWindow", "1", 0));
        label_3->setText(QApplication::translate("MainWindow", "Items for placement", 0));
        comboBox->clear();
        comboBox->insertItems(0, QStringList()
         << QApplication::translate("MainWindow", "tray 1", 0)
         << QApplication::translate("MainWindow", "tray 2", 0)
         << QApplication::translate("MainWindow", "tray 3", 0)
        );
        lblAbout->setText(QApplication::translate("MainWindow", "PnP SW by Hynek Stetina\n"
"VUTBR", 0));
        label->setText(QApplication::translate("MainWindow", "Placement simulator", 0));
        lblStatus->setText(QApplication::translate("MainWindow", "Board is not aligned!", 0));
        label_4->setText(QApplication::translate("MainWindow", "Status:", 0));
        btnAlign->setText(QApplication::translate("MainWindow", "Align procedure", 0));
        imgCCD->setText(QApplication::translate("MainWindow", "Simulation image", 0));
        lblO1->setText(QApplication::translate("MainWindow", "TextLabel", 0));
        lblO2->setText(QApplication::translate("MainWindow", "TextLabel", 0));
        lblO3->setText(QApplication::translate("MainWindow", "TextLabel", 0));
        lblP1->setText(QApplication::translate("MainWindow", "TextLabel", 0));
        lblP2->setText(QApplication::translate("MainWindow", "TextLabel", 0));
        lblP3->setText(QApplication::translate("MainWindow", "TextLabel", 0));
        imgCCD2->setText(QApplication::translate("MainWindow", "Real CCD image", 0));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
