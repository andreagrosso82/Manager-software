#############################################################################
# Filename    : Modifica_DB.py
# Description : aggiorna database
# Author      : Andrea Grosso
# Date        : 16/07/20
# Revision    : R0
# note        : Mi permette di modificare il database esistente
########################################################################
# Importo le librerie che mi interessano
from datetime import date
import datetime
import sqlite3
import time
from os.path import isfile
import Lettura_DB
import Manager_software


# Definisco le funzioni che mi servono
def modifica_progetto(dati_da_modificare):                                                                       # funzione che mi controlla i progetti per settimana
    print(dati_da_modificare[3])
    Data_Base = sqlite3.connect(dati_da_modificare[0])                                                                              # apre il file il sqlite con il nome che gli ho dato
    c = Data_Base.cursor()
    Nome_Table = "'Week " + dati_da_modificare[1] + "'"
    c.execute("SELECT * FROM" + Nome_Table)
    rows = c.fetchall()
    for row in rows:
        ID = row[0]
        week = row[1]
        designer = row[2]
        project = row[3]
        phaseoftheproject = row[4]
        kindofproject = row[5]
        drawing = row[6]
        timetodesign = row[7]
        deadline = row[8]
        state = row[9]
        date_login = row[10]
        if designer == dati_da_modificare[2] and project == dati_da_modificare[3]:
            print(row[6]+row[9])




def controllo_Progetti(file_name, dati_da_leggere):                                                                      # funzione che mi controlla le ore per settimana
    Data_Base = sqlite3.connect(file_name)                                                                              # apre il file il sqlite con il nome che gli ho dato
    c = Data_Base.cursor()
    Nome_Table = "'Week " + str(dati_da_leggere[0]) + "'"
    c.execute("SELECT * FROM" + Nome_Table)
    rows = c.fetchall()
    for row in rows:
        ID = row[0]
        week = row[1]
        designer = row[2]
        project = row[3]
        phaseoftheproject = row[4]
        kindofproject = row[5]
        drawing = row[6]
        timetodesign = row[7]
        deadline = row[8]
        state = row[9]
        date_login = row[10]
        if designer == dati_da_leggere[1]:
            if state == 'In progress':
                print(designer + " sta lavorando su: " + project + " e sul disegno: " + drawing
                  + " di cui ci vogliono:" + str(timetodesign) + " il disegno e' per il " + deadline)


def progetti_to_review(file_name,dati_da_leggere):                                                                      # funzione che mi controlla i project to review
    Data_Base = sqlite3.connect(file_name)                                                                              # apre il file il sqlite con il nome che gli ho dato
    c = Data_Base.cursor()
    Nome_Table = "'Week " + str(dati_da_leggere[0]) + "'"
    c.execute("SELECT * FROM" + Nome_Table)
    rows = c.fetchall()
    for row in rows:
        ID = row[0]
        week = row[1]
        designer = row[2]
        project = row[3]
        phaseoftheproject = row[4]
        kindofproject = row[5]
        drawing = row[6]
        timetodesign = row[7]
        deadline = row[8]
        state = row[9]
        date_login = row[10]
        if designer == dati_da_leggere[1]:
            if state == 'Ready to review':
                print('il ' + project + ' ' + drawing + ' ' + 'deve essere controllato')


# Main proram
if __name__ == "__main__":
    file_name = str(Manager_software.genera_nome()) + ".db"
    week = input('Introduci la settimana \n')
    designer = input('Inserisci il nome del designer di cui vuoi vedere le informazioni \n')
    dati_da_leggere = [week, designer.capitalize()]
    Lettura_DB.controllo_Progetti(file_name, dati_da_leggere)
    progetto = input('Introduci il progetto che vuoi modificare \n')
    dati_da_modificare = [file_name, week, designer.capitalize(), progetto.capitalize()]
    modifica_progetto(dati_da_modificare)