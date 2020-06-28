#############################################################################
# Filename    : Template.py
# Description :
# Author      :
# Date        :
# Revision    :
# note        :
########################################################################
# Importo le librerie che mi interessano

# Definisco le funzioni che mi servono


# Main proram
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
Lista = ["2", "26", "Andrea", "Test2", "Design", "New", "PLR", "3.0", "30-06-2020", "In Progress", "27-06-2020"]
progetto_test_2 = Progetto(Lista[0], Lista[1], Lista[2], Lista[3], Lista[4], Lista[5], Lista[6], Lista[7], Lista[8], Lista[9], Lista[10])
print(progetto_test_2.descrizione_progetto())