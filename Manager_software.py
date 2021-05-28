#############################################################################
# Filename    : Manager_software.py
# Description : programma che mi aiuta a gestire le ore che il mio team deve spendere per design
# Author      : Andrea Grosso
# Date        : 18.03.2021
# Revision    : R3
# note        : Aggiunto Sale Support e note durante la creazione della tabella
#             : Vedere di gestire il numero di caratteri per i commenti (Max 20)
#             : Modificato il nome del database (ne crea solo uno grande all'anno)
#             : Iniziato ad aggiungere il project manager (RIMOSSO)
#             ; Modificato la parte di creazione del database
########################################################################
# Importo le librerie che mi interessano
from datetime import date
import datetime
import sqlite3
import time
from os.path import isfile

# Definisco le costanti che mi servono
file_name = 'Project_database.db'

# Definisco le funzioni che mi servono

def data_corretta():
    data = datetime.date.today()                                                                                        # importa la data corrente
    data_corretta = str(data)                                                                                           # converte la data in formato string
    anno = (data_corretta[0:4])                                                                                         # definisce la variabile anno
    mese = (data_corretta[5:7])                                                                                         # definisce la variabile mese
    giorno = (data_corretta[8:10])                                                                                      # definisce la variabile giorno
    corretto_ordine=(giorno, '-', mese, '-', anno)                                                                      # stampa la data e l'ora
    data_corretta= ''.join(corretto_ordine)                                                                             # convertere il tulpe in stringa
    return(data_corretta)


def controllo_database(file_name):
    if not isfile(file_name):  # controlla se il file esiste gia' o deve essere creato
        DataBase = Crea_DB(file_name)
        DataBase.genera_file()
        DataBase.genera_tabella()
    else:
        print("Il file esiste gia'")
        DataBase = Crea_DB(file_name)
        DataBase.genera_tabella()


def controllo_ID(file_name):
    Data_Base = sqlite3.connect(file_name)  # apre il file il sqlite con il nome che gli ho dato
    c = Data_Base.cursor()
    date = datetime.datetime.now()
    month = (date.strftime("%B"))
    Nome_Table = str(month)
    c.execute("SELECT * FROM " + Nome_Table)
    rows = c.fetchall()
    for row in rows:
        ID = (row[0] + 1)
    return (ID)

# Muovere questa funzione nel Indice Generale file (Lascia cosi' per il momento)
def Interfaccia(ID):                                                                                                    # funzione che mi completa la tebella con le funzioni che ho bisogno
    Lista = {}
    Lista['ID'] = ID
    date = data_corretta()
    Lista['date'] = date
    designer = input('Introduci il nome del designer (Tom, Dinda, Dyanda, Luke, Andrea) \n')
    Lista['designer'] = designer.capitalize()
    project = input('Introduci il nome del progetto \n')
    Lista['project'] = project.capitalize()
    kindofproject = input('Definisci la natura del disegno che hai bisogno (New, Replace) \n')
    if kindofproject.capitalize() != 'New' and kindofproject.capitalize() != 'Replace':
        print('Non hai inserito la corretta risposta alla domanda, leggi la domanda con maggior attenzione')
        kindofproject = input('Definisci la natura del disegno che hai bisogno (New, Replace) \n')
    Lista['kindofproject'] = kindofproject.capitalize()
    phaseoftheproject = input("Il progetto a che punto è? (In_progress, Complete) \n")
    if phaseoftheproject.capitalize() != 'In_progress' and phaseoftheproject.capitalize() != 'Complete':                #gestisce l'errore nel caso non introduco il corretto valore
        print('Non hai inserito la risposta corretta alla domanda, leggi la domanda con maggior attenzione!!')
        phaseoftheproject = input("Il progetto a che punto è? (In Progress, Complete) \n")
    Lista['phaseoftheproject'] = phaseoftheproject.capitalize()                                                                      # genero la lista da passare al database
    return(Lista)


# Definisco le classi che mi servono

class Crea_DB:
    def __init__(self, file_name):
        self.file_name = file_name
        return

    def genera_file(self):                                                                                              # genera il file
        Data_Base = sqlite3.connect(self.file_name)                                                                     # apre il file il sqlite con il nome che gli ho dato
        Data_Base.commit()
        Data_Base.close()
        print('File creato')
        return

    def genera_tabella(self):                                                                                           # genera la tabella con la data corrente
        Data_Base = sqlite3.connect(self.file_name)                                                                     # apre il file il sqlite con il nome che gli ho dato
        c = Data_Base.cursor()
        date = datetime.datetime.now()
        month = (date.strftime("%B"))
        Nome_Table = str(month)
        sql_cmd = '''CREATE TABLE IF NOT EXISTS {}
                        (ID INT PRIMARY KEY NOT NULL,
                        Date TEXT KEY NOT NULL,
                        Designer TEXT NOT NULL, 
                        Project TEXT NOT NULL,
                        Kind_of_project TEXT NOT NULL,
                        Phase_of_the_project TEXT NOT NULL)'''.format(Nome_Table)
        c.execute(sql_cmd)
        Data_Base.commit()
        Data_Base.close()
        print('Tabella creata')
        return


class Database_Progetti:
    def __init__(self, ID, date, designer, project, kindofproject, phaseoftheproject):
        self.ID = ID
        self.date = date
        self.designer = designer
        self.project = project
        self.kindofproject = kindofproject
        self.phaseoftheproject = phaseoftheproject
        return


    def genera_database(self, file_name):
        Data_Base = sqlite3.connect(file_name)                                                                          # apre il file il sqlite con il nome che gli ho dato
        c = Data_Base.cursor()
        date = datetime.datetime.now()
        month = (date.strftime("%B"))
        Nome_Table = "'" + str(month) + "'"
        c.execute("INSERT INTO " + Nome_Table + 'VALUES (?, ?, ?, ?, ?, ?)', (self.ID, self.date, self.designer, self.project, self.kindofproject, self.phaseoftheproject))
        Data_Base.commit()
        Data_Base.close()
        print('Data base creato')
        return


#ID = 1
#while True:
    #controllo_database(file_name)
    #ID = controllo_ID(file_name)
    #Lista = Interfaccia(ID)
    #print(Lista)
    #progetto = Database_Progetti(Lista['ID'], Lista['date'], Lista['designer'], Lista['project'], Lista['kindofproject'], Lista['phaseoftheproject'])
    #progetto.genera_database(file_name)
    #Progetti = Database_Progetti(Lista['ID'],Lista['date'],Lista['designer'], Lista['project'],Lista['kindofproject'],Lista['phaseoftheproject']) #--> da un errore qui, penso sia dovuto al fatto che uso una lista, provare con i dizionari
    #Progetti.genera_database(file_name)
    #ID = controllo_ID(file_name)
    #a = input ('Introduci il valore di , a /n')
    #tot = tot + int(a)
    #print(tot)
    #
        #break