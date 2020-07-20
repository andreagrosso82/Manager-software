#############################################################################
# Filename    : Modifica_DB.py
# Description : Modifico il database
# Author      : Andrea Grosso
# Date        : 20-07-2020
# Revision    : R1
# note        : Inizio la stesura del programma per la modifica del database
#               la modifica dei dati con i dizionari non mi convince molto
########################################################################
# Importo le librerie che mi interessano
import datetime
from datetime import date
from time import strftime
import Manager_software
import Lettura_DB
from os.path import isfile
from time import strftime
import Settimane
import sqlite3
# Definisco le funzioni che mi servono

def controllo_Progetti(file_name,dati_da_modificare):                                                                                     # funzione che mi controlla le ore per settimana
    Data_Base = sqlite3.connect(file_name)                                                                              # apre il file il sqlite con il nome che gli ho dato
    c = Data_Base.cursor()
    Nome_Table = "'Week " + str(dati_da_modificare[0]) + "'"
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
        if project == dati_da_modificare[1]:
            informazioni={"ID":row[0],
                          "week": row[1],
                          "designer": row[2],
                          "project": row[3],
                          "phaseoftheproject": row[4],
                          "kindofproject": row[5],
                          "drawing": row[6],
                          "timetodesign": row[7],
                          "deadline": row[8],
                          "state": row[9],
                          "date_login":row[10]}
            print(informazioni)
            new_state=input('definisci lo stato del progetto (In progress, Ready to review, Amendments, Close, On hold) \n')
            informazioni["state"]=new_state
            modifica_dati(file_name, informazioni)


def modifica_dati(file_name, informazioni):
    Data_Base = sqlite3.connect(file_name)                                                                              # apre il file il sqlite con il nome che gli ho dato
    c = Data_Base.cursor()
    Nome_Table = "'Week " + str(informazioni['week']) + "'"
    print(Nome_Table)
    c.execute("UPDATE " + Nome_Table + 'SET State_Design = %s WHERE State_Design = In progress',
              (informazioni['state']))
    Data_Base.commit()
    Data_Base.close()




# Main proram
if __name__ == "__main__":
    print("Modifichiamo progetto esistente")
    settimana_corrente = date.today().isocalendar()[1]
    file_name = str(Manager_software.genera_nome()) + ".db"
    print('La settimana corrente è ' + str(settimana_corrente) + '\n')
    scegli_week = input("Vuoi vedere l'elenco delle settimane (Y/N) \n")
    if scegli_week.capitalize() == 'Y':
        Settimane.elenco_settimane()
        week = input('Introduci la settimana \n')
    if scegli_week.capitalize() == 'N':
        week = input('Introduci la settimana \n')
    if scegli_week.capitalize() != 'Y' and scegli_week.capitalize() != 'N':
        print("La risposta che hai introdotto non e' corretta")
    progetto = input('Inserisci il nome del progetto di cui vuoi modificare le informazioni \n')
    #drawing = input('Introduci il tipo di drawing che deve modificare(GW,PLR,PID,ELE,CSD) \n')
    #state = input('definisci lo stato del progetto (In progress, Ready to review, Amendments, Close, On hold) \n')
    dati_da_modificare = [week, progetto.capitalize()]
    controllo_Progetti(file_name, dati_da_modificare)

