class Model():
    '''
    Konstruktor fuer Model
    '''
    def __init__(self, buttonLen):
        self.aktuell = 1
        self.buttonLen = buttonLen
        self.verbleibend = buttonLen
        self.korrekt = 0
        self.falsch = 0
        self.gesamt = 0
        self.spiele = 0

    '''
    Resetet die Werte fuer die View
    '''
    def reset(self):
        self.verbleibend = self.buttonLen
        self.korrekt = 0
        self.falsch = 0
        self.gesamt = 0
        self.aktuell = 1

    '''
    Zaehlt die Werte fuer die View richtig hoch falls der richtige Button gedrueckt wurde
    '''
    def buttonKlickKorrekt(self):
        self.aktuell += 1
        self.korrekt += 1
        self.verbleibend -= 1
        self.gesamt += 1

    '''
    Zaehlt die Werte fuer die View richtig hoch falls der falsche Button gedrueckt wurde
    '''
    def buttonKlickFalsch(self):
        self.falsch += 1
        self.gesamt += 1