#############################################################################
# Filename    : Template.py
# Description :
# Author      :
# Date        :
# Revision    :
# note        :
########################################################################
# Importo le librerie che mi interessano
import collections
from collections import Counter
# Definisco le funzioni che mi servono


# Main proram
list = [1,2,3,4,1,2,6,7,3,8,1,5,1,45,7,7,8,9,1,9,9,7,2,3,4,2,7]
cnt = Counter(list)
print(cnt)
print(cnt[1])
print(cnt[2])
print(cnt[3])
#print(list(cnt.elements()))
# Definisco le classi che mi servono
class Progetto:
    def __init__(self, ID, week, designer, project, site_visit, kindofproject, drawing, timetodesign, deadline, state, date_login):
        self.ID = ID
        self.week = week
        self.designer = designer
        self.project = project
        self.site_visit = site_visit
        self.kindofproject = kindofproject
        self.drawing = drawing
        self.timetodesign = timetodesign
        self.deadline = deadline
        self.state = state
        self.date_login = date_login

    def descrizione_progetto(self):
        return f"ID:{self.ID}\n Week:{self.week}\n Designer:{self.designer}\n Project:{self.project}\n" \
               f"Site visit:{self.site_visit}\n Kind of project:{self.kindofproject}\n Drawing:{self.drawing}\n" \
               f"Time to design:{self.timetodesign}\n Deadline:{self.deadline}\n State:{self.state}\n Date Login:{self.date_login}\n"

Lista = ["1", "26", "Andrea", "Test1", "Design", "New", "ELE", "3.0", "30-06-2020", "In Progress", "27-06-2020"]
progetto_test_1 = Progetto(Lista[0], Lista[1], Lista[2], Lista[3], Lista[4], Lista[5], Lista[6], Lista[7], Lista[8], Lista[9], Lista[10])
print(progetto_test_1.descrizione_progetto())
#Lista = ["2", "26", "Andrea", "Test2", "Design", "New", "PLR", "3.0", "30-06-2020", "In Progress", "27-06-2020"]
#progetto_test_2 = Progetto(Lista[0], Lista[1], Lista[2], Lista[3], Lista[4], Lista[5], Lista[6], Lista[7], Lista[8], Lista[9], Lista[10])
#print(progetto_test_2.descrizione_progetto())

class Addizione:
    def __init__(self, addendo1, addendo2):
        self.addendo1 = addendo1
        self.addendo2 = addendo2

    def Controllo_numeri(self):
        if self.addendo1 > self.addendo2:
            print('posso fare la sottrazione tra i due')
            sottrazione = (int(self.addendo1) - int(self.addendo2))
            print('La sottrazione dei due numeri è', sottrazione)
        else:
            print('non posso fare la sottrazione tra i due')
    def somma(self):
        somma = (int(self.addendo1)+int(self.addendo2))
        print('La somma dei due numeri è', somma)
    def moltiplicazione(self):
        moltiplicazione = (int(self.addendo1)*int(self.addendo2))
        print('La moltiplicazione dei due numeri è', moltiplicazione)
    def Sottrazione(self):
        sottrazione = (int(self.addendo1)-int(self.addendo2))
        print('La sottrazione dei due numeri è', sottrazione)


#while True:
    #addendo1 = input('inserisci un numero \n')
    #addendo2 = input('inserisci un numero \n')
    #due_numeri = Addizione(addendo1, addendo2)
    #due_numeri.Controllo_numeri()
    #due_numeri.somma()
    #due_numeri.moltiplicazione()