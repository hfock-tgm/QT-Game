import sys
from time import time
from random import shuffle
from PySide.QtCore import Qt
from PySide.QtGui import *
from at.fock.MVC.View import View
from at.fock.MVC.Model import Model

class Controller(QMainWindow):
    '''
    Konstruktor fuer Controller
    '''
    def __init__(self, parent=None):
        super().__init__(parent)
        self.view = View()
        self.view.setupUi(self)
        self.timeDiff = None
        self.timeStart = None
        self.timeEnd = None

        self.buttonList = [
            self.view.pushButton_3,self.view.pushButton_4,self.view.pushButton_5,self.view.pushButton_6,self.view.pushButton_7,
            self.view.pushButton_8,self.view.pushButton_9,self.view.pushButton_10,self.view.pushButton_11,
            self.view.pushButton_12,self.view.pushButton_13,self.view.pushButton_14,self.view.pushButton_15,self.view.pushButton_16,self.view.pushButton_17,
            self.view.pushButton_18,self.view.pushButton_19,self.view.pushButton_20,self.view.pushButton_21,self.view.pushButton_22,self.view.pushButton_23,
            self.view.pushButton_24,self.view.pushButton_25
        ]
        self.model = Model(len(self.buttonList))

        # start ein neues Spiel
        self.neuStart()

        # Damit die Buttons auch etwas machen
        self.connectButtons()

    '''
    Startet ein neues Spiel
    '''
    def neuStart(self):
        self.model.spiele += 1
        self.updateLabels()

        self.activateAllButtons()
        self.shuffleButtons()

    '''
    Setzt alle vorhandenen Buttons auf setEnabled(True)
    '''
    def activateAllButtons(self):
        self.view.pushButton.setEnabled(True)
        self.view.pushButton_2.setEnabled(True)
        for pushButton in self.buttonList:
            pushButton.setEnabled(True)

    '''
    Verbindet die Buttons mit den Callbacks
    '''
    def connectButtons(self):
        # verbindet die die Callbacks mit den Button
        for button in self.buttonList:
            button.clicked.connect(self.buttonCallbacks)

        # Der Neu Start Button wird mit der neuStart() Methode verknuepft
        self.view.pushButton_2.clicked.connect(self.neuStart)
        # Der Beenden Button schliest die Applikation
        self.view.pushButton.clicked.connect(self.closeApp)

    '''
    Schliesst das Fenster
    '''
    def closeApp(self):
        sys.exit(0);

    '''
    Ueberprueft was passieren soll nachdem ein Button geklickt wird
    '''
    def buttonCallbacks(self):
        sender = self.sender()
        # Damit der Sender eh ein QPushButton ist
        if type(sender) == QPushButton:
            value = int(sender.text())
            print (value)

            if value == 1:
                self.startTime = time()
            if value == self.model.aktuell:
                self.model.buttonKlickKorrekt()
                sender.setEnabled(False)
            else:
                self.model.buttonKlickFalsch()

            self.updateLabels()
        else:
            raise RuntimeError("A sender of the type '" + type(sender) + "' was found in button callback method")

        if self.model.verbleibend == 0:
            self.endTime = time()
            self.timeDiff = self.endTime - self.startTime
            self.winWindow()



    '''
    Veraendert die Rheinfolge der buttonList und nummeriert diese dann durch
    '''
    def shuffleButtons(self):
        self.model.reset()
        # wuerfelt die Rheinfolge der Buttons durch
        shuffle(self.buttonList)

        # beschriftet die Buttons aufsteigend
        help = 1
        for button in self.buttonList:
            button.setText(str(help))
            help += 1

        self.updateLabels()

    '''
    Updated all die Labels in der View
    '''
    def updateLabels(self):
        self.view.label_korrekt.setText(str(self.model.korrekt))
        self.view.label_offen.setText(str(self.model.verbleibend))
        self.view.label_gesamt.setText(str(self.model.gesamt))
        self.view.label_spiele.setText(str(self.model.spiele))
        self.view.label_falsch.setText(str(self.model.falsch))

    '''
    Ein Fenster wird aufgerufen, dass dir sagt, dass du gewonnen hast JUHU
    '''
    def winWindow(self):
        q = QMessageBox()
        q.setWindowTitle("Fertig!")
        q.setTextFormat(Qt.RichText)
        q.setText("<center>Schritte benötigt: " + str(self.model.gesamt) + "</center>" + "\n" +
                  "<center>Zeit benötigt: " + str(self.timeDiff) + "</center>")
        q.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = Controller()
    controller.show()
    sys.exit(app.exec_())
